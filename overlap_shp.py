
""" Script che trova i punti dentro il layer poligonale e li evidenzia solo se il comune dei punti dentro il poligono è Breno """

# imports

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import os


def run_script(iface):
    #Aggiungo i layer
    source_file_pts = "/dati_programmazione/Beni_culturali_puntiformi.shp"
    source_file_poly = "/dati_programmazione/poligoni_10k_foglio_078_breno.shp"
    path_pts = os.path.dirname(os.path.abspath(__file__)) + source_file_pts
    path_poly = os.path.dirname(os.path.abspath(__file__)) + source_file_poly
    layer_pts = QgsVectorLayer(path_pts, "Beni_Culturali_Lombardia", "ogr")
    layer_poly = QgsVectorLayer(path_poly, "Media_valcamonica", "ogr")
    if layer_poly.isValid() and layer_pts.isValid():
        QgsProject.addMapLayers(QgsProject.instance(), [layer_poly,layer_pts], True)
        features_poly = layer_poly.getFeatures()
        features_points = layer_pts.getFeatures()
        #Prendo ogni componente del layer poligonale e per ognuno di questi prendo tutti i punti e guardo se si sovrappongono e se sono dentro al comune di Breno
        for feature_poly in features_poly:
            polygon_geometry = feature_poly.geometry()
            feature_point = layer_pts.getFeatures(QgsFeatureRequest().setFilterRect(polygon_geometry.boundingBox()))
            for point in feature_point:
                if point.geometry().within(polygon_geometry) and (point.attribute('COMUNE') == "Breno"):
                    #Se si sovrappongono e sono nel comune di Breno allora seleziono il punto
                    layer_pts.select(point.id())
        #Attivo la selezione e setto il layer attivo a quello dei punti
        iface.setActiveLayer(layer_pts)
        iface.zoomToActiveLayer()
    else:
        print("Some of the selected layers are not valid")
    pass
