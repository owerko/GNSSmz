import os
import gdal
import numpy as np
from simplekml import Kml, OverlayXY, ScreenXY, Units, AltitudeMode, Camera

def geotiff_to_kml(geotiff_file, output_kmz):
    # Open the GeoTIFF file
    dataset = gdal.Open(geotiff_file)
    if dataset is None:
        print("Failed to open the GeoTIFF file.")
        return

    # Get image dimensions
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize

    # Get geotransform information
    transform = dataset.GetGeoTransform()
    minx = transform[0]
    maxy = transform[3]
    maxx = minx + transform[1] * cols
    miny = maxy + transform[5] * rows

    # Create KML object
    kml = Kml()

    # Create ground overlay
    ground = kml.newgroundoverlay(name="GeoTIFF Overlay")

    # Set boundaries
    ground.latlonbox.north = maxy
    ground.latlonbox.south = miny
    ground.latlonbox.east = maxx
    ground.latlonbox.west = minx

    # Set the source image
    ground.icon.href = geotiff_file

    # Set transparency
    ground.alpha = 180

    # Create KMZ file
    kml.savekmz(output_kmz)
    print("KMZ file saved successfully.")

# Example usage
geotiff_file = "input.tif"  # Replace with your GeoTIFF file path
output_kmz = "output.kmz"    # Output KMZ file path
geotiff_to_kml(geotiff_file, output_kmz)
