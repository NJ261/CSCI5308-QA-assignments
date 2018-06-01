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
        

sec = security.Security(dealer_tag[0], dealer_tag[1])
print(sec.authenticate())

part_manage = part_manager.Part_Manager(order_part_number, order_quantity)
print(part_manage.validate_parts())

delivery_details = part_manager.delivery_address(delivery_add_tag[0], delivery_add_tag[1],
                                                 delivery_add_tag[2],delivery_add_tag[3],delivery_add_tag[4])
delivery_details.validate_delivery()  


""" REFERENCES:
    1. https://docs.python.org/2/library/xml.etree.elementtree.html
    """
    
