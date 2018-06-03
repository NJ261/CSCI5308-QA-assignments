import xml.etree.ElementTree as ET
import security
import part_manager

def input_function(file_name):
    global root
    tree = ET.parse(file_name)
    root = tree.getroot()
    main_tag_function(root)

main_tag = []
dealer_tag = []
order_part_number = []
order_quantity = []
delivery_add_tag = []


# -----------------------------------  WRITING XML OUTPUT FILE  ----------------------------------- 
def invalid_response_XML(error_msg):
    
    order = ET.Element("order")
    result = ET.SubElement(order, "result").text = "failure"
    error = ET.SubElement(order, "error"). text = "Invalid Order"
    errormessage = ET.SubElement(order, "errormessage"). text = error_msg
    
    tree = ET.ElementTree(order)
    tree.write("output.xml")
    
    
# START -----------------------------------  INPUT XML PARSING  ----------------------------------- 

def main_tag_function(root):
    
    count = 0
    for child in root:
        main_tag.append(child.tag)
        
    temp_main_tag = ['dealer','orderitems','deliveryaddress']
    
    for i in range(0, len(temp_main_tag)):
        if temp_main_tag[i] in main_tag:
            count = count + 1
        else:
            invalid_response_XML("Invalid input XML response")
            print "Invalid input XML response"
            break
        
    if count == 3:
        dealer_tag()
    else:
        invalid_response_XML("Invalid input XML response")
        print "Invalid input XML response"
    
    
def dealer_tag():  
    count = 0
    dealer_tag = [t.tag for t in root.findall('.//dealer/*')]
    temp_dealer_tag = ['dealerid','dealeraccesskey']
    
    for elem in range(0, len(temp_dealer_tag)):
        if (temp_dealer_tag[elem]) in dealer_tag:
            
            count = count + 1

        else:
            invalid_response_XML("Invalid input XML response")
            print "Invalid input XML response"
            break
        
    if count == 2:
        temp_dealer_tag = []
        for item in root.findall('dealer'):
            temp_dealer_tag.append(item.find('dealerid').text)
            temp_dealer_tag.append(item.find('dealeraccesskey').text)
        delivery_add_tag(temp_dealer_tag)
    else:
        invalid_response_XML("Invalid input XML response")
        print "Invalid input XML response"
    
    
def delivery_add_tag(temp_list):
    count = 0
    delivery_add_tag = [t.tag for t in root.findall('.//deliveryaddress/*')]
    temp_delivery_add_tag = ['name','street','city','province','postalcode']
    
    for elem in range(0, len(temp_delivery_add_tag)):
        if temp_delivery_add_tag[elem] in delivery_add_tag:
            
            count = count + 1
        else:
            invalid_response_XML("Invalid input XML response")
            print "Invalid input XML response"
            break
        
    if count == 5:
        temp_delivery_add_tag = []
        for item in root.findall('deliveryaddress'):
            temp_delivery_add_tag.append(item.find('name').text)
            temp_delivery_add_tag.append(item.find('street').text)
            temp_delivery_add_tag.append(item.find('city').text)
            temp_delivery_add_tag.append(item.find('province').text)
            temp_delivery_add_tag.append(item.find('postalcode').text)
        order_items_tag(temp_list, temp_delivery_add_tag)
    else:
        invalid_response_XML("Invalid input XML response")
        print "Invalid input XML response"
        
    
       
