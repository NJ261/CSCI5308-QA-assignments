import mock_data

class Security:
    
    def __init__(self, dealerId, dealerAccessKey):
        self.dealerId = dealerId
        self.dealerAccessKey = dealerAccessKey
        
    def validate_dealer(self):
        validate_msg = "Invalid Input XML Response"
        if self.dealerId is None:
            print validate_msg                # checking DEALER ID is not null
        elif self.dealerKey is None:
            print validate_msg                 # checking DEALER ACCESS KEY is not null
        else:
            validate_msg = "Dealer Authenticated"
            pass
        return validate_msg

        
    def authenticate(self):
        
        temp_length = len(mock_data.dealer_list)
        
        for i in range(0, temp_length):
            if self.dealerId in mock_data.dealer_list[i]:
                if self.dealerAccessKey in mock_data.dealer_key:
                    msg = "dealer authenticated"
                break
            else:
                msg = "dealer not authorized"
                
        return msg
