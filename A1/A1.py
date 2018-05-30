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

