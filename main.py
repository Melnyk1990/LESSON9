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

#################################################################################################################################
###########################################################################################################################
print('*'*10, 'TASK 3', 10*'*')
valid_email=[]
not_valid_email = []
print()
dok_info = ['@gmail.com', '123fAAsf8@gmail.com', 'hello_world@gmail.com', 'lucky_strike@gmail.com', 'Ivanov',
            'Petrov', 'Sidorov', '95-20-07', '64-01-09', '61-21-0', 'Ivanov', 'Petrov', 'Sidorov']

for email in dok_info:
    min_len_email =15
    max_len_email =26
    if re.findall(r'[0-9A-Za-z]+[-+_.]?@[a-z]+[.][a-z]{2,3}$', email) and min_len_email<len(email)<max_len_email:
        valid_email.append(email)
    else:
        not_valid_email.append(email)

print(f'checklist: {dok_info}')
print()
print(f'Valid email: {valid_email}')
print('Quantity that does not match the request: ', len(not_valid_email))



############################################################################################################
#########################################################################################################
print('*'*10, 'TASK 4', 10*'*')
valid_full_name= []
not_valid_full_name = []

list_full_name =['Иванов, валентин Егорович', 'петров степан петрович', 'Сидорова Василиса Евгеневна', 'Sidorova Vasilisa Evgenevna', 'Кнопкин Вячеслав Анатольевич', 'Корягин В.С.', 'Кнопкин В а']

for item in list_full_name:
    if re.findall(r'^[А-ЯA-Z]{1}[а-яa-z]{2,20}\s[А-ЯA-Z]{1}[а-яa-z]{2,20}\s[А-ЯA-Z]{1}[а-яa-z]{2,20}$', item):
        valid_full_name.append(item)
    else:
        not_valid_full_name.append(item)

print(f'checklist: {list_full_name}')
print()
print(f'Valid email: {valid_full_name}')
print('Quantity that does not match the request: ', len(not_valid_full_name))
