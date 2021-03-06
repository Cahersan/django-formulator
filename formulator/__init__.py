# -*- coding: utf-8 -*-
VERSION = (0, 2, 0, 'dev')
__version__ = '.'.join((str(each) for each in VERSION[:4]))


def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:4]))
