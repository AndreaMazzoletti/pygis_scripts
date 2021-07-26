""" Script per esportare gli shapefiles(.shp) in file kml (.kml) dato che questi ultimi sono lo standard per ogr usato da qgis"""

#imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os

def run_script(iface):
    #importo il layer
    source_file = "/dati_programmazione/Beni_culturali_puntiformi.shp"
    path = os.path.dirname(os.path.abspath(__file__)) + source_file
    layer = QgsVectorLayer(path, "Beni_Culturali_Lombardia", "ogr")
    if(layer.isValid()):
        #Specifico il crs con cui sarà rappresentato il layer
        dest_crs = QgsCoordinateReferenceSystem(32632)
        #Esporto in kml
        QgsVectorFileWriter.writeAsVectorFormat(layer,os.path.dirname(os.path.abspath(__file__)) + "/dati_programmazione/beni_culturali_puntiformi.kml", "utf-8", dest_crs, "KML")
    else:
        print("The selected layer is not valid")
    pass
