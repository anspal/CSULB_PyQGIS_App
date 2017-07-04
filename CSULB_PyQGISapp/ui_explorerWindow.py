# coding=utf-8
from PyQt4 import QtGui, QtCore
import resources

class Ui_ExplorerWindow(object):
	def setupUi(self, window):
		window.setWindowTitle('California State University Long Beach Explorer')
		
		self.centralWidget = QtGui.QWidget(window)
		self.centralWidget.setMinimumSize(800, 500)
		window.setCentralWidget(self.centralWidget)
		
		self.menubar = window.menuBar()
		self.fileMenu = self.menubar.addMenu('File')
		self.mapMenu = self.menubar.addMenu('Map')
		self.editMenu = self.menubar.addMenu('Edit')
		self.toolsMenu = self.menubar.addMenu('Tools')
		
		self.toolBar = QtGui.QToolBar(window)
		window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
		
		self.actionQuit = QtGui.QAction('Quit', window)
		self.actionQuit.setShortcut(QtGui.QKeySequence.Quit)
		
		self.actionShowBasemapLayer = QtGui.QAction('Basemap', window)
		self.actionShowBasemapLayer.setShortcut('Ctrl+B')
		self.actionShowBasemapLayer.setCheckable(True)
		
		self.actionShowLandmarkLayer = QtGui.QAction('Landmarks', window)
		self.actionShowLandmarkLayer.setShortcut('Ctrl+L')
		self.actionShowLandmarkLayer.setCheckable(True)
		
		self.actionShowBuildingLayer = QtGui.QAction('Buildings', window)
		self.actionShowBuildingLayer.setShortcut('Ctrl+B')
		self.actionShowBuildingLayer.setCheckable(True)
		
		icon = QtGui.QIcon(':/resources/mActionZoomIn.png')
		self.actionZoomIn = QtGui.QAction(icon, 'Zoom In', window)
		self.actionZoomIn.setShortcut(QtGui.QKeySequence.ZoomIn)
		
		icon = QtGui.QIcon(':/resources/mActionZoomOut.png')
		self.actionZoomOut = QtGui.QAction(icon, 'Zoom Out', window)
		self.actionZoomOut.setShortcut(QtGui.QKeySequence.ZoomOut)
		
		icon = QtGui.QIcon(':/resources/mActionPan.png')
		self.actionPan = QtGui.QAction(icon, 'Pan', window)
		self.actionPan.setShortcut('Ctrl+1')
		self.actionPan.setCheckable(True)
		
		icon = QtGui.QIcon(':/resources/mActionExplore.png')
		self.actionExplore = QtGui.QAction(icon, 'Explore', window)
		self.actionExplore.setShortcut('Ctrl+2')
		self.actionExplore.setCheckable(True)
		
		icon = QtGui.QIcon(':/resources/mActionEdit.png')
		self.actionEdit = QtGui.QAction(icon, 'Edit', window)
		self.actionEdit.setShortcut('Ctrl+3')
		self.actionEdit.setCheckable(True)
		
		icon = QtGui.QIcon(':/resources/mActionAddTrack.png')
		self.actionAddTrack = QtGui.QAction(icon, 'Add Track', window)
		self.actionAddTrack.setShortcut('Ctrl+4')
		self.actionAddTrack.setCheckable(True)
		
		icon = QtGui.QIcon(':/resources/mActionEditTrack.png')
		self.actionEditTrack = QtGui.QAction(icon, 'Edit Track', window)
		self.actionEditTrack.setShortcut('Ctrl+5')
		self.actionEditTrack.setCheckable(True)
		
		icon = QtGui.QIcon(':/resources/mDeleteTrack.png')
		self.actionDeleteTrack = QtGui.QAction(icon, 'Delete Track', window)
		self.actionDeleteTrack.setShortcut('Ctrl+6')
		self.actionDeleteTrack.setCheckable(True)
		
		icon = QIcon(":/resources/mActionGetInfo.png")
		self.actionGetInfo = QAction(icon, "Get Info", window)
		self.actionGetInfo.setShortcut("Ctrl+I")
		self.actionGetInfo.setCheckable(True)
		
		icon = QIcon(":/resources/mActionSetStartPoint.png")
		self.actionSetStartPoint = QAction(icon, "Set Start Point", window)
		self.actionSetStartPoint.setCheckable(True)
		
		icon = QIcon(":/resources/mActionSetEndPoint.png")
		self.actionSetEndPoint = QAction(icon, "Set End Point", window)
		self.actionSetEndPoint.setCheckable(True)
		
		icon = QIcon(":/resources/mActionFindShortestPath.png")
		self.actionFindShortestPath = QAction(icon, "Find Shortest Path", window)
		self.actionFindShortestPath.setCheckable(True)
		
		self.fileMenu.addAction(self.actionQuit)
		
		self.fileMenu.addAction(self.actionShowBasemapLayer)
		self.fileMenu.addAction(self.actionShowLandmarkLayer)
		self.fileMenu.addAction(self.actionShowBuildingLayer)
				
		self.mapMenu.addAction(self.actionZoomIn)
		self.mapMenu.addAction(self.actionZoomOut)
		self.mapMenu.addAction(self.actionPan)
		self.mapMenu.addAction(self.actionEdit)
		
		self.editMenu.addAction(self.actionAddTrack)
		self.editMenu.addAction(self.actionEditTrack)
		self.editMenu.addAction(self.actionDeleteTrack)
		self.editMenu.addAction(self.actionGetInfo)
		
		self.toolsMenu.addAction(self.actionSetStartPoint)
		self.toolsMenu.addAction(self.actionSetEndPoint)
		self.toolsMenu.addAction(self.actionFindShortestPath)
		
		self.toolBar.addAction(self.actionZoomIn)
		self.toolBar.addAction(self.actionZoomOut)
		self.toolBar.addAction(self.actionPan)
		self.toolBar.addAction(self.actionEdit)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionAddTrack)
		self.toolBar.addAction(self.actionEditTrack)
		self.toolBar.addAction(self.actionDeleteTrack)
		self.toolBar.addAction(self.actionGetInfo)
		self.toolBar.addSeparator()
		self.toolBar.addAction(self.actionSetStartPoint)
		self.toolBar.addAction(self.actionSetEndPoint)
		self.toolBar.addAction(self.actionFindShortestPath)
		
		window.resize(window.sizeHint())