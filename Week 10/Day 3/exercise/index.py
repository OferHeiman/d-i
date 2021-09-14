import json

json_file = 'GIT\Week 10\Day 3\exercise\cfile.json'
with open(json_file, 'r+') as file_obj:
  family = json.load(file_obj)
  for child in family['children']:
      print(f'the name of the child is {child["firstName"]} and the age is {child["age"]}')
      child['favoriteColor'] = 'red'
      file_obj.flush()
      file_obj.seek(0)
      json.dump(family,file_obj,indent= 2)

