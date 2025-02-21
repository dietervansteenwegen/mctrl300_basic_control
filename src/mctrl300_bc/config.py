#! /usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:expandtab:cuc:autoindent:ignorecase:colorcolumn=99


__author__ = 'Dieter Vansteenwegen'
__project__ = 'Novastar MCTRL300 Basic control'
__project_link__ = 'https://boxfish.be/posts/20230213-novastar-mctrl300-basic-control-software/'
import argparse
import logging
from typing import Union

PROGRAM_DESCRIPTION: str = 'Novastar MCTRL300 Basic control'

log = logging.getLogger(__name__)


def get_arguments() -> argparse.Namespace:
    """Parse  and evaluate the supplied arguments.

    Returns:
        argparse.Namespace: Namespace containing the parsed arguments
    """
    parser = HelpfullArgumentParser(
        add_help=True,
        description=PROGRAM_DESCRIPTION,
    )
    # parser.add_argument('arg', nargs='*', help='Positional argument')
    ## ADD REQUIRED ARG BELOW THIS GROUP. OPTIONAL ABOVE...

    # required_args = parser.add_argument_group('Required arguments')
    # required_args.add_argument(
    #     '--src_fn',
    #     help='Source CSV to process.',
    # )
    return parser.parse_args()


class HelpfullArgumentParser(argparse.ArgumentParser):
    """ArgumentParser subclass with improved error feedback.

    Provides better error message to user.
    """

    def error(self, msg):
        print('-' * 80)
        print(f'ERROR: {msg}\n')
        print('-' * 80)
        self.print_help()

        import sys

        sys.exit(-1)


class Config:
    def __init__(self):
        """Parses arguments and optionally configuration file for the application."""
        self.arguments: Union[None | argparse.Namespace] = {}
        self.config = None

    def get_config(self) -> None:
        """Get configuration from arguments and optionally a configuration file.

        If a config file is provided as one of the arguments, it will be read and stored
        in the config attribute.
        """
        self.arguments = get_arguments()

    def __str__(self) -> str:
        """String representation of the Config class."""
        return f'Config with arguments {self.arguments} and config {self.config} '
