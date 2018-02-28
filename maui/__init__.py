# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'christoph.statz <at> tu-dresden.de'
__version__ = '0.9.20170310'

from maui.backend import context
from maui.backend import arguments

def get_logger(name=__name__):

    import logging
    from maui.backend import loglevel
    from maui.backend import handler

    logger = logging.getLogger(name)
    logger.setLevel(loglevel)
    logger.addHandler(handler)
    logger.propagate = False

    return logger
