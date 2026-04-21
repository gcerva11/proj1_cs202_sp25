import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestStudent(unittest.TestCase):
    def test_emissions_per_capita_normal(self) -> None:
        self.assertAlmostEqual(emissions_per_capita(San_Francisco), 5.0, places=4)

    def test_emissions_per_capita_zero_population(self) -> None:
        self.assertAlmostEqual(emissions_per_capita(Mediterranean_Sea), 0.0, places=4)

    def test_emissions_per_capita_fraction(self) -> None:
        tiny = RegionCondition(
            region=Region(
                rect=GlobeRect(0.0, 1.0, 0.0, 1.0),
                name="Tiny",
                terrain="other"
            ),
            year=2025,
            pop=2,
            ghg_rate=1.0
        )
        self.assertAlmostEqual(emissions_per_capita(tiny), 0.5, places=4)
#######################################################################################################
    def test_area_positive(self) -> None:
        self.assertTrue(area(San_Francisco.region.rect) > 0)

    def test_area_zero_width(self) -> None:
        gr = GlobeRect(10.0, 20.0, 5.0, 5.0)
        self.assertAlmostEqual(area(gr), 0.0, places=4)

    def test_area_wraparound_dateline(self) -> None:
        gr = GlobeRect(10.0, 20.0, 170.0, -170.0)
        self.assertTrue(area(gr) > 0)

    def test_area_small_region(self) -> None:
        gr = GlobeRect(37.7, 37.8, -122.5, -122.4)
        self.assertTrue(area(gr) > 0)
#######################################################################################################
    def test_emissions_per_square_km_normal(self) -> None:
        self.assertTrue(emissions_per_square_km(San_Francisco) > 0)

    def test_emissions_per_square_km_zero_emissions(self) -> None:
        self.assertAlmostEqual(emissions_per_square_km(Mediterranean_Sea), 0.0, places=4)

    def test_emissions_per_square_km_zero_area(self) -> None:
        rc = RegionCondition(
            region=Region(
                rect=GlobeRect(10.0, 10.0, 20.0, 30.0),
                name="Flat Line",
                terrain="other"
            ),
            year=2025,
            pop=1000,
            ghg_rate=5000.0
        )
        self.assertAlmostEqual(emissions_per_square_km(rc), 0.0, places=4)

if __name__ == "__main__":
    unittest.main()