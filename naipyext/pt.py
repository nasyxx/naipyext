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
date     : Feb 18, 2019
email    : Nasy <nasyxx+python@gmail.com>
filename : pt.py
project  : naipyext
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Others
from IPython.core.interactiveshell import InteractiveShell

try:
    # Utils
    import rich
    from rich.pretty import install
except ImportError:
    print("Cannot find package 'rich'.")
    rich = None


try:
    # Math
    import numpy as np
except ImportError:
    print("Cannot find package 'numpy'.")
    np = None


def load_ipython_extension(ip: InteractiveShell) -> None:
    """Load extension."""
    if rich:
        install()
    if np:
        np.set_printoptions(threshold=50)
