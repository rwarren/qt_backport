import unittest
import PyQt5 #required (until PySide gets Qt5, anyway)

class TestPySideProxy(unittest.TestCase):
    def setUp(self):
        pass
        
    def testTopLevelImport(self):
        import PySide
        self.assertIsNot(PySide, PyQt5)
    
    def testSubModuleImport(self):
        import PySide.QtCore
        self.assert_(hasattr(PySide.QtCore, "QPointF"))
    
    def testFromFooImportBar(self):
        from PySide import QtNetwork
        self.assert_(hasattr(QtNetwork, "QDnsLookup"))
    
    def testQtGuiReassembly(self):
        import PySide.QtGui
        self.assert_(hasattr(PySide.QtGui, "QLabel")) #from QtWidgets
        self.assert_(hasattr(PySide.QtGui, "QColor")) #from QtGui proper
    
    def testFromFooImportStar(self):
        #This first bit duplicates testQtGuiReassembly, but proves a basis
        #import PySide.QtGui
        import PySide.QtGui
        self.assert_(hasattr(PySide.QtGui, "QLabel"))
        #Now test import * mechanics...
        # - We now know that PySide.QtGui.QLabel is working.  It should also
        #    be importable with import * mechanics...
        
        from PySide.QtGui import *
        try:
            obj = QLabel
        except NameError:
            self.fail("QLabel does not exist!  import * failed.")
        self.assertIs(QLabel, PySide.QtGui.QLabel)
    
    def testIsolation(self):
        import PySide.QtGui
        import PyQt5.QtGui
        
        c4_cls = PySide.QtGui.QColor
        c5_cls = PyQt5.QtGui.QColor
        
        #qt4 class could not be the same as qt5 (but should be a subclass)...
        self.assertIsNot(c4_cls, c5_cls)
        self.assert_(issubclass(c4_cls, c5_cls))
        
        #unmodified functionality should be identical... 
        c4 = c4_cls(100, 100, 100)
        c5 = c5_cls(100, 100, 100)
        self.assertEqual(c4.getRgb(), c5.getRgb())
        
        #modifying the core qt4 api implementation should only affect the
        #qt4 emulator and leave qt5 alone...
        c4_cls.getRgb = lambda self: "foo"
        self.assertEqual(c4.getRgb(), "foo")
        self.assertEqual(c5.getRgb(), (100, 100, 100, 255))

if __name__ == "__main__":
    unittest.main()
