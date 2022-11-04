import requests
from bs4 import BeautifulSoup
import json

def update_theme_list():
  # Function to scrap all the themes available and store them locally in a json file.

  URL = "https://github.com/storm119/Tilix-Themes/blob/master/Themes.md"
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")

  #Container principal
  results = soup.find(id="readme")

  table_rows = results.find_all("tr")

  themes = []

  for table_row in table_rows:
    style_name = table_row.find("strong")
    style_code_installer = table_row.find("code")

    theme_name = style_name.text.strip()
    command_theme_name = theme_name.lower().replace(" ", "_")
    command_theme = style_code_installer.text.strip()

    
    themeItem = [command_theme_name, [theme_name, command_theme]]
    themes.append(themeItem)

    with open("themes.json", "w") as outfile:
      json.dump(themes, outfile)

  print("Listado de temas actualizado.")