print("-----Ejercicio 12: Gestión de biblioteca-----")

libros = ["Cien años de soledad", "El principito", "1984"]
autores = ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell"]

if "1984" in libros:
    libros.append("Fahrenheit 451")
if "George Orwell" in autores:
    autores.append("Ray Bradbury")
if "El principito" in libros:
    libros.remove("El principito")
if len(autores) > 3:
    autores.remove(autores[0])
if "Cien años de soledad" in libros:
    libros.remove("Cien años de soledad")
    libros.append("Crónica de una muerte anunciada")


destacados=[libros[0], libros[1]]
autores_vivos=[autores[-1], autores[-2]]

libro_destacado = []
if "Ray Bradbury" in autores_vivos:
    libro_destacado=["Fahrenheit 451","Ray Bradbury"]
    
if "Crónica de una muerte anunciada" in autores_vivos:
    autores_vivos.append("Premio Nobel")

if "Premio Nobel" in destacados:
    registro={
        "título": "Crónica de una muerte anunciada",
        "autor": "Gabriel García Márquez",
        "disponible": True
    }


registro = {}
if "registro" in locals():
    registro["Ubicación"] = "estantería 3"
if "Don quijote" not in libros:
    libros.append("Don Quijote")
if "El principito" not in libros:
    libros.append("El principito")

print(libros, autores, destacados, autores_vivos, libro_destacado, registro)

    


    