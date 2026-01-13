from clase_estudiante import Estudiante

def main():
    est1 = Estudiante("Juan", "Ingeniería")
    est2 = Estudiante("María", "Medicina")
    est3 = Estudiante("Luis", "Derecho")

    print(est1.saludar())
    est1.estudiar()

    print(est2.saludar())
    est2.estudiar()
    
    print(est3.saludar())   
    est3.estudiar()

if __name__ == "__main__":
    main()