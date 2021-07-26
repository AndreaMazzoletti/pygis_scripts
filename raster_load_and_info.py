""" Script per la semplice dimostrazione di come caricare un raster e ottenerne le informazioni base (altezza, lunghezza, dimensione di una cella e quantità di fasce) """

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os


def run_script(iface):
    #Carico il layer
    source_file = "/dati_programmazione/raster/raster_peschiera.tif"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    raster_layer = QgsRasterLayer(path,"raster_peschiera")
    #Controllo se è valido
    if(raster_layer.isValid()):
        #Inserisco il raster nella mappa
        iface.addRasterLayer("/home/formai/Repository/GIS/dati_programmazione/raster/raster_peschiera.tif", "raster_peschiera")
        #Ottengo le unità per pixel dell'asse x e y
        print("Raster units per pixel on the x axis: ", raster_layer.rasterUnitsPerPixelX())
        print("Raster units per pixel on the y axis: ", raster_layer.rasterUnitsPerPixelY())
        #Ottengo l'altezza e la lunghezza in unità del raster
        print("Raster width: ", raster_layer.width())
        print("Raster height: ", raster_layer.height())
        #Ottengo il numero di fasce
        print("Number of bands: ", raster_layer.bandCount())

    else:
        print("The selected raster is not valid")
    pass
