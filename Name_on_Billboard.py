import unittest

def billboard(name, price=30):
    final_price = 0
    for i in name:
        final_price = final_price + price
    return final_price

class TestBillboardFunction(unittest.TestCase):
    def test_default_price(self):
        self.assertEqual(billboard("Hello"), 150)  
    
    def test_custom_price(self):
        self.assertEqual(billboard("Python", price=50), 300) 
    
    def test_empty_name(self):
        self.assertEqual(billboard("", price=50), 0)  
    
    def test_single_character_name(self):
        self.assertEqual(billboard("A"), 30)  
    
    def test_special_characters(self):
        self.assertEqual(billboard("!@#$%", price=10), 50)  

if __name__ == "__main__":
    unittest.main()