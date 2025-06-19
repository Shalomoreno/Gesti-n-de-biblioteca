print("-----Ejercicio 12: Gestión de biblioteca-----")

libros = ["Cien años de soledad", "El principito", "1984"]
autores = ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell"]

if "1984" in libros:
    libros.append("Fahrenheit 451")
else:
    print("El libro '1984' no está en la lista.")

if "George Orwell" in autores:
    autores.append("Ray Bradbury")
else:
    print("El autor 'George Orwell' no está en la lista.")

if "El principito" in libros:
    libros.remove("El principito")
else:
    print("El libro 'El principito' no está en la lista.")    

if len(autores) > 3:
    autores.remove(autores[0])
else:
    print("No hay suficientes autores para eliminar.")

if "Cien años de soledad" in libros:
    libros.remove("Cien años de soledad")
    libros.append("Crónica de una muerte anunciada")
else:
    print("El libro 'Cien años de soledad' no está en la lista.")


destacados=[libros[0], libros[1]]
autores_vivos=[autores[-1], autores[-2]]

libro_destacado = []
if "Ray Bradbury" in autores_vivos:
    libro_destacado=["Fahrenheit 451","Ray Bradbury"]
else:
    print("Ray Bradbury no está en la lista de autores vivos.")

if "Crónica de una muerte anunciada" in autores_vivos:
    autores_vivos.append("Premio Nobel")
else:
    print("El libro 'Crónica de una muerte anunciada' no está en la lista de autores vivos.")

if "Premio Nobel" in destacados:
    registro={
        "título": "Crónica de una muerte anunciada",
        "autor": "Gabriel García Márquez",
        "disponible": True
    }
else:
    print("El libro 'Crónica de una muerte anunciada' no está en la lista de destacados.")

registro = {}
if "registro" in locals():
    registro["Ubicación"] = "estantería 3"
else:
    print("No se ha creado el registro.")  
    
if "Don quijote" not in libros:
    libros.append("Don Quijote")
else:
    print("El libro 'Don Quijote' ya está en la lista.")    
    
if "El principito" not in libros:
    libros.append("El principito")
else:
    print("El libro 'El principito' ya está en la lista.")

print(libros , autores, destacados, autores_vivos, libro_destacado, registro)

    


    