#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99


__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'

from enum import Enum


class Pattern(Enum):
    PATTERN_NORMAL = 1
    PATTERN_RED = 2
    PATTERN_GREEN = 3
    PATTERN_BLUE = 4
    PATTERN_WHITE = 5
    PATTERN_HORIZONTAL = 6
    PATTERN_VERTICAL = 7
    PATTERN_SLASH = 8
    PATTERN_GRAYSCALE = 9


class Registers:
    REG_TEST_PATTERN = 0x02000101
    REG_BRIGHTNESS_OVERALL = 0x02000001
