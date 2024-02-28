class Nodo:
    
    def __init__( self , valor ):
        self.data = valor
        self.siguiente = None
    

class ListaSE:
    
    def __init__(self):
        self.cabeza = None
    def  AgregarNodoFinal(self , valor):
        
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza != None :
            nodoSustituto = self.cabeza
            
            if nodoSustituto.siguiente != None:
                while nodoSustituto.siguiente != None:
                     nodoSustituto = nodoSustituto.siguiente
                 
                nodoSustituto.siguiente = nuevo_nodo
            else:
                self.cabeza.siguiente = nuevo_nodo
                
        else:
            self.cabeza = nuevo_nodo
            
    def AgregarNodoInicio( self , valor) :
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else: 
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
    
    
    
    
lista_Simple = ListaSE()
lista_Simple.AgregarNodoInicio(1)
lista_Simple.AgregarNodoFinal(2)
lista_Simple.AgregarNodoFinal(5)
print(lista_Simple.cabeza.siguiente.siguiente.data)


 
