#complete your tasks in this file
@dataclass 
class GlobeRect(frozen=True):
lo_lat: float
hi_lat: float
west_long: float
east_long: float

class Region:
    rect: GlobeRect
    name: str
    terrain: "ocean" | "mountains" | "forest" | "other"

class RegionCondition
    region: Region
    year: int
    pop: int
    ghg_rate: float

