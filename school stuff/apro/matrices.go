package main

import "fmt"

// import "fmt"

func add(a[][]int, b[][]int) ([][]int) {
	var c [][]int
	if len(a) == len(b) && len(a[0]) == len(b[0]) {
		//initialize resultant matrix
		c = make([][]int, len(a))
		for i := 0; i < len(a); i++ {
			c[i] = make([]int, len(a[0]))
			for j := 0; j < len(a[0]); j++ {
				// add a, b to c
				c[i][j] = a[i][j] + b[i][j]
			}
		}
		return c
	}	
	return c
}
// Multiply two matrices together
func multiply(a[][]int, b[][]int) ([][]int) {
	var c [][]int
	c = make([][]int, len(a))
	// Initialize the resultant matrix
	for i:= range c {
		c[i] = make([]int, len(a[0])) 
	}
	for i:= 0; i < len(a); i++ {
		for j:= 0; j < len(b[0]); j++ {
			for k:= 0; k < len(a[0]); k++ {
				// add to c[i][j] the product of a row, and b col
				c[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return c
}

func main() {
	for sum:=1; sum >0; sum++ {
		// current matrices
		a:=[][]int{{1, 2, 3, 4}, {5,6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}}
		b:=[][]int{{17, 18, 19, 20}, {21, 22, 23, 24}, {25, 26, 27, 28}, {29, 30, 31, 32}}
		
		// input vars
		var duck string
		var mult string

		// duck stuff
		fmt.Print("Duck? (Y)es or (N)o: ")
		fmt.Scan(&duck)
		if duck == "Y" || duck == "y" || duck =="Yes" || duck=="yes" {
			fmt.Println("   _  ")
			fmt.Println("__(.)<")
			fmt.Println("\\____)")
			} else if duck != "N" && duck != "n" && duck !="No" && duck!="no" {
			fmt.Println("Incorrect Input")
			continue
		}

		// computation stuff
		fmt.Print("Multiply or Add? (Y)es for multiply or (N)o for add: ")
		fmt.Scan(&mult)
		if mult == "Y" || mult == "y" || mult =="Yes" || mult=="yes" {
			fmt.Println("Matrix A: ")
			printMatrix(a)
			fmt.Println("Matrix B: ")
			printMatrix(b)
			fmt.Println("Product of Matrices A and B: ")
			printMatrix(multiply(a, b))
			} else if mult == "N" || mult == "n" || mult =="No" || mult=="no" {
			fmt.Println("Matrix A: ")
			printMatrix(a)
			fmt.Println("Matrix B: ")
			printMatrix(b)
			fmt.Println("Sum of Matrices A and B: ")
			printMatrix(add(a, b))
		} else {
			fmt.Println("Incorrect Input")
			continue
		}
		fmt.Println("Again?")
		fmt.Scan(&duck)
		if duck == "Y" || duck == "y" || duck =="Yes" || duck=="yes" {
			continue
			} else if duck != "N" && duck != "n" && duck !="No" && duck!="no" {
			fmt.Println("Incorrect Input")
			continue
		}
		break
	}
}
// prints a matrix in beauty
func printMatrix(a [][]int){
	for _, row := range a {
		fmt.Println(row)
	}
}