# create a product and price for three items



product1_name, product1_price ='website development', 99
product2_name, product2_price = 'AWS Cloud Services', 300
product3_name, product3_price = 'Domain', 20


# create a company name and information
company_name ='Highdrone Technical Services. Inc'
company_address = '478 San Francisco, USA'
company_phone = 96381216197  

# declare ending messages
message = '*Thanks for shopping with us visit agian*'

# print top border
print('*' *55)

# print comany infromation using format
print('\t\t{}'.format(company_name))
print('\t\t{}'.format(company_address))

# print line between sections

print('=' *55)

#print the section of items

print('\tProduct Name\t\tProduct Price ')

#create a print statemet for each item
print('\t{}\t${}'.format(product1_name, product1_price))
print('\t{}\t${}'.format(product2_name, product2_price))
print('\t{}\t\t\t${}'.format(product3_name, product3_price))

print('=' *55)

# print header total

print('\t\t\t\tTotal')

# calculate total price and print out

total = product1_price + product2_price + product3_price
print('\t\t\t\t${}'.format(total))

# print a line after the total
print('=' *55)

# print thank you message
print('\t{}'.format(message))

#print end line
print('*' *55)
