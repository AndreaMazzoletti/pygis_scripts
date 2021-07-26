""" Script per ottenere i dati da un certo punto del raster (in questo esempio il centro ma può essere sostituito da un qualsiasi punto XY)  """

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os


def run_script(iface):
    #Carico il raster
    source_file = "/dati_programmazione/raster/raster_peschiera.tif"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    raster_layer = QgsRasterLayer(path,"raster_peschiera")
    #Ottengo il punto al centro
    center_point = raster_layer.dataProvider().extent().center()
    #Costruisco e verifico la query identificando il punto sul raster
    query = raster_layer.dataProvider().identify(center_point, QgsRaster.IdentifyFormatValue)
    query.isValid()
    #Eseguo la query
    print(query.results())
    pass
