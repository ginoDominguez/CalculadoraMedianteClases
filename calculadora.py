### Creacion de la clase Calculadora:

class Calculadora:
    def sumar(self, a,b):
        return a+b
    
    def restar(self, a, b):
        return a-b
    
    def multiplicar(self , a, b):
        return a*b
    
    def dividir(self, a, b):
        if b!=0:
            return a/b
        else:
            return "Error: No se puede dividir para cero"
        
        
    
    