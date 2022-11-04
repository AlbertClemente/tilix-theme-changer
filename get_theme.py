import json

import runcmd as cmd

def get_theme():
  # Function to get and install desired theme into Tilix terminal.

  file = open("themes.json", "r");
  themes = json.loads(file.read())

  print("\nEstos son los temas disponibles que hay para Tillix ahora mismo:\n")

  for theme in themes:
    print(theme[1][0] + " - comando: " + theme[0])
  
  theme_option = input("\n\nQué tema quieres aplicar? Introduce el comando asociado: ")

  for theme in themes:
    if theme_option == theme[0]:
      print('Ok! Descargando el tema...')
      theme_command = theme[1][1]
      # print(theme_command)
      cmd.runcmd("sudo --preserve-env " + theme_command, verbose=True)
      
      print("Tema añadido a Tilix.")