print("-----Ejercicio 12: Gestión de biblioteca-----")

libros = ["Cien años de soledad", "El principito", "1984"]
autores = ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell"]

if "1984" in libros:
    libros.append("Fahrenheit 451")
    print(libros )
elif "George Orwell" in autores:
    autores.append("Ray Bradbury")
    print(libros)
elif "El principito" in libros:
    libros.remove("El principito")
    print(libros)
elif autores.len() > 3:
    autores.remove(autores[0])
    print(autores)
elif "Cien años de soledad" in libros:
    libros.remove("Cien años de soledad")
    libros.append("Crónica de una muerte anunciada")
    print(libros)
else:
    print(" ")

destacados=[libros[0], libros[1]]
autores_vivos=[autores[-1], autores[-2]]
print(destacados, autores_vivos)

libro_destacado = []
if "Ray Bradbury" in autores_vivos:
    libro_destacado=["Fahrenheit 451","Ray Bradbury"]
    print(libro_destacado)
elif "Crónica de una muerte anunciada" in autores_vivos:
    autores_vivos.append("Premio Nobel")
    print(autores_vivos)
elif "Premio Nobel" in destacados:
    registro={
        "título": "Crónica de una muerte anunciada",
        "autor": "Gabriel García Márquez",
        "disponible": True
    }
    print(registro)
else:
    print(" ")

registro = {}
if "registro" in locals():
    registro["Ubicación"] = "estantería 3"
    print(registro)
elif "Don quijote" not in libros:
    libros.append("Don Quijote")
    print(libros)
elif "El principito" not in libros:
    libros.append("El principito")
    print(libros)

print(libros, autores, destacados, autores_vivos, libro_destacado, registro)

    


    