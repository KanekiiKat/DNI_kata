class AsignadorCaracter:
    
    TABLA_ASIGNACIONES = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 
                        'B', 'N', 'J','Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    
    @classmethod
    def get_tabla(cls):
        return cls.TABLA_ASIGNACIONES
    
    @classmethod
    def obtener_letra(cls, dni:str):
        cls.TABLA_ASIGNACIONES[int(dni[:-1]) % (len(cls.TABLA_ASIGNACIONES) + 1)]
    
    @classmethod
    def es_letra_correcta(cls, dni:str):
        return cls.obtener_letra() == dni[-1]

    def __repr__(self):
        return "".join(self.get_tabla())