#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99


__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'

import enum
import logging

import serial
from PySide6 import QtCore as qtc
from serial.tools import list_ports

DEFAULT_BAUDRATE = 115200
DEFAULT_TIMEOUT = 4

log = logging.getLogger(__name__)


class ConnStatus(enum.Enum):
    NO_PORT = -1
    CLOSED = 0
    OPENED = 1


class ConnAction(enum.Enum):
    CLOSE = 0
    OPEN = 1


class SerialHandlerError(Exception):
    pass


class SerialStateError(SerialHandlerError):
    pass


class SerialHandler(qtc.QObject):
    sgn_conn_changed = qtc.Signal(str, ConnStatus)  # (portname, status)
    sgn_port_list_changed = qtc.Signal(tuple)  # (port, manufacturer, product)
    sgn_err_msg = qtc.Signal(str)  # Error message
    sgn_rx_data = qtc.Signal(bytearray)

    def __init__(self):
        """Initialize and set to default status."""
        super().__init__()
        self._reset()

    def _reset(self) -> None:
        """Reset the status to a default state.

        - Clears the `port` attribute,
        - Sets `conn_status` to `NO_PORT`,
        - Clears the list of available ports,
        - Signals that the list of ports and the connection has changed
        """
        self.port: serial.Serial = None
        self.conn_status: ConnStatus = ConnStatus.NO_PORT
        self._available_ports = ()
        self.sgn_port_list_changed.emit(self._available_ports)
        self.sgn_conn_changed.emit('', self.conn_status)

    @qtc.Slot()
    def check_available_ports(self) -> None:
        """Checks/updates the list of available ports.

        - Get list of available ports
        - Set them as `CLOSED`
        - If the list is different from the `_available_ports` attribute, update it and
            emit the `sgn_port_list_changed` signal
        """
        # Should do/todo:
        #   - check if portlist is still acurate -> If not -> update/signal
        #   - check if current port is still available -> If not -> set to None and update/signal
        #   - check if current port is still open -> If not -> set to closed and update/signal
        available_ports = self.get_available_ports()
        for port in available_ports:
            port.append(ConnStatus.CLOSED)
        if available_ports != self._available_ports:
            self._available_ports = available_ports
            self.sgn_port_list_changed.emit(available_ports)

    @qtc.Slot()
    def change_status(self, str_port: str, conn_action: ConnAction):
        """Change status (connect/disconnect) of `str_port`.

        Args:
            str_port (str): name/identifier of port to open (e.g. 'COM3' or '/dev/tty01')
            conn_action (ConnAction): Open or close the port
        """
        # TODO: Error handling and additional checking
        if conn_action == ConnAction.OPEN:
            self.open(str_port)
        else:
            self.close(str_port)

    def send(self, data: bytearray) -> None:
        """Send data to the serial port.

        Send data to serial port if it is available and open.

        Args:
            data (bytearray): Data to be sent to the serial port.

        Raises:
            SerialStateError: If port is not available or not open.
        """
        if self.port is None or not self.port.is_open:
            err_msg = 'Port is not open. Cannot send data.'
            log.error(err_msg)
            self.sgn_err_msg.emit(err_msg)
            raise SerialStateError(err_msg)
        else:
            self.port.write(data)

    def receive(self, size: int) -> bytearray:
        """Receive data from the port.

        Attempts to receive `size` bytes from the port (until timeout) and returns them.

        Args:
            size (int): number of bytes to receive

        Returns:
            bytearray: data received from port

        Emits:
            sgn_rx_data: if data is read
            sgn_err_msg: if port is not available or not open
        """
        if self.port is None or not self.port.is_open:
            err_msg = 'Port is not open. Cannot receive data.'
            log.error(err_msg)
            self.sgn_err_msg.emit(err_msg)
        else:
            self.sgn_rx_data.emit(self.port.read(size))  # TODO: check if amount of data is correct

    def open(self, port: str, baudrate: int = DEFAULT_BAUDRATE, timeout: int = DEFAULT_TIMEOUT):
        """Open a serial port with given parameters.

        Args:
            port (str): Name of the port (e.g. 'COM1', '/dev/ttyUSB0').
            baudrate (int, optional): Port baudrate. Defaults to DEFAULT_BAUDRATE.
            timeout (int, optional): Timeout in seconds. Defaults to DEFAULT_TIMEOUT.
        """
        if self.port is not None and self.port.is_open:
            self.close(port)
            self.port = None
            self.sgn_conn_changed.emit(self.port.port if self.port else '', self.conn_status)

        if self.port is None:
            try:
                self.port = serial.Serial(
                    port=port,
                    baudrate=DEFAULT_BAUDRATE,
                    timeout=DEFAULT_TIMEOUT,
                )
                if not self.port.is_open:
                    err_msg = 'Port did not open. No exception raised.'
                    raise serial.SerialException(err_msg)
            except serial.SerialException as e:
                err_msg = f'Error while opening {port}: {e}'
                log.error(err_msg)
                self.sgn_err_msg.emit(err_msg)
                # TODO: raise SerialHandlerError?
            else:
                self.sgn_conn_changed.emit(self.port.port, ConnStatus.OPENED)

    def close(self, port: str) -> None:
        """Close `port`

        Args:
            port (str): Port to close

        Emits:
            sgn_err_msg: If `port` does not match the current active port
        """
        if self.port and self.port.port == port:
            self.port.close()
            self._reset()
        else:
            err_msg = f'Trying to close {port} but current active port is {self.port}'
            self.sgn_err_msg.emit(err_msg)

    def check_port(self) -> ConnStatus:
        """Check status of the current selected port and update the `conn_status` attribute
        if necessary.

        Returns:
            ConnStatus: Connection status of the selected port (`port` attribute)

        Emits:
            sgn_conn_changed: If connection status has changed
        """
        if self.port is None:
            conn_status = ConnStatus.NO_PORT
        elif self.port.is_open:
            conn_status = ConnStatus.OPENED
        else:
            conn_status = ConnStatus.CLOSED
        if conn_status != self.conn_status:
            self.conn_status = conn_status
            self.sgn_conn_changed.emit(self.port.port if self.port else '', self.conn_status)
        return self.conn_status

    @staticmethod
    def get_available_ports() -> list[str, str, str]:
        """Get available ports.

        Returns:
            list: List of [device, manufacturer, product] sorted by device
        """
        ports = list_ports.comports(include_links=False)
        ports.sort(key=lambda port: port.device)
        # log.info(ports_sorted)
        return [
            [port.device, port.manufacturer, port.product]
            for port in ports
            if port.manufacturer is not None
        ]
