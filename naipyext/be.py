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
import types
from typing import Any, Tuple, Optional

# Other Packages
from IPython.core.interactiveshell import InteractiveShell

try:
    import better_exceptions
except ImportError:
    print("pip install better_exceptions in need.")
    better_exceptions = None


def load_ipython_extension(ip: InteractiveShell) -> None:
    """Load extension."""
    old_show_tb = ip.showtraceback

    def exception_thunk(
        self,
        exc_tuple: Tuple[Any, ...] = tuple(),
        filename: Optional[str] = None,
        tb_offset: Optional[int] = None,
        exception_only: bool = False,
        **kwargs: Any
    ):
        notuple = False
        if exc_tuple is None:
            notuple = True
            exc_tuple = sys.exc_info()
        etype, value, tb = self._get_exc_info(exc_tuple)
        use_better = not any(
            [filename, tb_offset, exception_only, issubclass(etype, SyntaxError)]
        )
        if use_better:
            return better_exceptions.excepthook(etype, value, tb)

        return old_show_tb(
            None if notuple else exc_tuple,
            filename,
            tb_offset,
            exception_only,
            **kwargs
        )

    if better_exceptions:
        ip.showtraceback = types.MethodType(exception_thunk, ip)
