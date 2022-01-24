# Desafio 9.2 Calculadora
#
# Classe Calculadora que contém os seguintes métodos:
# - somar - subtrair - multiplicar - dividir
#
# PS: Esses métodos funcionam apenas com dois números
#
# PS2: Todos os métodos retornam o valor
#
#  A classe também contém as propriedades (atributos):
# - primeiro_valor - segundo_valor
# 
# PS3: Os valores são passados em parâmetro
# 
# PS4: Os valores vão ser lidos do usuário (input)

class Calculadora(object):
    def somar(self, primeiro_n, segundo_n):
        return primeiro_n + segundo_n
        
    def subtrair(self, primeiro_n, segundo_n):
        return primeiro_n - segundo_n
        
    def multiplicar(self, primeiro_n, segundo_n):
        return primeiro_n * segundo_n
        
    def dividir(self, primeiro_n, segundo_n):
        return primeiro_n / segundo_n
        
calc = Calculadora()