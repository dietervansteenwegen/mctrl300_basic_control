#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'

import logging

# from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from .config import Config
from .log import DialogLog
from .serports import ConnStatus, SerConnection
from .ui_sources.mainwindow import Ui_MainWindow

log = logging.getLogger(__name__)


class MainWindow(Ui_MainWindow, qtw.QMainWindow):
    sgn_ser_conn_check_status = qtc.Signal()
    sgn_change_conn = qtc.Signal(str, ConnStatus)  # (portname, status)

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__()
        self.setupUi(self)
        self._setup_dialog_log()
        self.setStatusBar(qtw.QStatusBar(self))
        self.ser_connection = SerConnection()
        # self.scr_status = ScreenStatus()
        self._setup_signals()
        self._setup_timers()

    def _setup_signals(self):
        self.sgn_ser_conn_check_status.connect(self.ser_connection.check_status)
        self.ser_connection.sgn_port_list_changed.connect(self._update_port_list)
        self.ser_connection.sgn_conn_changed.connect(self._ser_conn_has_changed)
        self.ser_connection.sgn_err_msg.connect(self._handle_ser_conn_err_msg)

    @qtc.Slot()
    def _handle_ser_conn_err_msg(self, msg: str):
        # TODO
        log.error(f'Serial connection error: {msg}')

    @qtc.Slot()
    def _ser_conn_has_changed(self, port: str, status):
        # TODO
        log.info(f'Connection status changed: {port} - {status}')

    def _setup_timers(self):
        self.timer_1s = qtc.QTimer(self)
        self.timer_1s.setInterval(1000)
        # self.timer_1s.timeout.connect(self._timer_timeout)
        self.timer_1s.timeout.connect(self.sgn_ser_conn_check_status.emit)
        self.timer_1s.start()

    def _setup_dialog_log(self):
        self.dialog_log: DialogLog = DialogLog(self)
        self.dialog_log.show()

    @qtc.Slot()
    def _update_port_list(self, port_list: tuple[str, str, str]):
        self.statusBar().showMessage('List of serial ports changed', 2000)
        self.lst_serial_ports.clear()
        for port, manufacturer, product in port_list:
            self.lst_serial_ports.addItem(f'{port} ({manufacturer}: {product})')


def start_gui(config: Config) -> None:
    app = qtw.QApplication([])
    ui = MainWindow(config)  # noqa: F841
    ui.show()
    _ = app.exec_()


def run(config: Config):
    """Main command line entry point."""
    start_gui(config)  # noqa: F821
