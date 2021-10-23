import requests
import json

pincode = input("Enter the pincode of the area : ")
date = input("Enter the date to get vaccinate (dd-mm-yyyy): ")

url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'
response = requests.get(url)
print(f"Status Code : {response.status_code}")

response_dict = response.json()
vacc_dicts = response_dict['sessions']

filename = 'vaccine_info.json'
with open(filename, 'w') as file:
    json.dump(response_dict, file, indent=4)

if vacc_dicts:
    vacc_info_dicts = []
    for vacc_dict in vacc_dicts:
        if vacc_dict['fee_type'] == 'Paid':
            fee = vacc_dict['fee']
        else:
            fee = 'Free'

        vacc_info = {
            'center_name': vacc_dict['name'],
            'address': f"{vacc_dict['address']}, {vacc_dict['district_name']}, {vacc_dict['state_name']}",
            'vacc_name': vacc_dict['vaccine'],
            'total_capacity': vacc_dict['available_capacity'],
            'capacity_dose1': vacc_dict['available_capacity_dose1'],
            'capacity_dose2': vacc_dict['available_capacity_dose2'],
            'fees': fee,
        }
        vacc_info_dicts.append(vacc_info)

    for info in vacc_info_dicts:
        print(f"\nCenter Name : {info['center_name']}")
        print(f"Address : {info['address']}")
        print(f"Total Capacity : {info['total_capacity']}")
        print(f"Dose1 : {info['capacity_dose1']}")
        print(f"Dose2 : {info['capacity_dose2']}")
        print(f"Price : {info['fees']}")

else:
    print("Vaccination Closed")