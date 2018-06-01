import mock_data

class Part_Manager:
    
    def __init__(self, part_number, quantity):
        self.part_number = part_number
        self.quantity = quantity
        
    def validate_parts(self):
        temp = []
        temp_msg = ""
        temp_part_number = [self.part_number]
        temp_quantity = [self.quantity]
        
        for i in range(0, len(temp_part_number)):
            
            if temp_part_number[i] is None:
                temp_msg = "Invalid Input XML Response: Error in Part number"
                print temp_msg
                break
            
            else:
                temp.append(int(self.part_number[i]))
                temp_msg = "Part Number and Quantity are good."
                
                if temp_quantity[i] is None:
                    temp_msg = "Invalid Input XML Response: Error in Quantity"
                    print temp_msg
                    break
                    
                else:
                    temp_quantity = int(self.quantity[i])
                    if temp_quantity < 1:
                        temp_msg = "Invalid Input XML Response: Error in Quantity"
                        print temp_msg 
                        break
                    else:
                        temp_msg = "Part Number and Quantity are good."
                        break
                
        return temp_msg
    
        
    
        
    def part_number_checking(self):
        
        temp_length = len(mock_data.part_number)
        
        for i in range(0, temp_length):
            if self.part_number in mock_data.part_number[i]:
                msg = mock_data.part_number_msg[i]
                
            else:
                msg = "invalid part"
                
            return msg
        
class delivery_address:
    
    def __init__(self, name, address, city, province, postalCode):
        self.name = name
        self.address = address
        self.city = city 
        self.province = province
        self.postalCode = postalCode
        
    def validate_delivery(self):
        
        temp_delivery_details = [self.name, self.address, self.city, self.province, self.postalCode]
        
        temp_msg = ""
        for elem in range(0, len(temp_delivery_details)):
            if temp_delivery_details[elem] is None:
                temp_msg = "Invalid Input XML Response: Error in Delivery Details"
                print temp_msg
            else:
                temp_msg = "Delivery Details are good"
                
        return temp_msg

    
