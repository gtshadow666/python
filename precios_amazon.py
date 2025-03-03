import requests
from bs4 import BeautifulSoup

precio_desado= 1.8
# URL del producto en Amazon
url = ""

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
