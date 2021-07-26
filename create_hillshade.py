""" Script per creare un hillshade da un raster """

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import processing
import os

def run_script(iface):
    #Importo il raster
    source_file = "/dati_programmazione/raster/raster_peschiera.tif"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    raster_layer = QgsRasterLayer(path,"raster_peschiera_hillshade")
    if(raster_layer.isValid()):
        #Imposto i parametri
        parameters = {'INPUT': raster_layer, 
                'BAND': 1, 
                'COMPUTE_EDGES': False,
                'ZEVENBERGEN': False,
                'Z_FACTOR': 1.0,
                'SCALE': 1.0,
                'AZIMUTH': 315,
                'COMBINED': False,
                'ALTITUDE': 45,
                'MULTIDIRECTIONAL': False,
                'OUTPUT': os.path.dirname(os.path.abspath(__file__)) + "/dati_programmazione/raster/raster_peschiera_hillshade.tif"}
        #Eseguo l'algoritmo hillshadedi gdal con i parametri che ho creato
        processing.runAndLoadResults("gdal:hillshade", parameters)
    else:
        print("The selected raster is not valid")
    pass
