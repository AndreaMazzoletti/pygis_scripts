
""" Script per determinare il nearest neighbor di un punto usando gli spatial index """

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os


def run_script(iface):
    source_file = "/dati_programmazione/Beni_culturali_puntiformi.shp"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    points_layer = QgsVectorLayer(path , "Beni_Culturali_Lombardia", "ogr")
    features = list(points_layer.getFeatures())
    first_feature = features[0]
    #Creo un index dove la prima feature è il punto cardine
    index = QgsSpatialIndex()
    #Aggiungo le feature allo spatial index
    for feature in features:
        index.addFeature(feature)
    #Se cerco il nearest neighbour scrivo 2, perchè il primo risultato è il punto stesso
    print(index.nearestNeighbor(first_feature.geometry().asPoint(), 2, 100000))
    pass
