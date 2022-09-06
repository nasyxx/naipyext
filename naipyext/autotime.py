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
import sys, time

# Others
from IPython.core.interactiveshell import InteractiveShell

K = 1000
G = K * K * K
M = 60
H = M * M
D = H * 24
Y = 365
YD = D * Y


def duration(ns: int) -> str:
    """Calculate human readable time string."""
    return ", ".join(
        map(
            lambda nu: f"{nu[0]}{nu[1]}",
            filter(
                lambda nu: nu[0] > 0,
                zip(
                    map(  # noqa: WPS317
                        lambda d, m: (ns // d) % m,
                        (YD * G, D * G, H * G, M * G, G, K * K, K, 1),
                        (sys.maxsize, Y, 24, 60, 60, K, K, K),
                    ),
                    ("y", "d", "h", "m", "s", "ms", "µs", "ns"),
                ),
            ),
        )
    )


class Timer:
    """A simply timer.

    Since the old one autotime that cannot easily install from pypi
    annoyed me,  I write my own one.
    """

    def __init__(self) -> None:
        """Initialize timer."""
        self.perf = 0
        self.cput = 0
        self.print = True

    def start(self) -> None:
        """Start timer."""
        self.perf = time.perf_counter_ns()
        self.cput = time.process_time_ns()

    def stop(self) -> None:
        """Stop timer."""
        cput, perf = (
            time.process_time_ns() - self.cput,
            time.perf_counter_ns() - self.perf,
        )
        if self.print and perf:
            print("Performance:", duration(perf))
        if self.print and cput:
            print("Process:", duration(cput))


timer = Timer()


def load_ipython_extension(ip: InteractiveShell) -> None:
    """Load timer."""
    timer.print = True
    ip.events.register("pre_run_cell", timer.start)
    ip.events.register("post_run_cell", timer.stop)


def unload_ipython_extension(ip: InteractiveShell) -> None:
    """Unload timer."""
    timer.print = False
    ip.events.unregister("pre_run_cell", timer.start)
    ip.events.unregister("post_run_cell", timer.stop)
