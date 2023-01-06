import requests
import csv
url = "https://sofia-stage.dnagenotek.com/api/v2/orders"
username = ""
password = ""

filename = 'csv_files/labels_noheader.csv'
replace_array = []
with open(filename, mode='r') as csvfile:
  datareader = csv.reader(csvfile)
  current_count=0
  for row in datareader:
    # print(row)
    new_dict={
                    "sample_id": row[0],    
                    "label_line_1": "",   
                    "label_line_2": ""    
                  }   
    replace_array.append(new_dict)    
    current_count+=1
    
replace_array_count=(len(replace_array))    
# print(replace_array)



# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


# How many elements each
# list should have
n = 42
divided_replace_array = list(divide_chunks(replace_array, n))
for value in divided_replace_array:
  data = {    
            "destination": {    
              "co_first_name": "James",
              "co_last_name": "Phung",
              "co_phone_number": "6139-903-0917",
              "company": "Monash University",
              "address_1": "99 Commercial Rd",
              "address_2": "Alfred Centre 6th Floor",
              "city": "Melbourne",
              "region": "VIC",
              "country": "AUS",
              "postal_code": "3004"
            },
            "items": [
              {
                "sku": "8011",
                "quantity": len(value)
              }
            ],
            "labels": value,
            "customer_id": "",
            "service_level": "USPS First-Class Mail (Endicia)"
          }

  # print(data)   
  response = requests.post(url, auth=(username, password),json=data)
  print(response.status_code)
  print(response.json())

