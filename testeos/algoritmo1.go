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

switch numero {
case 1, 3, 5:
	fmt.Println("Número es impar")
case 2, 4, 6:
	fmt.Println("Número es par")
default:
	fmt.Println("Número no está en el rango")
}
fmt.Println("Switch con fallthrough:")
switch numero {
case 1:
	fmt.Println("Caso 1")
case 3:
	fmt.Println("Caso 3")
	fallthrough
case 4:
	fmt.Println("Caso 4 por fallthrough")
default:
	fmt.Println("Caso default")
}
