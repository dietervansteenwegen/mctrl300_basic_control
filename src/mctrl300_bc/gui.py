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
from .models import SerialPortModel
from .serial_handler import ConnAction, ConnStatus, SerialHandler
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
        self.ser_connection = SerialHandler()
        # self.scr_status = ScreenStatus()
        self._setup_models()
        self._setup_signals()
        self._setup_timers()

    def _setup_models(self):
        self.model_ports = SerialPortModel()
        self.tbl_serial_ports.setModel(self.model_ports)

    def _setup_signals(self):
        self.sgn_ser_conn_check_status.connect(self.ser_connection.check_status)
        self.sgn_change_conn.connect(self.ser_connection.change_status)
        self.ser_connection.sgn_port_list_changed.connect(self._update_port_table)
        self.ser_connection.sgn_conn_changed.connect(self._ser_conn_has_changed)
        self.ser_connection.sgn_err_msg.connect(self._handle_ser_conn_err_msg)
        self.btn_serial_open.clicked.connect(self._handle_btn_serial_open_click)

    @qtc.Slot()
    def _handle_btn_serial_open_click(self):
        # if self.tbl_serial_ports.select
        port_name = self.tbl_serial_ports.currentIndex().siblingAtColumn(0).data()
        if port_name:
            self.sgn_change_conn.emit(
                port_name,
                ConnAction.OPEN if self.btn_serial_open.isChecked() else ConnAction.CLOSE,
            )

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
        self.timer_1s.timeout.connect(self.sgn_ser_conn_check_status.emit)
        self.timer_1s.start()

    def _setup_dialog_log(self):
        self.dialog_log: DialogLog = DialogLog(self)
        self.dialog_log.show()

    @qtc.Slot()
    def _update_port_table(self, port_list: tuple[str, str, str]):
        self.model_ports.update(port_list)
        self.model_ports.layoutChanged.emit()
        self.tbl_serial_ports.resizeColumnsToContents()
        self.statusBar().showMessage('List of serial ports changed', 2000)


def start_gui(config: Config) -> None:
    app = qtw.QApplication([])
    ui = MainWindow(config)  # noqa: F841
    ui.show()
    _ = app.exec_()


def run(config: Config):
    """Main command line entry point."""
    start_gui(config)  # noqa: F821
