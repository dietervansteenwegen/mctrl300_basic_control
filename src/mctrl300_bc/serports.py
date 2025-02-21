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
    DISCONNECTED = 0
    CONNECTED = 1


class SerConnection(qtc.QObject):
    sgn_conn_changed = qtc.Signal(str, ConnStatus)  # (portname, status)
    sgn_port_list_changed = qtc.Signal(tuple)  # (port, manufacturer, product)
    sgn_err_msg = qtc.Signal(str)  # Error message

    def __init__(self):
        super().__init__()
        self._reset()

    def _reset(self):
        self.port: serial.Serial = None
        self.conn_status: ConnStatus = ConnStatus.DISCONNECTED
        self._available_ports = ()

    @qtc.Slot()
    def change_status(self, str_port, status):
        pass

    @qtc.Slot()
    def check_status(self):
        available_ports = self.get_available_ports()
        if len(available_ports) != len(self._available_ports):
            self._available_ports = available_ports
            self.sgn_port_list_changed.emit(available_ports)

    def open(self, port: str, baudrate: int = DEFAULT_BAUDRATE, timeout: int = DEFAULT_TIMEOUT):
        self.port = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        self.port.open()
        return self.check_port()

    def check_port(self):
        if self.port is None:
            self.conn_status = ConnStatus.NO_PORT
        if self.port.is_open:
            self.conn_status = ConnStatus.CONNECTED
        else:
            self.conn_status = ConnStatus.DISCONNECTED
        return self.conn_status()

    def close(self):
        if self.port is not None:
            self.port.close()
            self._reset()
        return self.check_port()

    @staticmethod
    def get_available_ports() -> list:
        ports = list_ports.comports(include_links=False)
        return [
            (port.device, port.manufacturer, port.product)
            for port in ports
            if port.manufacturer is not None
        ]


# class SerialPort(serial.Serial):
#     def __init__(self, port: str):
#         super().__init__(
#             port,
#             baudrate=BAUDRATE,
#             bytesize=serial.EIGHTBITS,
#             parity=serial.PARITY_NONE,
#             stopbits=serial.STOPBITS_ONE,
#             timeout=TIMEOUT,
#         )
