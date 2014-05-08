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

#The starting list of all PyQt4 modules was obtained from here:
#       http://pyqt.sourceforge.net/Docs/PyQt4/modules.html
# - modules unavailable in PyQt5 have been commented out (for now?)
_all_PyQt4_modules = (
    'QtCore', 'QtDBus', 'QtDesigner', 'QtGui', 'QtHelp', 'QtMultimedia',
    'QtNetwork', 'QtOpenGL', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit',
    'QtXmlPatterns', "uic",
    #'QAxContainer', 'QtAssistant', 'QtDeclarative', 'QtScript',
    #'QtScriptTools', 'QtXml', 'phonon',
)

_this_module = sys.modules[__name__]
for _module_name in _all_PyQt4_modules:
    _qt4_module_name = "PyQt4." + _module_name
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

#Set the qt_backport constants that depended on us importing...
_qt_backport.CURRENT_EMULATOR = _qt_backport.PYQT4

#clean up...
# - this makes all the _ prefixes a bit unnecessary, but whatever.
sys.path.remove(_common_path)
del _common_path
del _qt5_backport
del _all_PyQt4_modules
del _this_module
del _module_name
del _qt4_module_name
del _qt5_module_name
del _qt5_module
del _qt_backport
