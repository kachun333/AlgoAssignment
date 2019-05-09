from math import radians, sin, cos, acos

# slat = Starting latitude
# slon = starting longitude
# elat = ending latitude
# elon = Ending longitude


def calculate(lat1, lon1, lat2, lon2):
    slat = radians(float(lat1))
    slon = radians(float(lon1))
    elat = radians(float(lat2))
    elon = radians(float(lon2))
    dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
    print("The distance is %.2fkm." % dist)


if __name__ == '__main__':

    print("kl to Brasilia")
    calculate(2.7456, 101.7072, -15.8697, -47.9172)
    print("kl to tokyo")
    calculate(2.7456, 101.7072, 35.5494, 139.7798)
    print("kl to London")
    calculate(2.7456, 101.7072, 51.5048, 0.0495)
    print("kl to New York")
    calculate(2.7456, 101.7072, 40.6413, -73.7781)
    print("kl to Bangkok")
    calculate(2.7456, 101.7072, 13.6900, 100.7501)
    print("kl to Kabul")
    calculate(2.7456, 101.7072, 34.5609, 69.2101)

    print("Brasilia to tokyo")
    calculate(-15.8697, -47.9172, 35.5494, 139.7798)
    print("Brasilia to London")
    calculate(-15.8697, -47.9172, 51.5048, 0.0495)
    print("Brasilia to New York")
    calculate(-15.8697, -47.9172, 40.6413, -73.7781)
    print("Brasilia to Bangkok")
    calculate(-15.8697, -47.9172, 13.6900, 100.7501)
    print("Brasilia to Kabul")
    calculate(-15.8697, -47.9172, 34.5609, 69.2101)

    print("Tokyo to London")
    calculate(35.5494, 139.7798, 51.5048, 0.0495)
    print("Tokyo to New York")
    calculate(35.5494, 139.7798, 40.6413, -73.7781)
    print("Tokyo to Bangkok")
    calculate(35.5494, 139.7798, 13.6900, 100.7501)
    print("Tokyo to Kabul")
    calculate(35.5494, 139.7798, 34.5609, 69.2101)

    print("London to New York")
    calculate(51.5048, 0.0495, 40.6413, -73.7781)
    print("London to Bangkok")
    calculate(51.5048, 0.0495, 13.6900, 100.7501)
    print("London to Kabul")
    calculate(51.5048, 0.0495, 34.5609, 69.2101)

    print("New York to Bangkok")
    calculate(40.6413, -73.7781, 13.6900, 100.7501)
    print("New York to Kabul")
    calculate(40.6413, -73.7781, 34.5609, 69.2101)

    print("Bangkok to Kabul")
    calculate(13.6900, 100.7501, 34.5609, 69.2101)
