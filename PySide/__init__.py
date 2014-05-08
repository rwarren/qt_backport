import qt_backport as _qt_backport
if _qt_backport.CURRENT_EMULATOR is not None:
    raise ImportError("qt_backport emulator already running: '%s'" % \
                      _qt_backport.CURRENT_EMULATOR)

try:
    import PyQt5
except ImportError:
    raise ImportError("qt_backport emulation currently requires PyQt5")

import sys
import os
_common_path = os.path.join(os.path.dirname(__file__), "../common")
_common_path = os.path.abspath(_common_path)
sys.path.append(_common_path)

import qt5_backport as _qt5_backport #from shared dir
_qt5_backport.reassemble_QtGui()
_qt5_backport.patch_api()

#All PySide modules taken from list here:
#   https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html
#modules unavailable in PyQt5 have been commented out.
_all_PySide_modules = (
    "QtCore", "QtGui", "QtHelp", "QtMultimedia", "QtNetwork",
    "QtOpenGL", "QtSql", "QtSvg", "QtUiTools",
    "QtWebkit",
    #"QtDeclarative", "QtScript", "QtScriptTools", "QtXml", "Phonon",
)
_this_module = sys.modules[__name__]
for _module_name in _all_PySide_modules:
    _qt4_module_name = "PySide." + _module_name
    _qt5_module_name = "PyQt5." + _module_name
    #Dynamically import the required modules...
    # - the odd fromlist is because without it the __import__ actually
    #    returns the top level module.  See here for a full explanation:
    #       http://stackoverflow.com/questions/2724260
    try:
        _qt5_module = __import__(_qt5_module_name, fromlist=["foo", ])
        #make the module available as PyQt4.<module_name>
        setattr(_this_module, _module_name, _qt5_module)
        #also make it directly importable (eg: import PyQt4.QtGui)...
        sys.modules[_qt4_module_name] = _qt5_module
    except ImportError:
        #Not all modules will necessarily be available (eg: QtOpenGL)
        pass

QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot

#Set the qt_backport constants that depended on us importing...
_qt_backport.CURRENT_EMULATOR = _qt_backport.PYSIDE

#clean up...
# - this makes all the _ prefixes a bit unnecessary, but whatever.
sys.path.remove(_common_path)
del _common_path
del _qt5_backport
del _all_PySide_modules
del _this_module
del _module_name
del _qt4_module_name
del _qt5_module_name
del _qt5_module
del _qt_backport
