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

    #Ex1: WGS 84 [EPSG4326] to 2000 [EPSG2178]
    # lat = decimal_degrees(50, 3, 56.71715)
    # long = decimal_degrees(19, 55, 12.92679)
    # transformer1 = Transformer.from_crs('epsg:4326', 'epsg:2178')
    # x0, y0 = transformer1.transform(lat, long)
    #
    # print(f'Współrzędna X(N): {x0:.3f}')
    # print(f'Współrzędna Y(E): {y0:.3f}')


    #Ex2: ECEF WGS84 [EPSG4978] to WGS84 [EPSG4326]
    transformer2 = Transformer.from_crs("EPSG:4978", "EPSG:4326", always_xy=True)

    # Example coordinates in EPSG:4978
    x, y, z = 3912239.4942, 1357006.7149, 4835451.9071  # Replace these with your coordinates

    # Transform the coordinates
    lon, lat, alt = transformer2.transform(x, y, z)

    # Print the transformed coordinates
    print(f'X: {x}, Y: {y}, Z: {z}')
    print(f"Latitude: {lat:.10f}\u00B0, Longitude: {lon:.10f}\u00B0, Altitude: {alt:.4f}m")
    print(f'Latitude {dms(lat)[0]:.0f}\u00B0{dms(lat)[1]:.0f}\'{dms(lat)[2]:.5f}\", Longitude: {dms(lon)[0]:.0f}\u00B0{dms(lon)[1]:.0f}\'{dms(lon)[2]:.5f}\", Altitude: {alt:.4f}m ')
