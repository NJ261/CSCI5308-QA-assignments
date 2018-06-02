import unittest
import A1
import part_manager
import security


class test_A1(unittest.TestCase):
    
# -----------------------------------  set up the mock data for test cases  ----------------------------------- 
    def setUp(self):
        self.security1 = security.Security("XXX-1234-ABCD-1234", None)
        self.security2 = security.Security(None, "kkklas8882kk23nllfjj88290")
        self.security3 = security.Security("XXX-1234-ABCD-1234", "kkklas8882kk23nllfjj88290")
        
        self.part_check1 = part_manager.Part_Manager("1233", "2")
        self.part_check2 = part_manager.Part_Manager(None, "5")
        self.part_check3 = part_manager.Part_Manager("2222", None)
        
        self.delivery1 = part_manager.DeliveryAddress("Mr. Jadeja", "South Park St", "Halifax", "NS", "B3J2K9")
        self.delivery2 = part_manager.DeliveryAddress(None, "South Park St", "Halifax", "NS", "B3J2K9")
        self.delivery3 = part_manager.DeliveryAddress("Mr. Jadeja", None, "Halifax", "NS", "B3J2K9")
        self.delivery4 = part_manager.DeliveryAddress("Mr. Jadeja", "South Park St", None, "NS", "B3J2K9")
        self.delivery5 = part_manager.DeliveryAddress("Mr. Jadeja", "South Park St", "Halifax", None, "B3J2K9")
        self.delivery6 = part_manager.DeliveryAddress("Mr. Jadeja", "South Park St", "Halifax", "NS", None)
        
        self.auth1 = security.Security("FAKEDEALER", "FAKEACCEESKEY")
        self.auth2 = security.Security("XXX-1111-ABCD-1111", "abcd123wxyz456qwerty78901")
        self.auth3 = security.Security("XXX-2222-ABCD-2222", "kkklas8882kk23nllfjj88292") 

        self.part_status1 = part_manager.Part_Manager(["1234", "1111", "2222", "3333", "4444", "fake_part_number"], 
                                                      ["1","2","3","4","5","6"])     

    
# -----------------------------------  Class: Security  ----------------------------------- 
# -----------------------------------------------------------------------------------------
        
    # ------------------------------  Method: validate_dealer -----------------------------  
    def test_dealerCheck(self):
        self.assertEqual(self.security1.validate_dealer(), "Invalid Input XML Response Error: in Dealer Access Key")
        self.assertEqual(self.security2.validate_dealer(), "Invalid Input XML Response Error: in Dealer Id")
        self.assertEqual(self.security3.validate_dealer(), "Dealer details validated")
        
        
    # ------------------------------  Method: isDealerAuthorized --------------------------- 
    def test_dealer_auth(self):
        self.assertEqual(self.auth1.isDealerAuthorized(), "dealer not authorized.")
        self.assertEqual(self.auth2.isDealerAuthorized(), "dealer not authorized.")
        self.assertEqual(self.auth3.isDealerAuthorized(), "dealer authenticated")
        
        
# -----------------------------------  Class: part_manager  --------------------------------
# ------------------------------------------------------------------------------------------
        
    # ------------------------------  Method: validate_parts ------------------------------- 
    def test_partsCheck(self):
        self.assertEqual(self.part_check1.validate_parts(), "Part Number and Quantity are good.")
        self.assertEqual(self.part_check2.validate_parts(), "Invalid Input XML Response: Error in Part number")
        self.assertEqual(self.part_check3.validate_parts(), "Invalid Input XML Response: Error in Quantity")
       
    # ------------------------------  Method: validate_delivery ----------------------------
    def test_delivery(self):
        self.assertEqual(self.delivery1.validate_delivery(), "Delivery Details are good")
        self.assertEqual(self.delivery2.validate_delivery(), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(self.delivery3.validate_delivery(), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(self.delivery4.validate_delivery(), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(self.delivery5.validate_delivery(), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(self.delivery6.validate_delivery(), "Invalid Input XML Response: Error in Delivery Details")
    
    # ------------------------------  Method: SubmitPartForManufactureAndDelivery -----------
    def test_part_status_check(self):
        self.assertEqual(self.part_status1.SubmitPartForManufactureAndDelivery(), 
                         ['success', 'out of stock', 'no longer manufactured', 'invalid part', 'success', 'Invalid Part'])
        

# -----------------------------------  Class: A1  -------------------------------------------
# -------------------------------------------------------------------------------------------
        
    # ------------------------------  Method: main_function ---------------------------------
    def test_main_function(self):
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', '35 Streetname', 'Halifax', 'NS', 'B2T1A4'],
                                          ['1234', '5678'], ['2', '25']), "Dealer is authorized, check the response in output.xml")
        self.assertEqual(A1.main_function([None, 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', '35 Streetname', 'Halifax', 'NS', 'B2T1A4'], ['1234', '5678'],
                                          ['2', '25']), "Invalid Input XML Response Error: in Dealer Id")
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', None], ['Mrs. Jane Smith', '35 Streetname', 'Halifax', 'NS', 'B2T1A4'],
                                          ['1234', '5678'], ['2', '25']), "Invalid Input XML Response Error: in Dealer Access Key")
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], [None, '35 Streetname', 'Halifax', 'NS', 'B2T1A4'], ['1234', '5678'], 
                                          ['2', '25']), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', None, 'Halifax', 'NS', 'B2T1A4'],
                                          ['1234', '5678'], ['2', '25']), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', '35 Streetname', None, 'NS', 'B2T1A4'],
                                          ['1234', '5678'], ['2', '25']), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', '35 Streetname', 'Halifax', None, 'B2T1A4'], 
                                          ['1234', '5678'], ['2', '25']), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', '35 Streetname', 'Halifax', 'NS', None], 
                                          ['1234', '5678'], ['2', '25']), "Invalid Input XML Response: Error in Delivery Details")
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', '35 Streetname', 'Halifax', 'NS', 'B2T1A4'],
                                          ["0000", '5678'], ['2', '25']), "Dealer is authorized, check the response in output.xml")   
        self.assertEqual(A1.main_function(['XXX-1234-ABCD-1234', 'kkklas8882kk23nllfjj88290'], ['Mrs. Jane Smith', '35 Streetname', 'Halifax', 'NS', 'B2T1A4'],
                                          ['1234', '5678'], ['0', '25']), "Invalid Input XML Response: Error in Quantity")


        
if __name__ == '__main__':
    unittest.main()
