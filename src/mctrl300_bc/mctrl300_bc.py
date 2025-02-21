#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'

import logging

from .config import Config

log = logging.getLogger(__name__)


class MCTRL300BasicControl:
    def __init__(self, config: Config):
        log.info(f'MCTRL300BasicControl initialized. Config: {config}')