def order_items_tag(temp_list_dealer, temp_list_delivery):
    
    count = 0
    item_tag = [t.tag for t in root.findall('.//orderitems/*')]
    
    if len(item_tag) != 0:
        sub_item_tag = [t.tag for t in root.findall('.//item/*')]
        if (len(sub_item_tag) % 2) == 0:
            
            order_items = root.find("orderitems")
            for order in order_items.findall('item'):
                part_number = order.find('partnumber')
                quantity = order.find('quantity')
                
                if part_number.text is None:
                    print "Invalid Input XML Response Error: in Part Number"
                    invalid_response_XML("Invalid input XML response Error: in Part Number")
                    count = count + 1
                    break
                
                elif quantity.text is None:
                    print "Invalid Input XML Response Error: in Quantity"
                    invalid_response_XML("Invalid input XML response Error: in Quantity")
                    count = count + 1
                    break
                
                else:
                    order_quantity.append(quantity.text)
                    order_part_number.append(part_number.text)
                    
            if count == 0:        
                main_function(temp_list_dealer, temp_list_delivery, order_part_number, order_quantity)

        else:
            print "Invalid Input XML Response Error: in tags"
            invalid_response_XML("Invalid input XML response Error: in tags")
    else:
        print "Invalid Input XML Response Error: in tags"
        invalid_response_XML("Invalid input XML response Error: in tags")
        

# END -----------------------------------  INPUT XML PARSING  -----------------------------------         


# -----------------------------------  WRITING XML OUTPUT FILE  ----------------------------------- 
        
# writing XML: dealer not authorized XML
def not_authorized_XML():
    
    order = ET.Element("order")
    result = ET.SubElement(order, "result").text = "failure"
    error = ET.SubElement(order, "error"). text = "Not authorized"
    
    tree = ET.ElementTree(order)
    tree.write("output.xml")
    
    
# writing XML: authorized XML response
def authorized_response_XML(error_response):
    
    temp_part_length = len(order_part_number)
    
    order = ET.Element("order")
    orderitems = ET.SubElement(order, "orderitems")
    
    for i in range(0, temp_part_length):
        item = ET.SubElement(orderitems, "item")
        partnumber = ET.SubElement(item, "partnumber").text = order_part_number[i]
        quantity = ET.SubElement(item, "quantity").text = order_quantity[i]

        if error_response[i] == "success":
            result = ET.SubElement(item, "result").text = "success"
            errormessage = ET.SubElement(item, "errormessage").text = ""
        else:
            result = ET.SubElement(item, "result").text = "failure"
            errormessage = ET.SubElement(item, "errormessage").text = error_response[i]
                  
    tree = ET.ElementTree(order)
    tree.write("output.xml")
            
    
# -----------------------------------  MAIN LOGIC FUNCTION ----------------------------------- 
def main_function(dealer_tag, delivery_add_tag, order_part_number, order_quantity):
    
    sec = security.Security(dealer_tag[0], dealer_tag[1])
    part_manage = part_manager.Part_Manager(order_part_number, order_quantity)
    
    delivery_details = part_manager.DeliveryAddress(delivery_add_tag[0], delivery_add_tag[1],
                                                     delivery_add_tag[2],delivery_add_tag[3],delivery_add_tag[4])
    dealer_validate = sec.validate_dealer()
    
    # validating dealer id and access key field
    if len(dealer_validate) < 25:
        parts_validation = part_manage.validate_parts()
        
        # validating part number and quantity field
        if len(parts_validation) < 40:
            delivery_details_validation = delivery_details.validate_delivery()
            
            # validating delivery details fields such as name, address, city, province, postal code
            if len(delivery_details_validation) < 30:
                dealer_auth = sec.isDealerAuthorized()
                
                # Dealer authentication with provided dealer id and access key
                if len(dealer_auth) < 21:
                    part_check = part_manage.SubmitPartForManufactureAndDelivery()
                    
                    if len(part_check) < 8:
                        # writing successful XML response 
                        authorized_response_XML(part_check)
                        msg = "Dealer is authorized, check the response in output.xml"
                        print msg
                        
                else:
                    # writing Fault XML Response: Dealer is not authorized
                    not_authorized_XML()  
                    msg = "Dealer is not authorized"
                    
            else:
                # writing Fault XML response: Delivery details
                invalid_response_XML(delivery_details_validation)   
                msg = delivery_details_validation
                
        else:
            # writing Fault XML response: Part number and quantity
            invalid_response_XML(parts_validation) 
            msg = parts_validation
            
    else:
        # writing Fault XML Response: Dealer ID or Access key
        invalid_response_XML(dealer_validate)    
        msg = dealer_validate

    return msg 
