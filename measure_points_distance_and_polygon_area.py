
""" Script per misurare la distanza fra due punti"""

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os


def run_script(iface):
    #Distanza fra due punti
    source_file_pts = "/dati_programmazione/Beni_culturali_puntiformi.shp"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file_pts
    points_layer = QgsVectorLayer(path, "Beni_Culturali_Lombardia", "ogr")
    features = list(points_layer.getFeatures())
    first_feature = features[0]
    last_feature = features[1]
    distance = QgsDistanceArea()
    print(distance.measureLine([first_feature.geometry().asPoint(),last_feature.geometry().asPoint()]))

    #Area di un poligono
    source_file_poly = "/dati_programmazione/poligoni_10k_foglio_078_breno.shp"
    polygon_layer = QgsVectorLayer(os.path.dirname(os.path.abspath(__file__)) + source_file_poly, "Media_valcamonica", "ogr")
    polygon_features = list(polygon_layer.getFeatures())
    feature = polygon_features[0]
    polygon_distance = QgsDistanceArea()
    print(distance.measureArea(feature.geometry()))

    pass
