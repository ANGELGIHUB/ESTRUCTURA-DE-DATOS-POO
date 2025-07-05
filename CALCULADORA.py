class calculadora:
    def __init__(self):
        self.objlista = lista_numeros()
        self.numero1 = ""
        self.numero2 = ""
        
    def pedir_numero(self):
        numero1 = input("ingrse su numero 1")
        numero2 = input("ingrese su numero 2")
        return numero1, numero2
    
    def almacenar_numero(self):
        dato_numero = [self.numero1, self.numero2]
        self.objlista.guardar_numero(dato_numero)
        
    def insertar_valor(self):
        pos = input(())