import xml.etree.ElementTree as ET
import security
import part_manager

tree = ET.parse('in_order.xml')
root = tree.getroot()

main_tag = []
dealer_tag = []
order_part_number = []
order_quantity = []
delivery_add_tag = []

# ---------- input XML reading -------------
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

# ---------- Writing output XML -------------
        
# writing XML: dealer not authorized XML
def not_authorized_XML():
    
    order = ET.Element("order")
    result = ET.SubElement(order, "result").text = "failure"
    error = ET.SubElement(order, "error"). text = "Not authorized"
    
    tree = ET.ElementTree(order)
    tree.write("output.xml")
    
# writing XML: invalid input XML response
def invalid_response_XML(error_msg):
    
    order = ET.Element("order")
    result = ET.SubElement(order, "result").text = "failure"
    error = ET.SubElement(order, "error"). text = "Invalid Order"
    errormessage = ET.SubElement(order, "errormessage"). text = error_msg
    
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
            


sec = security.Security(dealer_tag[0], dealer_tag[1])
part_manage = part_manager.Part_Manager(order_part_number, order_quantity)
delivery_details = part_manager.delivery_address(delivery_add_tag[0], delivery_add_tag[1],
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
            dealer_auth = sec.authenticate()
            
            # Dealer authentication with provided dealer id and access key
            if len(dealer_auth) < 21:
                part_check = part_manage.part_number_checking()
                
                if len(part_check) < 8:
                    # writing successful XML response 
                    authorized_response_XML(part_check)
                    
            else:
                # writing Fault XML Response: Dealer is not authorized
                not_authorized_XML()    
                
        else:
            # writing Fault XML response: Delivery details
            invalid_response_XML(delivery_details_validation)   
            
    else:
        # writing Fault XML response: Part number and quantity
        invalid_response_XML(parts_validation)      
        
else:
    # writing Fault XML Response: Dealer ID or Access key
    invalid_response_XML(dealer_validate)       


""" REFERENCES:
    1. https://docs.python.org/2/library/xml.etree.elementtree.html
    """
    
