# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }
# print(rick_dict.items())
# print(rick_dict.keys())
# print(rick_dict.values())

# for k,v in rick_dict.items():
#     print(f'the key is {k} the value is {v}')


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
for key in keys_to_remove:
    del sample_dict[key]
print(sample_dict)