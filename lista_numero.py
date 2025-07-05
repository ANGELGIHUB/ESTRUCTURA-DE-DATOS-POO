class lista_numeros:
    def __init__(self):
        self.lista_numero=[]
        
    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        
    def ingresar_datos_nuevos(self, otra_lista: list):
        self.lista_numero.extend(otra_lista)
        
    def insertar_datos(self, posicion: int, valor):
        self.lista_numero.insert(posicion, valor)
        
    def usuario_ve_numero(self):
        print("EL NUMERO A VER ES", self. lista_numeros)