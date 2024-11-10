//Daniel Villamar
nombre := "Juan"
edad := 30
precio := 49.99
fmt.Println("Nombre:", nombre)
fmt.Println("Edad:", edad)
fmt.Println("Precio:", precio)
fmt.Print("Nombre: ", nombre, " | ")
fmt.Print("Edad: ", edad, " | ")
fmt.Print("Precio: ", precio, " | ")
mensaje := fmt.Sprintf("\nNombre: %s | Edad: %d | Precio: %.2f", nombre, edad, precio)
