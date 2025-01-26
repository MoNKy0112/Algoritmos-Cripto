# Autor : Jonathan Moncaleano
from ui import main_menu
from console import console_menu
if __name__ == "__main__":
    # Aquí puedes agregar el código que deseas ejecutar cuando se ejecute el script
    print("Este es el punto de entrada principal del script.")
    input("Presiona [y] si quieres usar la interfaz gráfica: ")

    if input == "y":
        main_menu()
    else:
        console_menu()
