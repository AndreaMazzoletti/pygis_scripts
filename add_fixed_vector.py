"""Script per aggiungere un layer alla mappa"""

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os

def run_script(iface):
    source_file = "/dati_programmazione/Beni_culturali_puntiformi.shp"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    layer = QgsVectorLayer(path, "Beni_Culturali_Lombardia", "ogr")
    if(layer.isValid()):
        QgsProject.addMapLayers(QgsProject.instance(), [layer], True)
    else:
        print("The layer is invalid")
    pass
