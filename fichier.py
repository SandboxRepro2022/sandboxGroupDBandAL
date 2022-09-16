
import requests
URL = "https://www.data.gouv.fr/fr/datasets/r/dc7663c7-5da9-4765-a98b-ba4bc9de9079"
  
file = requests.get(URL, stream = True)
  
with open("covid_data.txt","wb") as pdf:
    for chunk in file.iter_content(chunk_size=1024):
  
         if chunk:
             pdf.write(chunk)
