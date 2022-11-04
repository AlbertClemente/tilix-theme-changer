import update_theme
import get_theme


option_prompt = input('Entra "1" para actualizar listado o "2" para aplicar el tema. Introduce "0" para salir: ')


if option_prompt == "1":
  update_theme.update_theme_list()
elif option_prompt == "2":
  get_theme.get_theme()
      