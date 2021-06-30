import requests
import json
from requests.structures import CaseInsensitiveDict

url = "https://aplicaciones007.jne.gob.pe/srop_publico/Consulta/api/AfiliadoApi/GetNombresCiudadano"
headers = CaseInsensitiveDict()
headers["Host"] = "aplicaciones007.jne.gob.pe"
headers["Connection"] = "keep-alive"
headers["Content-Length"] = "21"
headers["X-KL-Ajax-Request"] = "Ajax_Request"
headers["RequestVerificationToken"] = "fwdtjDD8S5rdCqB65WheV5nbNVrghtbNdZfNAs_ZxeZoXYYYXWIS6c2mYw94LEnTLZthuuGnojzaRlsZRfrh262Yr8GP1bdvHpbnQ53aBxw1:OEARHueJ8wgorGwXhGj2E-Z2kjn8fajLNi9ujxVGjueNG6qXUoLeWjAtbSnLqnAqaZ8vP8oInf4yHKiJx09zQN2Nin55t4yuSEplANr3LSU1"
headers["sec-ch-ua-mobile"] = "?0"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
headers["Content-Type"] = "application/json"
headers["Accept"] = "*/*"
headers["X-Requested-With"] = "XMLHttpRequest"
headers["Origin"] = "https://aplicaciones007.jne.gob.pe"
headers["Sec-Fetch-Site"] = "same-origin"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Dest"] = "empty"
headers["Referer"] = "https://aplicaciones007.jne.gob.pe/srop_publico/Consulta/Afiliado"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Accept-Language"] = "es-ES,es;q=0.9"
headers["Cookie"] = "_ga=GA1.3.1630701290.1622671709; visid_incap_2499388=YIjcE/uvTVan2seh56g9FBQH3GAAAAAAQUIPAAAAAAAbZZNOskz+b0EiWRG1Y6Kv; incap_ses_1374_2499388=EmlfT0d0wyWv3H1Y6W0RExQH3GAAAAAAT9iddkxjDtunhMh6eOxmjw==; _gid=GA1.3.675933546.1625032471; _gat=1; _gat_dretTracker=1; ASP.NET_SessionId=enczuu0oc2w4fuqr5gg3r4sw"

#filepath = sys.argv[1]
filepath = "dnis.txt"
print("DNI,APELLIDOS Y NOMBRES")

with open(filepath, "r", encoding="latin-1") as file:
    for line in file:
        dni = line.replace('\n', '').replace('\r', '')
        data = '{"CODDNI":"' + dni + '"}'
        resp = requests.post(url, headers=headers, data=data)
        x = json.loads(resp.text)
        y = x["data"].replace("|", " ")
        z = dni + ","  + y
        print(z)
			
			
