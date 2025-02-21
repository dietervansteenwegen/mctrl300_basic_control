# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QCursor, QFont
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QListWidget,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSlider,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName('MainWindow')
        MainWindow.resize(494, 417)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setWindowTitle('Novastar MCTRL300 basic controller')
        self.menu_show_logs = QAction(MainWindow)
        self.menu_show_logs.setObjectName('menu_show_logs')
        # if QT_CONFIG(shortcut)
        self.menu_show_logs.setShortcut('Ctrl+Shift+L')
        # endif // QT_CONFIG(shortcut)
        self.menu_about = QAction(MainWindow)
        self.menu_about.setObjectName('menu_about')
        # if QT_CONFIG(shortcut)
        self.menu_about.setShortcut('Ctrl+Shift+A')
        # endif // QT_CONFIG(shortcut)
        self.brightness_1_pct = QAction(MainWindow)
        self.brightness_1_pct.setObjectName('brightness_1_pct')
        self.brightness_5_pct = QAction(MainWindow)
        self.brightness_5_pct.setObjectName('brightness_5_pct')
        self.brightness_50_pct = QAction(MainWindow)
        self.brightness_50_pct.setObjectName('brightness_50_pct')
        self.brightness_100_pct = QAction(MainWindow)
        self.brightness_100_pct.setObjectName('brightness_100_pct')
        self.pattern_live = QAction(MainWindow)
        self.pattern_live.setObjectName('pattern_live')
        self.pattern_red = QAction(MainWindow)
        self.pattern_red.setObjectName('pattern_red')
        self.pattern_green = QAction(MainWindow)
        self.pattern_green.setObjectName('pattern_green')
        self.pattern_blue = QAction(MainWindow)
        self.pattern_blue.setObjectName('pattern_blue')
        self.pattern_white = QAction(MainWindow)
        self.pattern_white.setObjectName('pattern_white')
        self.pattern_cycle_colors = QAction(MainWindow)
        self.pattern_cycle_colors.setObjectName('pattern_cycle_colors')
        self.pattern_slash = QAction(MainWindow)
        self.pattern_slash.setObjectName('pattern_slash')
        self.pattern_black = QAction(MainWindow)
        self.pattern_black.setObjectName('pattern_black')
        self.pattern_black.setEnabled(False)
        self.pattern_freeze = QAction(MainWindow)
        self.pattern_freeze.setObjectName('pattern_freeze')
        self.pattern_freeze.setEnabled(False)
        self.brightness_up = QAction(MainWindow)
        self.brightness_up.setObjectName('brightness_up')
        self.brightness_down = QAction(MainWindow)
        self.brightness_down.setObjectName('brightness_down')
        self.pattern_next = QAction(MainWindow)
        self.pattern_next.setObjectName('pattern_next')
        self.pattern_previous = QAction(MainWindow)
        self.pattern_previous.setObjectName('pattern_previous')
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName('action_Exit')
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.v_layout_port = QVBoxLayout()
        self.v_layout_port.setObjectName('v_layout_port')
        self.v_layout_port.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName('label_2')
        font = QFont()
        font.setFamilies(['DejaVu Sans'])
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setText('Select serial port to controller:')

        self.v_layout_port.addWidget(self.label_2)

        self.lst_serial_ports = QListWidget(self.centralwidget)
        self.lst_serial_ports.setObjectName('lst_serial_ports')

        self.v_layout_port.addWidget(self.lst_serial_ports)

        self.btn_serial_open = QPushButton(self.centralwidget)
        self.btn_serial_open.setObjectName('btn_serial_open')
        self.btn_serial_open.setText('Open selected port')
        self.btn_serial_open.setCheckable(True)

        self.v_layout_port.addWidget(self.btn_serial_open)

        self.btn_serial_refresh = QPushButton(self.centralwidget)
        self.btn_serial_refresh.setObjectName('btn_serial_refresh')
        self.btn_serial_refresh.setEnabled(False)

        self.v_layout_port.addWidget(self.btn_serial_refresh)

        self.lbl_serial_status = QLabel(self.centralwidget)
        self.lbl_serial_status.setObjectName('lbl_serial_status')
        self.lbl_serial_status.setFrameShape(QFrame.Shape.Box)
        self.lbl_serial_status.setText('No port')
        self.lbl_serial_status.setTextFormat(Qt.TextFormat.PlainText)
        self.lbl_serial_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_port.addWidget(self.lbl_serial_status)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName('line_3')
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.v_layout_port.addWidget(self.line_3)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName('label_7')
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_7.setText('Screen connected to output:')

        self.v_layout_port.addWidget(self.label_7)

        self.cmb_output = QComboBox(self.centralwidget)
        self.cmb_output.setObjectName('cmb_output')
        self.cmb_output.setMinimumSize(QSize(0, 20))
        self.cmb_output.setToolTipDuration(5)
        self.cmb_output.setEditable(False)
        self.cmb_output.setMaxVisibleItems(2)

        self.v_layout_port.addWidget(self.cmb_output)

        self.horizontalLayout.addLayout(self.v_layout_port)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName('line')
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName('line_2')
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.h_layout_settings = QHBoxLayout()
        self.h_layout_settings.setObjectName('h_layout_settings')
        self.HLayoutSettings_dummy = QHBoxLayout()
        self.HLayoutSettings_dummy.setObjectName('HLayoutSettings_dummy')
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.lbl_brightness = QLabel(self.centralwidget)
        self.lbl_brightness.setObjectName('lbl_brightness')
        self.lbl_brightness.setMaximumSize(QSize(16777215, 20))
        self.lbl_brightness.setBaseSize(QSize(0, 20))
        font2 = QFont()
        font2.setBold(True)
        self.lbl_brightness.setFont(font2)
        self.lbl_brightness.setText('Brightness:')

        self.verticalLayout_3.addWidget(self.lbl_brightness)

        self.sldr_brightness = QSlider(self.centralwidget)
        self.sldr_brightness.setObjectName('sldr_brightness')
        self.sldr_brightness.setEnabled(False)
        self.sldr_brightness.setMinimumSize(QSize(70, 0))
        self.sldr_brightness.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
        self.sldr_brightness.setAutoFillBackground(False)
        self.sldr_brightness.setMaximum(255)
        self.sldr_brightness.setValue(8)
        self.sldr_brightness.setSliderPosition(8)
        self.sldr_brightness.setOrientation(Qt.Orientation.Vertical)
        self.sldr_brightness.setInvertedAppearance(False)
        self.sldr_brightness.setTickPosition(QSlider.TickPosition.NoTicks)
        self.sldr_brightness.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.sldr_brightness)

        self.lbl_brightness_value = QLabel(self.centralwidget)
        self.lbl_brightness_value.setObjectName('lbl_brightness_value')
        self.lbl_brightness_value.setMaximumSize(QSize(16777215, 20))
        self.lbl_brightness_value.setBaseSize(QSize(0, 20))
        self.lbl_brightness_value.setText('Unknown')
        self.lbl_brightness_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_brightness_value)

        self.HLayoutSettings_dummy.addLayout(self.verticalLayout_3)

        self.grp_patterns = QGroupBox(self.centralwidget)
        self.grp_patterns.setObjectName('grp_patterns')
        self.grp_patterns.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_patterns.sizePolicy().hasHeightForWidth())
        self.grp_patterns.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setBold(False)
        self.grp_patterns.setFont(font3)
        self.grp_patterns.setStyleSheet('border: none')
        self.grp_patterns.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.grp_patterns.setFlat(True)
        self.layoutWidget = QWidget(self.grp_patterns)
        self.layoutWidget.setObjectName('layoutWidget')
        self.layoutWidget.setGeometry(QRect(0, 20, 112, 260))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.btn_normal = QRadioButton(self.layoutWidget)
        self.btn_normal.setObjectName('btn_normal')
        self.btn_normal.setText('Live (input)')

        self.verticalLayout.addWidget(self.btn_normal)

        self.btn_red = QRadioButton(self.layoutWidget)
        self.btn_red.setObjectName('btn_red')
        self.btn_red.setText('Red')

        self.verticalLayout.addWidget(self.btn_red)

        self.btn_green = QRadioButton(self.layoutWidget)
        self.btn_green.setObjectName('btn_green')
        self.btn_green.setText('Green')

        self.verticalLayout.addWidget(self.btn_green)

        self.btn_blue = QRadioButton(self.layoutWidget)
        self.btn_blue.setObjectName('btn_blue')
        self.btn_blue.setText('Blue')

        self.verticalLayout.addWidget(self.btn_blue)

        self.btn_white = QRadioButton(self.layoutWidget)
        self.btn_white.setObjectName('btn_white')
        self.btn_white.setText('White')

        self.verticalLayout.addWidget(self.btn_white)

        self.btn_cycle_colors = QRadioButton(self.layoutWidget)
        self.btn_cycle_colors.setObjectName('btn_cycle_colors')
        self.btn_cycle_colors.setText('Cycle colors')

        self.verticalLayout.addWidget(self.btn_cycle_colors)

        self.btn_slash = QRadioButton(self.layoutWidget)
        self.btn_slash.setObjectName('btn_slash')
        self.btn_slash.setText('Slash')

        self.verticalLayout.addWidget(self.btn_slash)

        self.btn_blackout = QRadioButton(self.layoutWidget)
        self.btn_blackout.setObjectName('btn_blackout')
        self.btn_blackout.setEnabled(False)
        self.btn_blackout.setText('Blackout')

        self.verticalLayout.addWidget(self.btn_blackout)

        self.btn_freeze = QRadioButton(self.layoutWidget)
        self.btn_freeze.setObjectName('btn_freeze')
        self.btn_freeze.setEnabled(False)
        self.btn_freeze.setText('Freeze')

        self.verticalLayout.addWidget(self.btn_freeze)

        self.HLayoutSettings_dummy.addWidget(self.grp_patterns)

        self.h_layout_settings.addLayout(self.HLayoutSettings_dummy)

        self.horizontalLayout.addLayout(self.h_layout_settings)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName('menubar')
        self.menubar.setGeometry(QRect(0, 0, 494, 23))
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName('menu_help')
        self.menuBrightness = QMenu(self.menubar)
        self.menuBrightness.setObjectName('menuBrightness')
        self.menuBrightness.setEnabled(True)
        self.menuPattern = QMenu(self.menubar)
        self.menuPattern.setObjectName('menuPattern')
        self.menuPattern.setEnabled(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName('menuFile')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lst_serial_ports, self.btn_serial_open)
        QWidget.setTabOrder(self.btn_serial_open, self.cmb_output)
        QWidget.setTabOrder(self.cmb_output, self.btn_serial_refresh)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPattern.menuAction())
        self.menubar.addAction(self.menuBrightness.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.menu_show_logs)
        self.menu_help.addAction(self.menu_about)
        self.menuBrightness.addAction(self.brightness_1_pct)
        self.menuBrightness.addAction(self.brightness_5_pct)
        self.menuBrightness.addAction(self.brightness_50_pct)
        self.menuBrightness.addAction(self.brightness_100_pct)
        self.menuBrightness.addSeparator()
        self.menuBrightness.addAction(self.brightness_up)
        self.menuBrightness.addAction(self.brightness_down)
        self.menuPattern.addAction(self.pattern_live)
        self.menuPattern.addAction(self.pattern_red)
        self.menuPattern.addAction(self.pattern_green)
        self.menuPattern.addAction(self.pattern_blue)
        self.menuPattern.addAction(self.pattern_white)
        self.menuPattern.addAction(self.pattern_cycle_colors)
        self.menuPattern.addAction(self.pattern_slash)
        self.menuPattern.addAction(self.pattern_black)
        self.menuPattern.addAction(self.pattern_freeze)
        self.menuPattern.addSeparator()
        self.menuPattern.addAction(self.pattern_next)
        self.menuPattern.addAction(self.pattern_previous)
        self.menuFile.addAction(self.action_Exit)

        self.retranslateUi(MainWindow)

        self.cmb_output.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.menu_show_logs.setText(QCoreApplication.translate('MainWindow', 'Show &logs', None))
        self.menu_about.setText(QCoreApplication.translate('MainWindow', '&About', None))
        self.brightness_1_pct.setText(QCoreApplication.translate('MainWindow', '1%', None))
        # if QT_CONFIG(shortcut)
        self.brightness_1_pct.setShortcut(QCoreApplication.translate('MainWindow', '1', None))
        # endif // QT_CONFIG(shortcut)
        self.brightness_5_pct.setText(QCoreApplication.translate('MainWindow', '5%', None))
        # if QT_CONFIG(shortcut)
        self.brightness_5_pct.setShortcut(QCoreApplication.translate('MainWindow', '2', None))
        # endif // QT_CONFIG(shortcut)
        self.brightness_50_pct.setText(QCoreApplication.translate('MainWindow', '50%', None))
        # if QT_CONFIG(shortcut)
        self.brightness_50_pct.setShortcut(QCoreApplication.translate('MainWindow', '5', None))
        # endif // QT_CONFIG(shortcut)
        self.brightness_100_pct.setText(QCoreApplication.translate('MainWindow', '100%', None))
        # if QT_CONFIG(shortcut)
        self.brightness_100_pct.setShortcut(QCoreApplication.translate('MainWindow', '0', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_live.setText(QCoreApplication.translate('MainWindow', 'Live', None))
        # if QT_CONFIG(shortcut)
        self.pattern_live.setShortcut(QCoreApplication.translate('MainWindow', 'N', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_red.setText(QCoreApplication.translate('MainWindow', 'Red', None))
        # if QT_CONFIG(shortcut)
        self.pattern_red.setShortcut(QCoreApplication.translate('MainWindow', 'R', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_green.setText(QCoreApplication.translate('MainWindow', 'Green', None))
        # if QT_CONFIG(shortcut)
        self.pattern_green.setShortcut(QCoreApplication.translate('MainWindow', 'G', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_blue.setText(QCoreApplication.translate('MainWindow', 'Blue', None))
        # if QT_CONFIG(shortcut)
        self.pattern_blue.setShortcut(QCoreApplication.translate('MainWindow', 'B', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_white.setText(QCoreApplication.translate('MainWindow', 'White', None))
        # if QT_CONFIG(shortcut)
        self.pattern_white.setShortcut(QCoreApplication.translate('MainWindow', 'W', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_cycle_colors.setText(
            QCoreApplication.translate('MainWindow', 'Cycle colors', None)
        )
        # if QT_CONFIG(shortcut)
        self.pattern_cycle_colors.setShortcut(QCoreApplication.translate('MainWindow', 'C', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_slash.setText(QCoreApplication.translate('MainWindow', 'Slash', None))
        # if QT_CONFIG(shortcut)
        self.pattern_slash.setShortcut(QCoreApplication.translate('MainWindow', 'S', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_black.setText(QCoreApplication.translate('MainWindow', 'Blackout', None))
        self.pattern_freeze.setText(QCoreApplication.translate('MainWindow', 'Freeze', None))
        self.brightness_up.setText(QCoreApplication.translate('MainWindow', 'Brightness up', None))
        # if QT_CONFIG(shortcut)
        self.brightness_up.setShortcut(QCoreApplication.translate('MainWindow', 'Up', None))
        # endif // QT_CONFIG(shortcut)
        self.brightness_down.setText(
            QCoreApplication.translate('MainWindow', 'Brightness down', None)
        )
        # if QT_CONFIG(shortcut)
        self.brightness_down.setShortcut(QCoreApplication.translate('MainWindow', 'Down', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_next.setText(QCoreApplication.translate('MainWindow', 'Next pattern', None))
        # if QT_CONFIG(shortcut)
        self.pattern_next.setShortcut(QCoreApplication.translate('MainWindow', 'Right', None))
        # endif // QT_CONFIG(shortcut)
        self.pattern_previous.setText(
            QCoreApplication.translate('MainWindow', 'Previous pattern', None)
        )
        # if QT_CONFIG(shortcut)
        self.pattern_previous.setShortcut(QCoreApplication.translate('MainWindow', 'Left', None))
        # endif // QT_CONFIG(shortcut)
        self.action_Exit.setText(QCoreApplication.translate('MainWindow', '&Exit', None))
        self.btn_serial_refresh.setText(
            QCoreApplication.translate('MainWindow', 'Refresh ports list', None)
        )
        # if QT_CONFIG(tooltip)
        self.cmb_output.setToolTip(
            QCoreApplication.translate(
                'MainWindow', 'Select which controller output is connected to the screen', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.cmb_output.setCurrentText('')
        self.grp_patterns.setTitle(QCoreApplication.translate('MainWindow', 'Pattern/Label:', None))
        self.menu_help.setTitle(QCoreApplication.translate('MainWindow', '&Help', None))
        self.menuBrightness.setTitle(QCoreApplication.translate('MainWindow', 'Brightness', None))
        self.menuPattern.setTitle(QCoreApplication.translate('MainWindow', 'Pattern', None))
        self.menuFile.setTitle(QCoreApplication.translate('MainWindow', 'File', None))
        pass

    # retranslateUi
