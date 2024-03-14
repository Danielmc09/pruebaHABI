import unittest
from bloques_ordenados import ordenar_bloques

class TestOrdenarBloques(unittest.TestCase):

    def test_bloques_basicos(self):
        self.assertEqual(ordenar_bloques([1,3,2,0,7,8,1,3,0,6,7,1]), "123 1378 167")

    def test_bloques_con_vacios(self):
        self.assertEqual(ordenar_bloques([2,1,0,0,3,4]), "12 X 34")

    def test_tres_ceros_consecutivos(self):
        self.assertEqual(ordenar_bloques([1,2,0,0,0,3,4]), "12 X X 34")

    def test_arreglo_vacio(self):
        self.assertEqual(ordenar_bloques([]), "")

    def test_solo_ceros(self):
        self.assertEqual(ordenar_bloques([0,0]), "X X")

    def test_sin_ceros(self):
        self.assertEqual(ordenar_bloques([9,1,5]), "159")

if __name__ == "__main__":
    unittest.main()
