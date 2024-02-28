class Nodo:
    
    #Constructor de la clase Nodo
    
    def __init__( self , valor ):
        self.data = valor
        self.siguiente = None
    
class ListaSE:
    
    def __init__(self):
        self.cabeza = None
        
    def AgregarNodoInicio( self , valor) :
        #Primero se crea el nodo, duh, y después se comprueba si existe la cabeza o no
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else: 
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
    
    
    
    
lista_Simple = ListaSE()
lista_Simple.AgregarNodoInicio(5)
print(lista_Simple.cabeza.data)
lista_Simple.AgregarNodoInicio(8)
print(lista_Simple.cabeza.data)

 
