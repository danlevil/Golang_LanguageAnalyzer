//Daniel Villamar
edad := 25            
nombre := "Juan"      
precio := 99.99       
disponible := true    

var edad int = 13           
var nombre string = "Melissa"  
var precio float64 = 12.16  
var disponible bool = true  

var (
    edad       int     = 24
    nombre     string  = "Nicole"
    precio     float64 = 123.99
    disponible bool    = false
)
mapa1 := make(map[string]int)
mapa1["A"] = 1
mapa1["B"] = 2
fmt.Println("Mapa 1:", mapa1)

mapa2 := map[string]int{
    "C": 3,
    "D": 4,
}
fmt.Println("Mapa 2:", mapa2)

var mapa3 map[string]int
mapa3 = make(map[string]int)
mapa3["E"] = 5
mapa3["F"] = 6
fmt.Println("Mapa 3:", mapa3)

// 4. Iterar sobre un map
fmt.Println("Iterando sobre mapa2:")
for clave, valor := range mapa2 {
    fmt.Printf("Clave: %s, Valor: %d\n", clave, valor)
}
