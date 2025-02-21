#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99


__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'


from . import novastar_mctrl300


class ScreenStatus:
    def __init__(self):
        self.screen_connected: bool = False
        self.screen_current_pattern: novastar_mctrl300.Pattern = 0
