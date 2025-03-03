import requests
from bs4 import BeautifulSoup

precio_desado= 10
# URL del producto en Amazon
url = "https://www.mediamarkt.es/es/product/_raton-logitech-lift-vertical-ergonomico-inalambrico-4000-ppp-botones-personalizables-multidispositivo-windows-mac-usb-logi-bolt-negro-1532312.html"
# Cabecera para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Hacer la solicitud
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Buscar el precio en la página
price = soup.find("span", {"class": "sc-d571b66f-0 iJjLfD"})  # Puede cambiar con el tiempo los decimales los hemos quitado poara no aumentar la compeljidad asi que solo mirames las unidades del precio
if price:
    precio_str = price.text.strip().replace('$', '').replace(',', '.').replace('€','')  # Ajusta según la moneda (por ejemplo, '$' para USD)
    
    precio_float = float(precio_str)
    if precio_float <= precio_desado:
        print(f"El articulo vale {precio_float}€ teniendo un precio deseado o inferior")
    else:
        print("Espere unos dias a que baje el precio para comprarlo")
else:
    print("❌ No se pudo obtener el precio.")
