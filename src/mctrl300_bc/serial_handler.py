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
        available_ports = self.get_available_ports()
        for port in available_ports:
            port.append(ConnStatus.CLOSED)
        if available_ports != self._available_ports:
            self._available_ports = available_ports
            self.sgn_port_list_changed.emit(available_ports)

    @qtc.Slot()
    def change_status(self, str_port, conn_action: ConnAction):
        if conn_action == ConnAction.OPEN:
            self.open(str_port)
        else:
            self.close(str_port)
        # TODO: Error handling and additional checking

        # try:
        #     self.port = serial.Serial(str_port,
        #                               baudrate=DEFAULT_BAUDRATE,
        #                               timeout=DEFAULT_TIMEOUT,
        #                               write_timeout=DEFAULT_TIMEOUT,
        #                       )
        #     self.port.open()
        #     if self.port.is_open:
        #         self.conn_status = ConnStatus.CONNECTED
        # except serial.SerialException as e:

    def open(self, port: str, baudrate: int = DEFAULT_BAUDRATE, timeout: int = DEFAULT_TIMEOUT):
        if self.port is not None and self.port.is_open:
            self.close(port)
            self.port = None
            self.sgn_conn_changed.emit(self.port.port if port else '', self.conn_status)

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

    # def close(self, port: str):
    #     try:
    #         if not self.port.port == port:
    #             raise ValueError
    #         self.port.close()
    #     except:  # noqa: E722, S110
    #         pass  # TODO
    #     if self.port is not None and self.port.is_open:
    #         self.port.close()
    #         self.conn_status = ConnStatus.CLOSED
    #         self.sgn_conn_changed.emit('', self.conn_status)
    #     else:
    #         err_msg = (
    #             f'Want to close port {port} but current port is {self.port.port},  '
    #             f'is_open: {self.port.is_open == True}'
    #         )
    #         log.error(err_msg)
    #         self.sgn_err_msg.emit(err_msg)

    def check_port(self):
        if self.port is None:
            self.conn_status = ConnStatus.NO_PORT
        if self.port.is_open:
            self.conn_status = ConnStatus.OPENED
        else:
            self.conn_status = ConnStatus.CLOSED
        return self.conn_status()

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
