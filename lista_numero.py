class lista_numeros:
    def __init__(self):
        self.numeros = []
    
    def guardar_numeros(self, dato_numeros):
        self.lista_numeros.append(dato_numeros)
        print(self.lista_numeros)


    def añadir_lista(self, dato_numeros):
        self.lista_numeros.extend(dato_numeros)
        print(self.lista_numeros)


    def insertar_numero(self, posicion, numero):
        sublista = [2, 8]
        self.lista_numeros.insert(posicion, sublista)
        print(self.lista_numeros)
        return self.lista_numeros


    def eliminar_numero(self, posicion):
        elemento_eliminado = self.lista_numeros.pop(posicion)
        print(f"Lista: {self.lista_numeros} actualizada.")
        print(f'Elemento eliminado: {elemento_eliminado} eliminado de la lista correctamente')
        return elemento_eliminado


    def mostrar_elementos(self, posicion):
        elemento = self.lista_numeros [posicion]
        print(f"Elemento en la posición {posicion}: {elemento}")
        return elemento
            

    def obtener_lista(self):
        return self.lista_numeros   
