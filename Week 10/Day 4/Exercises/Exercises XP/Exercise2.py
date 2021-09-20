import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_dict = json.loads(sampleJson)
print(f"The Salary is: {json_dict['company']['employee']['payable']['salary']}")
json_dict['company']['employee']['birth_date'] = '1996'
sampleJson = json.dumps(json_dict)
print(sampleJson)
json_file = "sampleJson.json"
with open(json_file, 'w') as file_obj:
    json.dump(sampleJson, file_obj)