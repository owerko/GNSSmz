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
    lat = decimal_degrees(50, 3, 56.71715)
    long = decimal_degrees(19, 55, 12.92679)
    transformer = Transformer.from_crs('epsg:4326', 'epsg:2178')
    x, y = transformer.transform(lat, long)

    print(f'Współrzędna X(N): {x:.3f}')
    print(f'Współrzędna Y(E): {y:.3f}')
