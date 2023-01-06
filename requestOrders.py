# Notes
# Replace Staging URL with Prod URL
# Replace Staging API key with Prod API key
# Change "VI" to "VIC" in Production env

import json
import requests
import csv

# Staging URL
# url = "https://sofia-stage.dnagenotek.com/api/v2/orders"

# Production URL
url = "https://sofia.dnagenotek.com/api/v2/orders"

# Replace the username with the API key
# username = "" #staging API key
# username = ""  #Production API key

# Leave the password empty
password = ""

filename = 'csv_files/labels_header_final.csv'
replace_array = []
with open(filename, mode='r') as csvfile:
  datareader = csv.reader(csvfile)
  for row in datareader:
    new_dict={
                    "sample_id": row[0],    
                    "label_line_1": "",   
                    "label_line_2": ""    
                  }   
    replace_array.append(new_dict)    
    
replace_array_count=(len(replace_array))    

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
              "address_1": "99 Commercial Rd, Alfred Centre 6th Floor",
              "address_2": "",
              "city": "Melbourne",
              "region": "VIC", #Change to "VIC" for Production
              "country": "AU",
              "postal_code": "3004 "
            },
            "items": [
              {
                "sku": "8011",
                "quantity": len(value)
              }
            ],
            "labels": value,
            "customer_id": ""
          }

  # print(json.dumps(data))   
  response = requests.post(url, auth=(username, password),json=data)
  print(response.status_code)
  print(response.json())