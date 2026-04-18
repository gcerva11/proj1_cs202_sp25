from dataclasses import dataclass
import math import pi, sin
#complete your tasks in this file
@dataclass (frozen=True)
class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass (frozen=True)
class Region:
    rect: GlobeRect
    name: str
    terrain: "ocean" | "mountains" | "forest" | "other"

@dataclass (frozen=True)
class RegionCondition:
    region: Region
    year: int
    pop: int
    ghg_rate: float

#sample data

San_Francisco = RegionCondition(
    region = Region(
        rect = GlobeRect(
            lo_lat = 37.703399,
            hi_lat = 37.812,
            west_long = -122.527,
            east_long = -122.3482
        ),
        name = "San Francisco",
        terrain = "other"
    ),
    year = 2025,
    pop = 840000,
    ghg_rate = (840000 * 5)
)

London = RegionCondition(
    region = Region(
        rect = GlobeRect(
            lo_lat = 51.2868,
            hi_lat = 51.6919,
            west_long = -0.5103,
            east_long = 0.3340
        ),
        name = "London",
        terrain = "other"
    ),
    year = 2025,
    pop = 9000000,
    ghg_rate = (9000000 * 5)
)

Mediterranean_Sea = RegionCondition(
    region = Region(
        rect = GlobeRect(
            lo_lat = 30.0,
            hi_lat = 45.0,
            west_long = -5.0,
            east_long = 40.0
        ),
        name = "Mediterranean Sea",
        terrain = "ocean"
    ),
    year = 2025,
    pop = 0,
    ghg_rate = 0.0
)   

slo_county = RegionCondition(
    region = Region(
        rect = GlobeRect(
            lo_lat = 35.0,
            hi_lat = 36.0,
            west_long = -121.0,
            east_long = -120.0
        ),
        name = "San Luis Obispo County",
        terrain = "other"
    ),
    year = 2025,
    pop = 280000,
    ghg_rate = (280000 * 5)
)

def emissions_per_capita(rc: RegionCondition) -> float:
    if rc.pop == 0:
        return 0.0
    else: 
        return rc.ghg_rate / rc.pop 

def area(gr: GlobeRect) -> float:
    R = 6378.1 
    lambda1 = gr.west_long * (pi/180)
    lambda2 = gr.east_long * (pi/180)
    phi1 = gr.lo_lat * (pi/180)
    phi2 = gr.hi_lat * (pi/180)
    
    long_difference = lambda2 - lambda1
    if long_difference < 0:
        long_difference = long_difference + (2*pi)
    
    return ((R **2) * abs(long_difference) * abs(sin(phi2) - sin(phi1)))


def emissions_per_square_km(rc: RegionCondition) -> float:
    region_area = area(rc.region.rect)
    #per square km ?
    if region_area == 0:
        return 0.0
    return rc.ghg_rate / region_area
#co2 equivalent per square kilometer

def densest(lst:list[int]])-> str:
if index == len(lst - 1)
    return lst[index]

else:
    max_of_rest = find_max_recursive(lst, index+1)
    if lst[index] > max_of_rest:
        return lst[insex]
    else:
        return max_of_rest