import re
print('*'*10, 'TASK 1 and TASK 2', 10*'*')
valid_home_number=[]
not_valid_home_number = []

valid_mobile_number=[]
not_valid_mobile_number = []
dok_info = ['23-25-09', '55-12-09', '95-20-07', '64-01-09', '61-21-0', '+805552674444', '+805555741254', '380988002265',
            '+380551254444', '+805552674444', '+805555741254', '+82565454444445' '+825-654-54444445''Ivanov', 'Petrov', 'Sidorov']

for num in dok_info:
    if re.findall(r'^\d{2}-\d{2}-\d{2}$', num) and len(num)==8:
        valid_home_number.append(num)
    else:
        not_valid_home_number.append(num)
    if re.findall(r'^[+]?[380]{3}[0-9]{9}$', num) and 12<= len(num) <=13:
        valid_mobile_number.append(num)
    else:
        not_valid_mobile_number.append(num)

print(dok_info)
print()
print(f'Valid home numbers phon: {valid_home_number}')
print('Quantity does not match search: ', len(not_valid_home_number))
print()
print(f'Valid home numbers phon: {valid_mobile_number}')
print('Quantity does not match search: ', len(not_valid_mobile_number))
