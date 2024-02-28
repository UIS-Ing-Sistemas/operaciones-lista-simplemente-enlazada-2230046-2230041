class Nodo:

#CONSTRUCTOR DE LA CLASE NODO
        
    def __init__( self , valor ):
        self.data = valor
        self.siguiente = None
    

class ListaSE:

#CONSTRUCTOR DE LA CLASE LISTASE
    
    def __init__(self):
        self.cabeza = None

# MÉTODO PARA AGREGAR UN NODO AL INICIO
        
    def AgregarNodoInicio( self , valor) :
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else: 
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

# MÉTODO PARA AGREGAR UN NODO AL FINAL DE LA LISTA
            
    def  AgregarNodoFinal(self , valor):
        
        nuevo_nodo = Nodo(valor)
        nodo_sustituto = self.cabeza

        if self.cabeza != None :
            
            if nodo_sustituto.siguiente != None:
                while nodo_sustituto.siguiente != None:
                    nodo_sustituto = nodo_sustituto.siguiente
                 
                nodo_sustituto.siguiente = nuevo_nodo
            else:
                self.cabeza.siguiente = nuevo_nodo
                
        else:
            self.cabeza = nuevo_nodo
            
    
#MÉTODO PARA ELIMINAR EL PRIMER ELEMENTO DE LA LISTA
                     
    def EliminarPrimero(self):
        nodo_repuesto = self.cabeza

        if self.cabeza != None:
            self.cabeza = self.cabeza.siguiente
        
        if   nodo_repuesto.siguiente == None:
            self.cabeza = None
            
        
#MÉTODO PARA ELIMINAR EL ÚLTIMO ELEMENTO DE LA LISTA
            
    def EliminarUltimo(self):
        if self.cabeza != None :
            nodo_final = self.cabeza
            nodo_anterior = None

            if nodo_final.siguiente != None:
                while nodo_final.siguiente != None:
                     nodo_anterior = nodo_final
                     nodo_final = nodo_final.siguiente

                nodo_final = None 
                nodo_anterior.siguiente = None

            else:
                self.cabeza = None

#MÉTODO PARA BUSCAR UN ELEMENTO POR SU FAVOR (TRUE OR FALSE)
                
    def buscarElemento(self, valor):
        valorEncontrado = False 

        if self.cabeza != None :
            if self.cabeza.siguiente != None:

                while valorEncontrado == False:
                     if valor == self.cabeza.data:
                         valorEncontrado = True
                         
                     
                     if self.cabeza.siguiente != None:
                        self.cabeza = self.cabeza.siguiente
                     else:
                        return valorEncontrado

        return valorEncontrado

#MÉTODO PARA CONTAR LA CANTIDAD DE ELEMENTOS EN LA LISTA SE
    
    def tamañoLista(self):
         tamaño_Lista = 0

         if self.cabeza != None :
            tamaño_Lista = 1
            nodo_actual = self.cabeza
           
            while nodo_actual.siguiente != None:
                tamaño_Lista+= 1
                nodo_actual = nodo_actual.siguiente
            return tamaño_Lista
         else:
             return tamaño_Lista
    
    def  comprobar_lista_vacía(self):

        if self.cabeza == None:
            return True
        else:
            return False
    

#PROBAR LA FUNCIONALIDAD DE LOS MÉTODOS
    
lista_Simple = ListaSE()

lista_Simple.AgregarNodoFinal(2)
lista_Simple.AgregarNodoFinal(8)
lista_Simple.AgregarNodoFinal(15)

lista_Simple.EliminarPrimero()
lista_Simple.EliminarPrimero()
lista_Simple.EliminarUltimo()

print(lista_Simple.comprobar_lista_vacía())



 