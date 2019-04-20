#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Apr 20, 2019
email    : Nasy <nasyxx+python@gmail.com>
filename : autotime.py
project  : naipyext
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
import time

# Other Packages
from pendulum import duration as dt
from IPython.core.interactiveshell import InteractiveShell


class Timer:
    """A simply timer.

    Since the old one autotime that cannot easily install from pypi
    annoyed me,  I write my own one.
    """

    def __init__(self) -> None:
        """Initial timer."""
        self.perf = 0.0
        self.cput = 0.0

    def start(self) -> None:
        """Start timer."""
        self.perf = time.perf_counter()
        self.cput = time.process_time()

    def stop(self) -> None:
        """Stop timer."""
        perf = time.perf_counter() - self.perf
        cput = time.process_time() - self.cput
        if perf and cput and (perf > 1e-2 or cput > 1e-2):
            print("Performance:", dt(seconds=perf).in_words())
            print("Process:", dt(seconds=cput).in_words())


timer = Timer()


def load_ipython_extension(ip: InteractiveShell) -> None:
    "Load timer."
    ip.events.register("pre_run_cell", timer.start)
    ip.events.register("post_run_cell", timer.stop)


def unload_ipython_extension(ip: InteractiveShell) -> None:
    "Unload timer."
    ip.events.unregister("pre_run_cell", timer.start)
    ip.events.unregister("post_run_cell", timer.stop)
