from src.asignador_caracter import AsignadorCaracter

class Dni:
    
    def __init__(self, dni: str):
        self.dni = dni
        self.asignador_caracter = AsignadorCaracter
        
    def obtener_dni(self):
        return self.dni
    
    def comprobar_numero(self):
        return self.dni[:-1].isdigit()
    
    def comprobar_letra(self):
        return self.dni[-1].isalpha()
    
    def comprobar_dni(self):
        return Dni.comprobar_letra(self) and Dni.comprobar_numero(self)
    
    def validar_dni(self):
        if Dni.comprobar_dni:
            return self.dni[:-1] + str(self.asignador_caracter.obtener_letra(self.dni)) == str(Dni.obtener_dni(self))
        
    def __repr__(self):
        return "".join(self.obtener_dni())
            