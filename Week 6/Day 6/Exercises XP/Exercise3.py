brand = {
  "name": "Zara",
  "creation_date": 1975 ,
  "creator_name": "Amancio Ortega Gaona" ,
  "type_of_clothes": "men, women, children, home",
  "international_competitors": "Gap, H&M, Benetton" ,
  "number_stores": 7000 ,
  "major_color":
        {"France": "blue",
        "Spain": "red",
        "US": "pink, green",}
}
brand["number_stores"]=2
print("Zara's client are: "+brand["type_of_clothes"]+"s")
brand["country_creation"]="Spain"
if "international_competitors" in brand:
    brand["international_competitors"]=brand["international_competitors"]+", Desigual"
brand.pop("creation_date")
last_international_competitor=brand["international_competitors"].split(", ")
print(last_international_competitor[len(last_international_competitor)-1])
print(brand["major_color"]["US"])
print(len(brand))
more_on_zara  = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?
# Because the brand dictionary already had a 'number_store' key,when we used the method update() to add a 'number_stores' key,it just update the existing value.
print(brand["number_stores"])