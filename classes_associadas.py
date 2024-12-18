class Escritor:
    def __init__(self,nome): #a class construtor esta gerando um set de apenas um nome
        self.__nome = nome 
        self.__ferramenta = None #o atributo ferramenta foi gerado apena com none no modo construtos
    
    @property
    def nome(self):#um getter para retornar um nome 'private'
        return self.__nome
               
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self.__ferramenta = ferramenta# uma ferramenta sera setada em 'Escritor'

class Caneta:
    def __init__(self,marca):
        self.__marca = marca #atributo privado

    @property
    def caneta(self):
        return (f'Caneta {self.__marca}') #getter para assessar ao atributo
    
    #metodos da caneta
    def escrever(self):
        print(' o escritor esta escrevendo com a canenta')#ação para a caneta

class MaquinaEscrever:
    def __init__(self, marca):
        self.__marca = marca

    @property #propiedade de encapsulamento
    def maquinaEscrever(self):
        return self.__marca

    #metodos da maquina
    def escrever(self):
        print(' o escritor esta escrevendo com a maquina de escrever')