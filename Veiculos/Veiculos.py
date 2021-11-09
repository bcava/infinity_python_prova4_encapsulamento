from datetime import datetime



class Veiculos:
    def __init__(self, tipoVeiculo, placa, modelo, data):
        self.tipoVeiculo = tipoVeiculo
        self.__placa = placa
        self.__modelo = modelo 
        self.__data = data
        self.__horEntrada = datetime.now()
          
    
    @property
    def tipoVeiculo (self):
        return self.__tipoVeiculo
    
    @tipoVeiculo.setter
    def tipoVeiculo (self, tipoVeiculo):
        self.__tipoVeiculo = tipoVeiculo  

    @property
    def placa (self):
        return self.__placa
    
    @placa.setter
    def placa (self, placa):
        self.__placa = placa  
        
    @property
    def modelo (self):
        return self.__modelo
    
    @modelo.setter
    def modelo (self, modelo):
        self.__modelo = modelo  

    @property
    def data (self):
        return self.__data
    
    @data.setter
    def data (self, data):
        self.__data = data  



    @property
    def horSaida (self):
        return self.__horSaida
    
    @horSaida.setter
    def horSaida (self, horSaida):
        self.__horSaida = horSaida



#Método
    def valorTotal (self, horSaida):
        valorPorHora = 10
        format = '%H:%M:%S'
        valorFinal = datetime.strptime(horSaida, format) - datetime.strptime(self.__horEntrada, format)
       # valorFinal = horSaida - self.__horEntrada
        return valorFinal*valorPorHora



        ###conhecer a biblioteca datime