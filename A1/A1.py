import xml.etree.ElementTree as ET

tree = ET.parse('in_order.xml')

root = tree.getroot()

main_tag = []
dealer_tag = []
order_part_number = []
order_quantity = []
delivery_add_tag = []

# ---------- input XML reading ----------
for child in root:
    main_tag.append(child.tag)
    
for item in root.findall('dealer'):
    dealer_tag.append(item.find('dealerid').text)
    dealer_tag.append(item.find('dealeraccesskey').text)
    
for item in root.findall('deliveryaddress'):
    delivery_add_tag.append(item.find('name').text)
    delivery_add_tag.append(item.find('street').text)
    delivery_add_tag.append(item.find('city').text)
    delivery_add_tag.append(item.find('province').text)
    delivery_add_tag.append(item.find('postalcode').text)
    
order_items = root.find("orderitems")
for order in order_items.findall('item'):
    part_number = order.find('partnumber')
    quantity = order.find('quantity')
    
    if part_number.text is None or quantity.text is None :
        print "Invalid Input XML Response"
        
    else:
        order_quantity.append(quantity.text)
        order_part_number.append(part_number.text)

#if None in order_quantity or order_part_number or delivery_add_tag or dealer_tag or main_tag:
#   print "************************   Invalid input XML   ************************"
        
        

def validate_dealer(dealerId, dealerKey):
    temp = "Invalid Input XML Response"
    if dealerId is None:
        print temp                  # checking DEALER ID is not null
    elif dealerKey is None:
        print temp                  # checking DEALER ACCESS KEY is not null
    else:
        temp = "Dealer Authenticated"
        pass
    return temp

def validate_parts(part_number, quantity):
    temp = []
    temp_msg = ""
    temp_part_number = [part_number]
    temp_quantity = [quantity]
    
    for i in range(0, len(temp_part_number)):
        
        if temp_part_number[i] is None:
            temp_msg = "Invalid Input XML Response: Error in Part number"
            print temp_msg
            break
        
        else:
            temp.append(int(part_number[i]))
            temp_msg = "Part Number and Quantity are good."
            
            if temp_quantity[i] is None:
                temp_msg = "Invalid Input XML Response: Error in Quantity"
                print temp_msg
                break
                
            else:
                temp_quantity = int(quantity[i])
                if temp_quantity < 1:
                    temp_msg = "Invalid Input XML Response: Error in Quantity"
                    print temp_msg 
                    break
                else:
                    temp_msg = "Part Number and Quantity are good."
                    break
            
    return temp_msg

def validate_delivery(delivery_details):
    temp_msg = ""
    for elem in range(0, len(delivery_details)):
        if delivery_details[elem] is None:
            temp_msg = "Invalid Input XML Response: Error in Delivery Details"
            print temp_msg
        else:
            temp_msg = "Delivery Details are good"
            
    return temp_msg

        
validate_dealer(dealer_tag[0], dealer_tag[1])    
validate_parts(order_part_number, order_quantity)
validate_delivery(delivery_add_tag)


""" REFERENCES:
    1. https://docs.python.org/2/library/xml.etree.elementtree.html
    """
    
