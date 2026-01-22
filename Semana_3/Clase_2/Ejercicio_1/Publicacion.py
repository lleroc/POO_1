class Publicacion:
    def __init__(self, titulo:str = None, autor:str = None, anio_publicacion:int = None):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.lista_publicaciones = []

    def descripcion(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.anio_publicacion}"
    
    def __str__(self):
        return self.descripcion()
    
    def agregar_publicacion(self, publicacion):
        self.lista_publicaciones.append(publicacion)
    
    def listar_publicaciones(self):
        numeracion = 1
        for publicacion in self.lista_publicaciones:
            print(f"------------{numeracion}-----------")
            print(f"Ttitulo: {publicacion.titulo}")
            print(f"Autor: {publicacion.autor}")
            print(f"Año de Publicación: {publicacion.anio_publicacion}")
            print("---------------------------")
            numeracion += 1
    
    def lista_horizontal(self):
        indice = 1
        for publicacion in self.lista_publicaciones:
            print(f"Indice: {indice} - Titulo: {publicacion.titulo} - Autor: {publicacion.autor} - Año: {publicacion.anio_publicacion}")
            indice += 1
    
    def editar_publicacion(self, indice, titulo=None, autor=None, anio_publicacion=None):
        if indice < 0 or indice >= len(self.lista_publicaciones):
           print("No existe una publicación con ese índice.")
           return
        pub = self.lista_publicaciones[indice]
        if titulo:
             pub.titulo = titulo
        if autor:
             pub.autor = autor
        if anio_publicacion:
             pub.anio_publicacion = anio_publicacion
        print("Publicación actualizada exitosamente.")

    def eliminar_publicacion(self, indice):
        if indice < 0 or indice >= len(self.lista_publicaciones):
            print("No existe una publicación con ese índice.")
            return
        del self.lista_publicaciones[indice]
        print("Publicación eliminada exitosamente.")