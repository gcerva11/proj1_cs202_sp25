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
#######################################################################################################
    def test_pop_density_normal(self) -> None:
        self.assertTrue(pop_density(San_Francisco) > 0)

    def test_pop_density_zero_population(self) -> None:
        self.assertAlmostEqual(pop_density(Mediterranean_Sea), 0.0, places=4)

    def test_pop_density_zero_area(self) -> None:
        rc = RegionCondition(
            region=Region(
                rect=GlobeRect(5.0, 5.0, 1.0, 2.0),
                name="Zero Area Region",
                terrain="other"
            ),
            year=2025,
            pop=100,
            ghg_rate=1000.0
        )
        self.assertAlmostEqual(pop_density(rc), 0.0, places=4)
#######################################################################################################
    def test_densest_multiple_regions(self) -> None:
        self.assertEqual(
            densest([San_Francisco, London, Mediterranean_Sea, slo_county]),
            "San Francisco"
        )

    def test_densest_single_item(self) -> None:
        self.assertEqual(densest([London]), "London")

    def test_densest_with_zero_population_region(self) -> None:
        self.assertEqual(
            densest([Mediterranean_Sea, San_Francisco]),
            "San Francisco"
        )

    def test_densest_tie_prefers_first(self) -> None:
        rect = GlobeRect(0.0, 1.0, 0.0, 1.0)

        rc1 = RegionCondition(
            region=Region(rect, "First", "other"),
            year=2025,
            pop=1000,
            ghg_rate=5000.0
        )
        rc2 = RegionCondition(
            region=Region(rect, "Second", "other"),
            year=2025,
            pop=1000,
            ghg_rate=7000.0
        )

        self.assertEqual(densest([rc1, rc2]), "First")
#######################################################################################################
    def test_pop_growth_ocean(self) -> None:
        r = Region(GlobeRect(0.0, 1.0, 0.0, 1.0), "Ocean Test", "ocean")
        self.assertAlmostEqual(pop_growth(r), 0.0001, places=6)

    def test_pop_growth_mountains(self) -> None:
        r = Region(GlobeRect(0.0, 1.0, 0.0, 1.0), "Mountain Test", "mountains")
        self.assertAlmostEqual(pop_growth(r), 0.0005, places=6)

    def test_pop_growth_forest(self) -> None:
        r = Region(GlobeRect(0.0, 1.0, 0.0, 1.0), "Forest Test", "forest")
        self.assertAlmostEqual(pop_growth(r), -0.00001, places=6)

    def test_pop_growth_other(self) -> None:
        r = Region(GlobeRect(0.0, 1.0, 0.0, 1.0), "Other Test", "other")
        self.assertAlmostEqual(pop_growth(r), 0.0003, places=6)

#######################################################################################################
    def test_project_condition_updates_year(self) -> None:
        projected = project_condition(San_Francisco, 10)
        self.assertEqual(projected.year, San_Francisco.year + 10)

    def test_project_condition_keeps_same_region(self) -> None:
        projected = project_condition(London, 5)
        self.assertEqual(projected.region, London.region)
    
    def test_project_condition_positive_growth(self) -> None:
        projected = project_condition(San_Francisco, 10)
        self.assertTrue(projected.pop >= San_Francisco.pop)
        self.assertTrue(projected.ghg_rate >= San_Francisco.ghg_rate)

    def test_project_condition_forest_decreases_population(self) -> None:
        forest_rc = RegionCondition(
            region=Region(
                rect=GlobeRect(1.0, 2.0, 3.0, 4.0),
                name="Forest Region",
                terrain="forest"
            ),
            year=2025,
            pop=100000,
            ghg_rate=500000.0
        )

        projected = project_condition(forest_rc, 10)
        self.assertTrue(projected.pop <= forest_rc.pop)

    def test_project_condition_emissions_scale_with_population(self) -> None:
        projected = project_condition(San_Francisco, 1)
        expected = San_Francisco.ghg_rate * (projected.pop / San_Francisco.pop)
        self.assertAlmostEqual(projected.ghg_rate, expected, places=4)

if __name__ == "__main__":
    unittest.main()