import requests
url = "https://sofia-stage.dnagenotek.com/api/v2/orders"
username = ""
password = ""
data = {
  "destination": {
    "co_first_name": "John",
    "co_last_name": "Appleseed",
    "co_phone_number": "408-867-5309",
    "company": "ACME Corp",
    "address_1": "3000-5 Palladium Drive",
    "address_2": "",
    "city": "Ottawa",
    "region": "ON",
    "country": "CA",
    "postal_code": "K2V1C2"
  },
  "items": [
    {
      "sku": "8011",
      "quantity": 1
    }
  ],
  "labels": [
    {
      "sample_id": "AAAA20160121ZZZZ",
      "label_line_1": "",
      "label_line_2": ""
    }
  ],
  "customer_id": "",
  "service_level": "USPS First-Class Mail (Endicia)"
}
response = requests.post(url, auth=(username, password),json=data)
print(response.status_code)
print(response.json())



# import requests
# import json
 
# url = "https://sofia-stage.dnagenotek.com/api/v2/orders"
 
# # headers = {"Content-Type": "application/json; charset=utf-8"}
# headers = {"Authorization" : "Basic Snp1UEttUk9sc0M0TXZrRXdHSGl2d1Vhc3RDR3BuNVpnbDRMblQ2cFpxSDNRT3hpdU5QSWxaeWt5RXJHb0pMTzo="}
 
# data = {
#   "destination": {
#     "co_first_name": "John",
#     "co_last_name": "Appleseed",
#     "co_phone_number": "408-867-5309",
#     "company": "ACME Corp",
#     "address_1": "3000-5 Palladium Drive",
#     "address_2": "",
#     "city": "Ottawa",
#     "region": "ON",
#     "country": "CA",
#     "postal_code": "K2V1C2"
#   },
#   "items": [
#     {
#       "sku": "8011",
#       "quantity": 1
#     }
#   ],
#   "labels": [
#     {
#       "sample_id": "AAAA20160121ZZZZ",
#       "label_line_1": "1951-02-54",
#       "label_line_2": "Special instructions to be added and scanned"
#     }
#   ],
#   "customer_id": "AFW-123-340#87",
#   "service_level": "USPS First-Class Mail (Endicia)"
# }
 
# response = requests.post(url, headers=headers, json=data)
 
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())
