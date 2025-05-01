#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'

import logging
import sys

# from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from .common import UIStatus
from .config import Config
from .log import DialogLog
from .models import SerialPortModel
from .serial_handler import ConnAction, ConnStatus, SerialHandler
from .ui_sources.mainwindow import Ui_MainWindow

log = logging.getLogger(__name__)


class MainWindow(Ui_MainWindow, qtw.QMainWindow):
    sgn_ser_conn_check_status = qtc.Signal()
    sgn_change_conn = qtc.Signal(str, ConnStatus)  # (portname, status)
    sgn_change_uistatus = qtc.Signal(UIStatus)

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__()
        self.destroyed.connect(sys.exit)
        self.setupUi(self)
        self._setup_dialog_log()
        self.setStatusBar(qtw.QStatusBar(self))
        self.ser_connection = SerialHandler()
        # self.scr_status = ScreenStatus()
        self._setup_models()
        self._setup_signals()
        self._setup_timers()
        self._emit_signals()

    def _setup_models(self) -> None:
        """Set up models and link with widgets."""
        self.model_ports = SerialPortModel()
        self.tbl_serial_ports.setModel(self.model_ports)

    def _setup_signals(self) -> None:
        """Connect signals."""
        # self.sgn_change_uistatus.connect(self._update_ui_elements)
        self.sgn_ser_conn_check_status.connect(self.ser_connection.check_available_ports)
        self.sgn_change_conn.connect(self.ser_connection.change_connection)
        self.ser_connection.sgn_port_list_changed.connect(self._update_port_table)
        self.ser_connection.sgn_conn_changed.connect(self._ser_conn_has_changed)
        self.ser_connection.sgn_err_msg.connect(self._handle_ser_conn_err_msg)
        self.btn_serial_open.clicked.connect(self._handle_btn_serial_open_click)
        self.menu_show_logs.triggered.connect(self._handle_show_logs_dialog_changed)

    @qtc.Slot()
    def _emit_signals(self) -> None:
        self.sgn_change_conn.emit(None, ConnStatus.NO_PORT)

    @qtc.Slot()
    def _handle_show_logs_dialog_changed(self) -> None:
        if self.menu_show_logs.isChecked():
            self.dialog_log.show()
        else:
            self.dialog_log.hide()

    @qtc.Slot()
    def _update_ui_elements(self) -> None:
        """Update UI elements based on the current state of the application.

        This method is called when the connection status changes or when the available ports
        are updated.
        """
        pass

    @qtc.Slot()
    def _handle_btn_serial_open_click(self) -> None:
        """Handle a click event on the open/close button.

        If a port is selected in the `tbl_serial_ports`, attempt to open or close it (depending on
            the button isChecked() state).
        """
        port_name = self.tbl_serial_ports.currentIndex().siblingAtColumn(0).data()
        if port_name:
            self.sgn_change_conn.emit(
                port_name,
                ConnAction.OPEN if self.btn_serial_open.isChecked() else ConnAction.CLOSE,
            )

    @qtc.Slot()
    def _handle_ser_conn_err_msg(self, msg: str):
        """Handle an incoming error message.

        # TODO

        Args:
            msg (str): The incoming error message.
        """
        # TODO
        log.error(f'Serial connection error: {msg}')

    def _change_ui_state(self, state: UIStatus) -> None:
        self.cmb_output.setEnabled(state >= UIStatus.PORT_OPENED)
        output_selected: bool = self.cmb_output.currentIndex() != 0
        self.grp_patterns.setEnabled(state >= UIStatus.PORT_OPENED and output_selected)
        self.grp_brightness.setEnabled(state >= UIStatus.PORT_OPENED and output_selected)

    @qtc.Slot()
    def _ser_conn_has_changed(self, port: str, status) -> None:
        if not port or status != ConnStatus.OPENED:
            self.btn_serial_open.setChecked(False)
            self.lbl_serial_status.setText('No port opened')
            self.lbl_serial_status.setStyleSheet('color: #EE0000')

        elif status == ConnStatus.OPENED:
            self.cmb_output.setEnabled(True)
            self.lbl_serial_status.setStyleSheet('color: #00EE00')
            self.lbl_serial_status.setText(f'Port {port} is OPEN')
        # TODO
        log.info(f'Connection status changed: {port} - {status}')
        self._update_ui_elements()

    def _setup_timers(self) -> None:
        """Set up timers."""
        self.timer_1s = qtc.QTimer(self)
        self.timer_1s.setInterval(1000)
        self.timer_1s.timeout.connect(self.sgn_ser_conn_check_status.emit)
        self.timer_1s.start()

    def _setup_dialog_log(self) -> None:
        self.dialog_log: DialogLog = DialogLog(self)
        self.dialog_log.show()

    @qtc.Slot()
    def _update_port_table(self, port_list: tuple[str, str, str]) -> None:
        self.model_ports.update(port_list)
        self.model_ports.layoutChanged.emit()
        self.tbl_serial_ports.resizeColumnsToContents()
        self.statusBar().showMessage('List of serial ports changed', 2000)


def start_gui(config: Config) -> None:
    app = qtw.QApplication([])
    ui = MainWindow(config)  # noqa: F841
    ui.show()
    _ = app.exec_()


def run(config: Config) -> None:
    """Main command line entry point."""
    start_gui(config)  # noqa: F821
