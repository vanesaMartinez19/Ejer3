from claseRegistro import Registro
import os


class Menu:
    __op = int

    def __init__(self):
        self.__op = None

    def getOpcion(self):
        return self.__op

    def manejoMenu(self, op, Lista, dias, horas):
        if op == 1:
            self.opcion1(Lista, dias, horas)
        elif op == 2:
            self.opcion2(Lista, dias, horas)
        elif op == 3:
            self.opcion3(Lista, dias, horas)
        else:
            self.Salir()

    def opcion1(self, Lista, dias, horas):
        Lista[horas - 1][dias - 1].tempmax(Lista, horas, dias)
        Lista[horas - 1][dias - 1].tempmin(Lista, horas, dias)
        Lista[horas - 1][dias - 1].hummax(Lista, horas, dias)
        Lista[horas - 1][dias - 1].hummin(Lista, horas, dias)
        Lista[horas - 1][dias - 1].presmax(Lista, horas, dias)
        Lista[horas - 1][dias - 1].presmin(Lista, horas, dias)
        os.system('pause')
        os.system('cls')

    def opcion2(self, Lista, dias, horas):
        Lista[horas - 1][dias - 1].promedio(Lista, horas, dias)
        os.system('pause')
        os.system('cls')