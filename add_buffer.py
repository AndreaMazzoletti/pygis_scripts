
"""Script che crea buffer attorno a un punto (qui preso a caso) """

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os


def run_script(iface):
    #Carico il layer
    source_file = "/dati_programmazione/Beni_culturali_puntiformi.shp"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    layer = QgsVectorLayer(path , "Beni_Culturali_Lombardia", "ogr")
    if(layer.isValid()):
        #Carico il layer sulla mappa e seleziono una feature
        QgsProject.addMapLayer(QgsProject.instance(), layer, True)
        features = list(layer.getFeatures())
        single_feature = features[0]
        layer.select(single_feature.id())
        #Prendo la geometry e ci creo attorno il buffer
        buffer = single_feature.geometry().buffer(1000,10000)
        #Creo un layer temporaneo che ha il buffer come unico punto
        buffer_layer = QgsVectorLayer('Polygon?crs=EPSG:32632', 'Buffer' , 'memory')
        #Inserisco il buffer in un punto (l'unico) del layer
        buffer_object = QgsFeature()
        buffer_object.setGeometry(buffer)
        #Lo inserisco nel data provider del layer
        buffer_layer_data_provider = buffer_layer.dataProvider() 
        buffer_layer_data_provider.addFeatures([buffer_object])
        #Aggiorno il layer
        buffer_layer.updateExtents()
        #Aggiungo il layer del buffer
        QgsProject.addMapLayer(QgsProject.instance(), buffer_layer, True)
    else:
        print("The selected layer is invalid")
    pass
