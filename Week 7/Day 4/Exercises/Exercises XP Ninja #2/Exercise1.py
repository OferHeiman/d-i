def get_full_name(first_name,last_name,middle_name=None):
    print(f"{first_name} {middle_name} {last_name}") if middle_name else print(f"{first_name} {last_name}") 

get_full_name(first_name="john", last_name="lee")
get_full_name(first_name="john", middle_name="hooker", last_name="lee")