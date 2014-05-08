``qt5_backport``
================

``qt5_backport`` is for making old python code based on Qt4 work with Qt5.

More specifically (and currently), if you have PyQt5 installed and
functional, but want to work with older PyQt4 or PySide code without having
to do any conversion work, this package is for you!

Installation
============

1. Uninstall any existing Qt4 wrapper (PyQt4 or PySide) if you have one.
2. `Install PyQt5`_
3. ``pip install ``qt5_backport````

.. _`Install PyQt5`: http://pyqt.sourceforge.net/Docs/PyQt5/installation.html

Usage
=====

``qt5_backport`` automatically makes both 'PyQt4' and 'PySide' packages
available that will function like the old Qt4 versions, but will actually be
backed by PyQt5.

ie: your old code like this will just work as-is: ::

    import PyQt4
    from PyQt4 import QtCore
    from PyQt4.QtGui import *  #<-- this is supported, but yuck

or ::

    import PySide
    from PySide import QtCore
    from PySide.QtGui import *  #<-- this is supported, but yuck


When to use ``qt5_backport``?
=============================

This package is particularly useful when you have installed a modern Qt5
wrapper (currently only PyQt5) and are trying to learn Qt using legacy code
examples you find on the web.

``qt5_backport`` is not primarily intended as a method for porting your
applications from Qt4 to Qt5 (you are better off converting if you can), but
it does do a good job of this and can definitely help get you started.


Why is ``qt5_backport`` needed at all?
======================================

When Qt4 was updated to Qt5 there was a *major* reorganization done to the
class organization.  In addition, there have been many other API changes.

One of the most significant changes was that a huge number of classes that
used to be contained within 'QtGui' were dispersed out to various other
locations instead. eg: *All* of the widgets were moved out of QtGui and into
a new module called QtWidgets. Although the new locations make much more
sense, it broke a lot of old code. ``qt5_backport`` is a hack to make old
code work as-is.

There have been many more API changes in the Qt4.x to Qt5.2 transition (Qt5.2
is current the time of writing this). ``qt5_backport`` deals with many of
these changes, but all of them may not be captured (yet). A simple example of
such a change (that ``qt5_backport`` handles) is that QColor.dark() was
removed and replaced with QColor.darker() in Qt4.3.

Note that, although the backport generally works quite well, there may be
additional changes you need to make to to your old code for it to work. These
changes depend on the vintage of your old code. For example, old style
signal/slot connections are not currently supported.

NOTE: At the current time, the only Qt wrapper for python that works with Qt5
is PyQt5. In future this may change (eg: when PySide upgrades to use Qt5).

How does it work?
=================

``qt_backport`` wraps Qt using PyQt5 (currently the only python wrapper for
Qt5), but provides an emulation layer that emulates both the PySide and the
PyQt4 APIs.  Installing ``qt_backport`` automatically makes the PySide and
PyQt4 emulators available for import.

This is easier to see visually:

::

                       +-----------------------------------+       
                       |                                   |       
                       | Existing Python code that expects |       
                       |     the PyQt4 or PySide API       |       
                       |                                   |       
                       +-------+------------------+--------+       
                               |                  |                
                              OLD          <with qt_backport>      
                              WAY                 |                
                               |            +-----+-------+        
                               |            |             |        
    qt_backport                |            |  PySide or  |        
    Emulation layer:           |            |    PyQt4    |        
                               |            |             |        
                               |            +-----+-------+        
                               |                  |                
                      +--------+--------+   +-----+-------+        
                      |                 |   |             |        
    Wrapper layer:    | PySide or PyQt4 |   |   PyQt5     |        
                      |                 |   |             |        
                      +--------+--------+   +-----+-------+        
                               |                  |                
                          +----+-----+        +---+-----+          
                          |          |        |         |          
    Qt library layer:     |   Qt4    |        |   Qt5   |          
                          |          |        |         |          
                          +----------+        +---------+     

To do:
======
- support old-style connections (ie: ``connect(app, SIGNAL(), app, SLOT()``)
- support more known api changes
    - API change coverage is currently not 100%, being mostly driven by demand for certain classes/methods. Coverage is currently quite good, though.
    - other potential changes are covered here: http://qt-project.org/doc/qt-5/portingguide.html
- unit tests for the zillion api patches

License
=======
MIT.  See LICENSE file.