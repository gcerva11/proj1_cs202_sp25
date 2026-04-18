from dataclasses import dataclass

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
    ghg_rate = 0.0
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
    pop = 10000000,
    ghg_rate = 0.0
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
    pop = 300000,
    ghg_rate = 0.0
)


