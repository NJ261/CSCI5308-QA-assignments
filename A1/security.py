import mock_data

class security:
    
    def __init__(self, dealerId, dealerAccessKey):
        self.dealerId = dealerId
        self.dealerAccessKey = dealerAccessKey
        
    def authenticate(self):
        
        temp_length = len(mock_data.dealer_list)
        
        for i in range(0, temp_length):
            if self.dealerId in mock_data.dealer_list[i]:
                if self.dealerAccessKey in mock_data.dealer_key[i]:
                    msg = "dealer authenticated"
            else:
                msg = "dealer not authorized"
                
        return msg
