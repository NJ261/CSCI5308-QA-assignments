import unittest
import A1

class test_A1(unittest.TestCase):
    
    def test_dealerCheck(self):
        # Method 1
        self.assertIsNotNone(A1.dealer_tag[0])      # checking Dealer ID
        self.assertIsNotNone(A1.dealer_tag[1])      # checking Dealer Access Key
        
        # Method 2
        self.assertEqual(A1.validate_dealer("XXX-1234-ABCD-1234", None), "Invalid Input XML Response")
        self.assertEqual(A1.validate_dealer(None, "kkklas8882kk23nllfjj88290"), "Invalid Input XML Response")
        self.assertEqual(A1.validate_dealer("XXX-1234-ABCD-1234", "kkklas8882kk23nllfjj88290"), "Dealer Authenticated")
        
    def test_partsCheck(self):
        self.assertEqual(A1.validate_parts("1233", "2"), "Part Number and Quantity are good.")
        self.assertEqual(A1.validate_parts(None, "5"), "Invalid Input XML Response: Error in Part number")
        self.assertEqual(A1.validate_parts("1234", None), "Invalid Input XML Response: Error in Quantity")
        
    def test_delivery(self):
        self.assertEqual(A1.validate_delivery("Mr. Jadeja"), "Delivery Details are good")
        self.assertEqual(A1.validate_delivery("South Park St."), "Delivery Details are good")
        self.assertEqual(A1.validate_delivery("Halifax"), "Delivery Details are good")
        self.assertEqual(A1.validate_delivery("NS"), "Delivery Details are good")
        self.assertEqual(A1.validate_delivery("B3J2K9"), "Delivery Details are good")
        
        
if __name__ == '__main__':
    unittest.main()
