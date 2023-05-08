class Registro:
    __Temperatura = float
    __Humedad = 0
    __Presion = 0

    def __init__(self, Temperatura=0.0, Humedad=0, Presion=0):
        self.__Temperatura = float(Temperatura)
        self.__Humedad = int(Humedad)
        self.__Presion = int(Presion)

    def mostrarDatos(self):
        print(' {}        {}         {} '.format(self.__Temperatura, self.__Humedad, self.__Presion))


    def getTemperatura(self):
        return self.__Temperatura

    def getHumedad(self):
        return self.__Humedad

    def getPresion(self):
        return self.__Presion
    def tempmax(self,Lista,horas,dias):
        maximo=-999.99
        for dias in range(len(Lista)):
            for horas in range(len(Lista[dias])):
                if type(Lista[dias][horas])==Registro:
                    var=Lista[dias][horas].getTemperatura()
                    if var>maximo:
                        maximo=Lista[dias][horas].getTemperatura()
                        d = dias
                        h = horas+1
        print('Temperatura maxima: {} a la hora: {} del dia: {}'.format(maximo,d,h))

    def tempmin(self,Lista,horas,dias):
        minimo=50.0
        for dias in range(len(Lista)):
            for horas in range(len(Lista[dias])):
                if type(Lista[dias][horas])==Registro:
                    var=Lista[dias][horas].getTemperatura()
                    if var<minimo:
                        minimo=Lista[dias][horas].getTemperatura()
                        d = dias
                        h = horas+1
        print('Temperatura minima: {} a la hora: {} del dia: {}'.format(minimo,d,h))
