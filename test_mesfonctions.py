import unittest

from mesfonctions import (
    somme,
    factorielle,
    est_premier,
    celsius_en_fahrenheit as celsius_vers_fahrenheit,
    compter_voyelles,
)


class TestMesFonctions(unittest.TestCase):
    def test_somme_normale(self):
        self.assertEqual(somme(2, 3), 5)
        self.assertEqual(somme(-1, 4), 3)
        self.assertEqual(somme(0, 0), 0)

    def test_somme_flottante(self):
        self.assertAlmostEqual(somme(2.5, 1.5), 4.0)

    def test_factorielle_normale(self):
        self.assertEqual(factorielle(5), 120)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(0), 1)

    def test_factorielle_negatif(self):
        with self.assertRaises(ValueError):
            factorielle(-2)

    def test_est_premier_normale(self):
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(17))
        self.assertFalse(est_premier(1))
        self.assertFalse(est_premier(18))

    def test_est_premier_grand_nombre(self):
        self.assertTrue(est_premier(97))
        self.assertFalse(est_premier(100))

    def test_celsius_vers_fahrenheit_normale(self):
        self.assertEqual(celsius_vers_fahrenheit(0), 32)
        self.assertEqual(celsius_vers_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_vers_fahrenheit(-40), -40)

    def test_compter_voyelles_normale(self):
        self.assertEqual(compter_voyelles("bonjour"), 2)
        self.assertEqual(compter_voyelles("AEIOUY"), 6)
        self.assertEqual(compter_voyelles("Bcdfg"), 0)

    def test_compter_voyelles_avec_espaces(self):
        self.assertEqual(compter_voyelles("Une phrase avec des voyelles"), 11)


if __name__ == "__main__":
    unittest.main()
