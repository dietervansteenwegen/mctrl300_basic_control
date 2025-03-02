#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99

__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'

import logging
import sys
import traceback

from .config import Config
from .gui import run
from .log import add_rotating_file, setup_logger

"""Main entry point for `python -m mctrl300_bc`."""


def _setup_log():
    """Set up logging."""
    log = setup_logger()
    add_rotating_file(log)
    return log


def excepthook(exc_type, exc_value, exc_tb) -> None:
    log = logging.getLogger(__name__)
    tabbed_msg: list[str] = [
        i.replace('\n', '\t').replace('  ', ' ')
        for i in traceback.format_exception(exc_type, exc_value, exc_tb)
    ]
    for msg in tabbed_msg:
        log.error(msg)


sys.excepthook = excepthook

log = _setup_log()
try:
    config = Config()
    config.get_config()
    log.debug(f'Starting Novastar MCTRL300 Basic control with config {config}')
    sys.exit(run(config))
except KeyboardInterrupt:
    sys.exit(1)
