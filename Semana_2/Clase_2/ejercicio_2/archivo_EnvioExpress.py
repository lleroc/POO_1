from archivo_envio import clase_envio

class EnvioExpress(clase_envio):
    def __init__(self, peso:float, recargo_fijo:float=20):
        super().__init__(peso)
        self.recargo_fijo = recargo_fijo
    
    def calcular_costo(self, distancia:float | None = None):
        costo_base  = super().calcular_costo()
        if distancia is None:
            return costo_base + self.recargo_fijo
        
        if distancia <0:
            raise ValueError("La distancia no puede ser negativa")
        
        return costo_base + self.recargo_fijo + (distancia * 2)


