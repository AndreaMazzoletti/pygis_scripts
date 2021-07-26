""" Script per aggiungere un poligono ad un layer esistente """

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os


def run_script(iface):
    #Carico il layer poligonale
    source_file = "/dati_programmazione/polygon_example.shp"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    polygon_layer = QgsVectorLayer(path, "poligono_esempio", "ogr")
    #Creo il data provider del layer
    polygon_layer_data_provider = polygon_layer.dataProvider()
    #Creo un array di punti che sono i vertici del mio poligono che andrò ad aggiungere
    points = []
    points.append(QgsPointXY(-123.26,49.06))
    points.append(QgsPointXY(-127.19,43.07))
    points.append(QgsPointXY(-120.70,35.21))
    points.append(QgsPointXY(-115.89,40.02))
    points.append(QgsPointXY(-113.04,48.47))
    points.append(QgsPointXY(-123.26,49.06))
    #Creo il poligono
    polygon_to_add = QgsGeometry.fromPolygonXY([points])
    #Metto il poligono in una feature
    feature = QgsFeature()
    feature.setGeometry(polygon_to_add)
    #Aggiungo la feature al data provider (e quindi al poligono)
    polygon_layer_data_provider.addFeatures([feature])
    pass
