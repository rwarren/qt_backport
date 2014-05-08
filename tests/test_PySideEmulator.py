import unittest
import PyQt5 #required (until PySide gets Qt5, anyway)

class TestPySideProxy(unittest.TestCase):
    def setUp(self):
        pass
        
    def testTopLevelImoprt(self):
        import PySide
        self.assertIsNot(PySide, PyQt5)
    
    def testSubModuleImport(self):
        import PySide.QtCore
        self.assertIs(PySide.QtCore, PyQt5.QtCore)
    
    def testFromFooImportBar(self):
        from PySide import QtNetwork
        self.assertIs(QtNetwork, PyQt5.QtNetwork)
    
    def testQtGuiReassembly(self):
        import PySide.QtGui
        self.assertIs(PySide.QtGui.QLabel, PyQt5.QtGui.QLabel)
    
    def testFromFooImportStar(self):
        #This first bit duplicates testQtGuiReassembly, but proves a basis
        #import PySide.QtGui
        import PySide.QtGui
        self.assertIs(PySide.QtGui.QLabel, PyQt5.QtGui.QLabel)
        #Now test import * mechanics...
        # - We now know that PySide.QtGui.QLabel is working.  It should also
        #    be importable with import * mechanics...
        
        from PySide.QtGui import *
        try:
            obj = QLabel
        except NameError:
            self.fail("QLabel does not exist!  import * failed.")
        self.assertIs(QLabel, PyQt5.QtGui.QLabel)

if __name__ == "__main__":
    unittest.main()
