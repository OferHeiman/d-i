import requests

def load_time(website):
    response = requests.get(website)
    return response.elapsed


# website = input("Please enter a website URL: ")
# print(f"The webpage loaded in {load_time(website)} seconds")
print(f"Ynet loaded in {load_time('https://www.ynet.co.il/home/0,7340,L-8,00.html')} seconds")
print(f"Google loaded in {load_time('https://www.google.com/')} seconds")
print(f"imdb loaded in {load_time('https://www.imdb.com/')} seconds")
print(f"Stackoverflow loaded in {load_time('https://stackoverflow.com/')} seconds")

