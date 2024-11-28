package main

import (
	"fmt"
)

// Este es un comentario de una línea

/*
  Este es un comentario de múltiples líneas
  que cubre varias líneas de código.
*/

// Declaración de variables globales
var x int = 10
var y float64 = 20.5
const pi float32 = 3.14159

func main() {
	// Declaración de variables locales
	var name string = "Go Lang"
	message := "¡Hola, mundo!"

	fmt.Println(message)

	// Operaciones condicionales y de bucle
	if x > 5 {
		fmt.Println("x es mayor que 5")
	} else {
		fmt.Println("x es menor o igual a 5")
	}

	// Bucle for
	for i := 0; i < 5; i++ {
		fmt.Println("Iteración %d\n", i)
	}
}

// Función simple de suma
func add(a int, b int) int {
	return a + b
}