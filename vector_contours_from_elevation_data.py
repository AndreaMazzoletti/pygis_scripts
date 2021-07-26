""" Script per creare il contorno all'elevazione di un dem e salvarlo in uno shapefile usando gdal """

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import processing
import os


def run_script(iface):
    #Carico il layer
    source_file = "/dati_programmazione/dtm/dtm_vicenza.txt"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    dtm_layer = QgsRasterLayer(path,"DEM")
    if(dtm_layer.isValid()):
        #Aggiungo il dem al progetto
        iface.addRasterLayer(path , "dem_vicenza")
        #Creo i parametri
        parameters = {
            'INPUT': dtm_layer,
            'BAND': 1,
            'INTERVAL': 10,
            'OUTPUT': os.path.dirname(os.path.abspath(__file__)) + "/dati_programmazione/dtm/dtm_vicenza_contour.shp"
        }
        #Eseguo l'algoritmo contour di gdal con i parametri che ho creato prima
        processing.runAndLoadResults("gdal:contour", parameters)
    else:
        print("The selected dtm is not valid")

    pass
