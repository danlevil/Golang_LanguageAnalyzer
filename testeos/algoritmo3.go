// Ronald Gaibor

import (
    "fmt"
)

// Partition divide el arreglo y retorna el índice del pivote
func Partition(arr []int, low, high int) int {
    pivot := arr[high] // Selección del último elemento como pivote
    i := low - 1       // Índice del elemento más pequeño

    for j := low; j < high; j++ {
        // Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot {
            i++ // Incrementar el índice del elemento más pequeño
            arr[i], arr[j] = arr[j], arr[i] // Intercambio
        }
    }
    arr[i+1], arr[high] = arr[high], arr[i+1] // Intercambio con pivote
    return i + 1 // Retorno de índice para divider el arreglo
}

// QuickSort ordena un arreglo de manera recursiva por medio del algoritmo quick sort
func QuickSort(arr []int, low, high int) {
    if low < high {
        pi := Partition(arr, low, high) // Índice de partición

        // Ordena los elementos antes y después de la partición de forma recursiva
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)
    }
}

func main() {
    arr := []int{10, 7, 8, 9, 1, 5}
    fmt.Println("Original array:", arr)
    QuickSort(arr, 0, len(arr)-1)
    fmt.Println("Sorted array:", arr)
}
