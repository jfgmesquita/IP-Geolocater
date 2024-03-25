import requests, streamlit, pandas, ipaddress

streamlit.set_page_config(page_title = "Geolocalização de IP's")
streamlit.write("# Geolocalização de IP's")

with streamlit.form(key = "Qualquer coisa"):
    user_input = streamlit.text_input("Introduza o IP a localizar:")
    submit_button = streamlit.form_submit_button(label = "Submeter")
    if submit_button == True:
        try:
            ipaddress.ip_address(user_input)
            output = "O IP introduzido foi " + user_input
            streamlit.write(output)

            info_ip = requests.get(f"https://ipinfo.io/{user_input}/json")

            latitude = info_ip.json()["loc"].split(",")[0]
            longitude = info_ip.json()["loc"].split(",")[1]

            info_meteo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")

            ip = info_ip.json()["ip"]

            streamlit.write("## Veja abaixo a localização do IP introduzido.")
            data = pandas.DataFrame ({"latitude": [float(latitude)], "longitude": [float(longitude)]})

            streamlit.map(data,use_container_width = True)
        except:
            streamlit.write("O formato de IP introduzido é inválido.")

# Se necessário, escrever separadamente no terminal: pip install requests, pip install streamlit, pip install pandas, pip install ipadress
# Caso o ficheiro se localize no OneDrive, não esquercer de pôr o seu caminho entre aspas no comando para ver o programa Streamlit no browser.
