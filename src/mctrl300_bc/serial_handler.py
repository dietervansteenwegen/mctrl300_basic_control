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
        super().__init__()
        self._reset()

    def _reset(self):
        self.port: serial.Serial = None
        self.conn_status: ConnStatus = ConnStatus.NO_PORT
        self._available_ports = ()
        self.sgn_port_list_changed.emit(self._available_ports)
        self.sgn_conn_changed.emit('', self.conn_status)

    @qtc.Slot()
    def check_status(self):
        # Should do:
        #   - check if portlist is still acurate -> If not -> update/signal
        #   - check if current port is still available -> If not -> set to None and update/signal
        #   - check if current port is still open -> If not -> set to closed and update/signal
        available_ports = self.get_available_ports()
        for port in available_ports:
            port.append(ConnStatus.CLOSED)
        if available_ports != self._available_ports:
            self._available_ports = available_ports
            self.sgn_port_list_changed.emit(available_ports)
            return self.check_port()

    @qtc.Slot()
    def change_status(self, str_port, conn_action: ConnAction):
        if conn_action == ConnAction.OPEN:
            self.open(str_port)
        else:
            self.close(str_port)
        # TODO: Error handling and additional checking

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
        if self.port is None or not self.port.is_open:
            err_msg = 'Port is not open. Cannot receive data.'
            log.error(err_msg)
            self.sgn_err_msg.emit(err_msg)
            return bytearray()
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
        if self.port and self.port.port == port:
            self.port.close()
            self._reset()
            return self.check_port()
        else:
            err_msg = f'Trying to close {port} but current active port is {self.port}'
            self.sgn_err_msg.emit(err_msg)

    def check_port(self):
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
    def get_available_ports() -> list:
        ports = list_ports.comports(include_links=False)
        ports.sort(key=lambda port: port.device)
        # log.info(ports_sorted)
        return [
            [port.device, port.manufacturer, port.product]
            for port in ports
            if port.manufacturer is not None
        ]
