import os
import platform
from ctypes import cdll


def _module_path():
    dirname = os.path.dirname
    return dirname(__file__)


def _load_clib(name):
    suffix = 'so' if platform.uname()[0] != 'Darwin' else 'dylib'
    filename = os.path.join(_module_path(), name + '.' + suffix)
    return cdll.LoadLibrary(filename)