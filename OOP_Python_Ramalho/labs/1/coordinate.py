from dataclasses import dataclass, fields
from geohash import encode
from typing import NamedTuple


class Coordinate:
    '''Coordinate on Earth'''
    reference_system: str = 'WGS84'

    def __init__(self, lat: float = 0, longi: float = 0):
        self.lat = lat
        self.longi = longi

    def geohash(self, precision: int = None):
        response = encode(self.lat, self.longi, precision) if precision \
            else encode(self.lat, self.longi)
        return response

    def __repr__(self):
        return f'Coordinate({self.lat}, {self.longi})'

    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.longi < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.longi):.1f}°{we}'


class Coordinate_V2(NamedTuple):
    lat: float = 0
    longi: float = 0
    reference_system = 'WGS84'

    def geohash(self, precision: int = None):
        response = encode(self.lat, self.longi, precision) if precision \
            else encode(self.lat, self.longi)
        return response

    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.longi < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.longi):.1f}°{we}'


@dataclass
class Coordinate_V3:
    lat: float = 0
    longi: float = 0
    reference_system = 'WGS84'

    def geohash(self, precision: int = None):
        response = encode(self.lat, self.longi, precision) if precision \
            else encode(self.lat, self.longi)
        return response

    def __str__(self):
        ns = 'NS'[self.lat < 0]
        we = 'EW'[self.longi < 0]
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.longi):.1f}°{we}'

    def __dict__(self):
        cls = self.__class__
        response = dict()

        for field in fields(cls):
            response[field.name] = getattr(self, field.name)

        return response


if __name__ == "__main__":
    c1 = Coordinate()
    c2 = Coordinate_V2()
    print(c1.geohash(), '\t', c1)
    print(c2.geohash(), '\t', c2)

    del c1
    del c2

    c1 = Coordinate(15, -104)
    c2 = Coordinate_V2(-45, -54)
    print(c1.geohash(), '\t', c1)
    print(c2.geohash(), '\t', c2)

    import pdb; pdb.set_trace()
