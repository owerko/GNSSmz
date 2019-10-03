from pyproj import Proj, transform


def trans_wgs84to2000(x, y):  # argumaty: dlugosc, szerokosc w stopniach
    inProj = Proj(init='epsg:4326')  # WGS 84
    outProj = Proj(init='epsg:2178')  # Uklad 2000 strefa 7
    return transform(inProj, outProj, x, y)


print(trans_wgs84to2000(20, 50))
