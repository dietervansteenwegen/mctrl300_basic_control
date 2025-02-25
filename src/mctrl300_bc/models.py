#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'

import logging

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

log = logging.getLogger(__name__)


class SerialPortModel(qtc.QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._ports = []

    def headerData(self, section: int, orientation: qtc.Qt.Orientation, role: int):
        if orientation == qtc.Qt.Orientation.Horizontal and role == qtc.Qt.DisplayRole:
            lookup = {0: 'Port', 1: 'Manufacturer', 2: 'Product'}
            return lookup[section]
        if orientation == qtc.Qt.Orientation.Horizontal and role == qtc.Qt.TextAlignmentRole:
            return qtc.Qt.AlignLeft

    def data(self, index, role):
        if role == qtc.Qt.DisplayRole:
            return self._ports[index.row()][index.column()]
        elif (
            role == qtc.Qt.ForegroundRole
            and self._ports[index.row()][2] != 'CP2102 USB to UART Bridge Controller'
        ):
            return qtg.QColor('grey')

    def rowCount(self, index):
        return len(self._ports)

    def columnCount(self, index):
        return 3

    def update(self, ports):
        self.beginResetModel()
        self._ports = ports
        self.endResetModel()
