import mock_data

class part_manager:
    
    def __init__(self, part_number):
        self.part_number = part_number
        
    def part_number_checking(self):
        
        temp_length = len(mock_data.part_number)
        
        for i in range(0, temp_length):
            if self.part_number in mock_data.part_number[i]:
                msg = mock_data.part_number_msg[i]
                
            else:
                msg = "invalid part"
                
            return msg