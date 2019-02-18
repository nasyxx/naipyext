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
filename : be.py
project  : naipyext
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
import sys
from typing import Any, Tuple, Optional

# Other Packages
from IPython.core.interactiveshell import InteractiveShell

try:
    import better_exceptions as better_exceptions
except ImportError:
    print("pip install better_exceptions in need.")
    better_exceptions = None


def load_ipython_extension(ip: InteractiveShell) -> None:
    """Load extension."""
    old_show_tb = ip.showtraceback

    def exception_thunk(
        exc_tuple: Tuple[Any, ...] = tuple(),
        filename: Optional[str] = None,
        tb_offset: Optional[int] = None,
        exception_only: bool = False,
        **kwargs: Any
    ) -> None:
        "Formatted exception function."
        new_exc_tuple = exc_tuple or sys.exc_info()
        if not isinstance(new_exc_tuple[0], SyntaxError):
            return print(better_exceptions.format_exception(*new_exc_tuple))
        else:
            return old_show_tb(exc_tuple, filename, tb_offset, exception_only)

    if better_exceptions:
        ip.showtraceback = exception_thunk
