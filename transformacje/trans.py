from pyproj import Proj, transform


def trans_wgs84to2000(x, y):  # argumaty: dlugosc, szerokosc w stopniach
    inProj = Proj(init='epsg:4326')  # WGS 84
    outProj = Proj(init='epsg:2178')  # Uklad 2000 strefa 7
    return transform(inProj, outProj, x, y)


# dd mm ss.sssss -> dd+mm/60+ss.sssss/36000


def trans_2000towgs84(x, y):  # argumaty: dlugosc, szerokosc w stopniach
    outProj = Proj(init='epsg:4326')  # WGS 84
    inProj = Proj(init='epsg:2178')  # Uklad 2000 strefa 7
    return transform(inProj, outProj, x, y)


def dms(x):
    degrees = x // 1
    temp = (x - degrees) * 60
    minutes = temp // 1
    sec = (temp - minutes)*60
    return degrees, minutes, sec


def decimal_degrees(degrees, minutes, sec):
    return degrees + minutes / 60 + sec / 3600


if __name__ == '__main__':
    # print(trans_wgs84to2000(20, 50))

    # Kraw
    x, y = trans_2000towgs84(7422714.354, 5548331.631)
    print(x)
    print(dms(x))
    print(y)
    print(dms(y))
