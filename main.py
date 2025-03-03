import requests
from bs4 import BeautifulSoup

precio_desado= 1.8
# URL del producto en Amazon
url = "https://www.amazon.es/Liderpapel-BIC-Evolution-HB-irrompible/dp/B00008D0TS?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2O043KZE3V4HQ&dib=eyJ2IjoiMSJ9.5UumaRJdeIua9qm1VXpd85NV2nGOD5y_a2BnzV90JREd6r8hPWGDnag0sagaApEt5D0mL9iiEO_q_YYZSunAFUeZyVrnTMQtvsXgXzfFyzWCooAhPgTGZmGmihTbor9JmgMLbRpwpAUYiMF8nEK_NuiwpkIPATc_U4rzGu6feuhYRtggCq8xQLXqwEdwEd8hAMt1lCnC7KM-NxTTIIxRbHYZYZJPgMLXqY8nvVMpKc0FhxJxNQ4a_Fr2Seid01s-O5uoWJfOovdNg9_PGHUPs4pxD_npr2pcOY2Tds61t-4.snzFD5lXcbowrLVtvD1I3kg7vpsX4GpSPPD1MqNRDSw&dib_tag=se&keywords=lapiz&qid=1740997506&sprefix=lapiz%2Caps%2C139&sr=8-5"

# Cabecera para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Hacer la solicitud
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Buscar el precio en la página
price = soup.find("span", {"class": "a-offscreen"})  # Puede cambiar con el tiempo
if price:
    precio_str = price.text.strip().replace('$', '').replace(',', '.').replace('€','')  # Ajusta según la moneda (por ejemplo, '$' para USD)
    precio_float = float(precio_str)
    if precio_float <= precio_desado:
        print(f"El articulo vale {price.text} teniendo un precio deseado o inferior")
    else:
        print("Espere unos dias a que baje el precio para comprarlo")
else:
    print("❌ No se pudo obtener el precio.")
