"Exercicios para associação entre classes de objetos"
from classes_associadas import Escritor
from classes_associadas import Caneta
from classes_associadas import MaquinaEscrever


#instanciando os objetos
escritor = Escritor('mario')
caneta = Caneta('bic')
maquina = MaquinaEscrever('tauner')

#invocando os metodos
escritor.ferramenta = caneta
print(f"{escritor.nome} está usando uma {escritor.ferramenta.caneta} para escrever.")
escritor.ferramenta.escrever()

# Mudando a ferramenta para máquina de escrever
escritor.ferramenta = maquina
print(f"{escritor.nome} está usando uma máquina de marca {escritor.ferramenta.maquinaEscrever} para escrever.")
escritor.ferramenta.escrever()