from controller.menu import *
from config.app import *
from controller.function import *
if __name__ == "__main__":
    app=App('./proyecto/Base_de_Datos.db')
    menu(app)