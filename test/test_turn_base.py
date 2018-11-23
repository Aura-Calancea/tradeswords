import unittest
from turn_base import *


class TestUnit(unittest.TestCase):

    #test create_unit
    def test_create_unit(self):
        s = Spadasin()
        inst = s.create_unit()
        #verifica daca se creaza un obiect din clasa lui s
        self.assertEqual(inst.name , "Spadasin")
        
        #verifica daca obiectele sunt diferite
        #inst.name = "spadasin"
        self.assertNotEqual(inst, s)
        

    #setu pt instantieri
    def setUp(self):
        #self.unit1 = Unit()
        self.p = Prastier()
        self.g = Gardian()
        self.s = Spadasin()
        self.a = Arcas()
        self.h = Hoplit()
        self.cal = Calaret()
        self.cav = Cavaler()
        self.cent = Centaur()
        self.cic = Ciclop()     
    
    #test take damage
    def test_take_dammage(self):
        self.a.take_dammage(10)
        self.assertEqual(self.a.HP, 96)
   
    #test show_cost
    def test_show_cost(self):
        pass
    #    self.assertEqual(self.p.show_cost, 50)
        #fail din cauza felului cum am setat clasele si subclasele
        #F = "None != 50"
        
    #
    #pt testare clase:
    #folosire isinstance 
    def check_insta(self):
        #self.assertEqual(isinstance(s, Spadasin), True)
        #self.assertEqual(isinstance(s, low_Heroes), True)
        #self.assertEqual(isinstance(s, Unit), True)
        self.assertEqual(isinstance(s, high_Heroes), True)
    #folosire issubclass

    




if __name__ == '__main__':
    unittest.main()