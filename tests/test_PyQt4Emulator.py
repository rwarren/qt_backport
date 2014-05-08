import unittest
import PyQt5 #required (until PySide gets Qt5, anyway)

class TestPyQt4Proxy(unittest.TestCase):
    def setUp(self):
        pass
        
    def testTopLevelImoprt(self):
        import PyQt4
        self.assertIsNot(PyQt4, PyQt5)
    
    def testSubModuleImport(self):
        import PyQt4.QtCore
        self.assertIs(PyQt4.QtCore, PyQt5.QtCore)
    
    def testFromFooImportBar(self):
        from PyQt4 import QtNetwork
        self.assertIs(QtNetwork, PyQt5.QtNetwork)
    
    def testQtGuiReassembly(self):
        import PyQt4.QtGui
        self.assertIs(PyQt4.QtGui.QLabel, PyQt5.QtGui.QLabel)
    
    def testFromFooImportStar(self):
        #This first bit duplicates testQtGuiReassembly, but proves a basis
        #import PyQt4.QtGui
        import PyQt4.QtGui
        self.assertIs(PyQt4.QtGui.QLabel, PyQt5.QtGui.QLabel)
        #Now test import * mechanics...
        # - We now know that PyQt4.QtGui.QLabel is working.  It should also
        #    be importable with import * mechanics...
        
        from PyQt4.QtGui import *
        try:
            obj = QLabel
        except NameError:
            self.fail("QLabel does not exist!  import * failed.")
        self.assertIs(QLabel, PyQt5.QtGui.QLabel)

if __name__ == "__main__":
    unittest.main()
