# -*- coding: utf-8 -*-
"""
/***************************************************************************
 mapasBaseDockWidget
                                 A QGIS plugin
 Este plugin permite visualizar/descargar mapas base del IGN
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-01-23
        git sha              : $Format:%H$
        copyright            : (C) 2023 by IGN
        email                : ign@ign.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTreeWidgetItem #####
from PyQt5.QtGui import QIcon, QPixmap ######
from PyQt5 import Qt ######

import xml.etree.ElementTree as et #...........arbol manual...........# va?

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'mapas_base_dockwidget_base.ui'))


class mapasBaseDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):

        #self.ax = mapasBase()

        """Constructor."""
        super(mapasBaseDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect

        self.setupUi(self)

#########################################   METODOS   #########################################
#----------------------------------- CARGAR LOGO IGN -------------------------------------------#
    def cargarLogo(self):
        self.img = QPixmap(":/plugins/mapas_base/LogoIgn.png")
        scaled = self.img.scaled(self.logo.size())
        self.logo.setPixmap(scaled)
        

#--------------------------- CARGAR MAPA BASE EN LA VISTA PREVIA ------------------------------#
    def cargarMapa(self):
        if self.radioButton_1.isChecked():
            self.imagen = QPixmap(":/plugins/mapas_base/argenmap.png")
        
        if self.radioButton_2.isChecked():
            self.imagen = QPixmap(":/plugins/mapas_base/argenmapGris.png")
        
        if self.radioButton_3.isChecked():
            self.imagen = QPixmap(":/plugins/mapas_base/argenmapTopografico.png")
        
        if self.radioButton_4.isChecked():
            self.imagen = QPixmap(":/plugins/mapas_base/argenmapOscuro.png")

        
        scaled = self.imagen.scaled(self.label_3.size())
        self.label_3.setPixmap(scaled)


   #------------------------------------------------------------------------------------------#
    """ Function that closes the plugin """
    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()