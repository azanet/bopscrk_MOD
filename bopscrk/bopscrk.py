#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ORIGINAL: https://github.com/r3nt0n/bopscrk
# AZANET MOD: https://github.com/r3nt0n/azanet/FORK-bopscrk_MOD
# bopscrk - init script


name = 'bopscrk.py'
desc = 'Generate smart and powerful wordlists'
__version__ = '2.4 - MOD'
__author__ = '"Mod by Azanet" -- Original Author: r3nt0n'
__status__ = 'Development'


def start():
    try:
        from .modules import main
    except ImportError:
        # catching except when running python3 bopscrk.py
        # (sketchy, need some refactor)
        from modules import main

    main.run(name, __version__)


if __name__ == '__main__':
    start()
