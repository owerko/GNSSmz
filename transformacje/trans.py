from pyproj import Transformer

def dms(x):
    degrees = x // 1
    temp = (x - degrees) * 60
    minutes = temp // 1
    sec = (temp - minutes) * 60
    return degrees, minutes, sec


def decimal_degrees(degrees, minutes, sec):
    return degrees + minutes / 60 + sec / 3600


if __name__ == '__main__':

    #Ex1: WGS 84 [EPSG4326] to UTM 33N [EPSG25833]
    # lat = decimal_degrees(47, 23, 36.59)
    # long = decimal_degrees(13, 29, 21.70)
    # transformer1 = Transformer.from_crs('epsg:4326', 'epsg:25833')
    # x0, y0 = transformer1.transform(lat, long)
    #
    # print(f'Współrzędna X(N): {x0:.3f}')
    # print(f'Współrzędna Y(E): {y0:.3f}')

    x, y = 386000, 5250000
    transformer2 = Transformer.from_crs("EPSG:25833", "EPSG:4326")
    lon, lat = transformer2.transform(x, y)
    print(f'X: {x}, Y: {y}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')

    x1, y1 = 385000, 5266000
    lon, lat = transformer2.transform(x1, y1)
    print(f'X: {x1}, Y: {y1}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')
    x2, y2 = 408000, 5265000
    lon, lat = transformer2.transform(x2, y2)
    print(f'X: {x2}, Y: {y2}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')
    x3,y3 = 385000, 5249000
    lon, lat = transformer2.transform(x3, y3)
    print(f'X: {x3}, Y: {y3}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')
    x4, y4 = 408000, 5249000
    lon, lat = transformer2.transform(x4, y4)
    print(f'X: {x4}, Y: {y4}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')
    x5, y5 = 391000, 5257000
    lon, lat = transformer2.transform(x5, y5)
    print(f'X: {x5}, Y: {y5}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')
    x6, y6 = 398000, 5262000
    lon, lat = transformer2.transform(x6, y6)
    print(f'X: {x6}, Y: {y6}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')
    x7, y7 = 395000, 5259000
    lon, lat = transformer2.transform(x7, y7)
    print(f'X: {x7}, Y: {y7}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\" ')
    #
    #
    # #Ex2: Earth-centered, Earth-fixed coordinate system WGS84 [EPSG4978] to WGS84 [EPSG4326]
    # transformer2 = Transformer.from_crs("EPSG:4978", "EPSG:4326", always_xy=True)
    #
    # # Example coordinates in EPSG:4978
    # x, y, z = 3912239.4942, 1357006.7149, 4835451.9071  # Replace these with your coordinates
    #
    # # Transform the coordinates
    # lon, lat, alt = transformer2.transform(x, y, z)
    #
    # # Print the transformed coordinates
    # print(f'X: {x}, Y: {y}, Z: {z}')
    # print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0, Altitude: {alt:.4f}m")
    # print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\", Altitude: {alt:.4f}m ')
