public class alumnos
{
    private string nombre;

    public alumnos(string nombre)
    {
        this.nombre = nombre;
    }
}

class curso
{
   private string nombre;

    public curso(string nombre)
    {
        this.nombre = nombre;
    }
}


class program(alumnos, curso)
{
    static void Main(string[] args)
    {
        alumnos alumno1 = new alumnos("Juan Perez");
        curso curso1 = new curso("Matemáticas");
    }
}