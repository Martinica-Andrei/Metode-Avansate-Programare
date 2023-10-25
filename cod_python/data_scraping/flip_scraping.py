import requests
from bs4 import BeautifulSoup

def extrage_informatii(url, limita=5):
    raspuns = requests.get(url)
    if raspuns.status_code == 200:
        soup = BeautifulSoup(raspuns.text, "html.parser")
        elemente_nume = soup.find_all("a", class_="font-bold d-block mt-md-2 mb-1")
        elemente_pret = soup.find_all("div", class_="real-price font-bold")
        informatii_produse = []
        index = 0
        
        for nume_element, pret_element in zip(elemente_nume, elemente_pret):
            nume = nume_element.get_text(strip=True)
            pret = pret_element.find("span").get_text(strip=True) # strip elimina spatiile g
            informatii_produse.append({"nume" : nume, "pret": pret})
            index += 1
    
            if index >= limita:
                return informatii_produse   
        return informatii_produse
    else:
        print("Cererea HTTP a esuat.Cod de stare : " + raspuns.status_code)
        return None
    
produse = extrage_informatii("https://flip.ro/magazin/apple/iphone-14/")
for p in produse:
    for k, v in p.items():
        v = v.replace(" ", "")
        v = v.replace('\n', "")
        v = ' , '.join(v.split(','))
        print(f"{k} : {v}")