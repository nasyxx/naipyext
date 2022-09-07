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
filename : ns.py
project  : naipyext
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Others
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.importstring import import_item


def load_ipython_extension(ip: InteractiveShell) -> None:
    """Load ipython extension."""
    namespaces = {
        "chain": "itertools.chain",
        "dir": "pdir",
        "httpx": "httpx",
        "nlg": "numpy.linalg",
        "np": "numpy",
        "os": "os",
        "pd": "pandas",
        "random": "random",
        "re": "re",
        "req": "httpx",
        "sys": "sys",
        "time": "time",
    }
    ns = ip.user_ns
    for k, v in namespaces.items():
        try:
            ns[k] = import_item(v)
        except ImportError:
            print(f"Cannot import {v}.")
