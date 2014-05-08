import os
from PyQt5 import QtCore

THIS_DIR = os.path.dirname(__file__)

__version__ = open(os.path.join(THIS_DIR, "../VERSION"), "r").read().strip()

PYQT4 = "PyQt4"
PYQT5 = "PyQt5"
PYSIDE = "PySide"

EMULATORS = (PYQT4, PYSIDE)
QT_WRAPPERS = (PYQT5, ) #Currently the only Qt5 wrapper available!

#Values below are changed on import of either PyQt4 or PySide
CURRENT_EMULATOR = None #not imported yet

#Values below depend on the Qt wrapper and Qt lib in use..
# - having wrapper options here is a bit of a farce right now since PyQt5 is the
#    only option for Qt5, but eventually there may be more options and our API
#    should be ready for that
CURRENT_QT_WRAPPER = PYQT5  #must be in QT_WRAPPERS
CURRENT_QT_WRAPPER_VERSION_TUPLE = tuple(QtCore.PYQT_VERSION_STR.split("."))
CURRENT_QT_WRAPPER_VERSION_STR = \
    "%s v%s" % (CURRENT_QT_WRAPPER, ".".join(CURRENT_QT_WRAPPER_VERSION_TUPLE))
CURRENT_QT_VERSION_TUPLE = tuple(QtCore.QT_VERSION_STR.split("."))
CURRENT_QT_VERSION_STR = ".".join(CURRENT_QT_VERSION_TUPLE)

#cleanup...
del THIS_DIR
del os
