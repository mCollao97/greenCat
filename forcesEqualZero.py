#METODO QUE REALIZA LA SUMATORIA DE MOMENTOS DE A CON RESPECTO A EJE (y)

def obtenerAy():
	
	i					= 0
	cantidadFuerzas 	= int(input("Ingrese cantidad de fuerzas pleeeeeeeease: "))
	
	fuerzas 			= [0]*cantidadFuerzas
	distancias			= [0]*cantidadFuerzas
	resultados			= [0]*cantidadFuerzas
	
	totalSuma			= 0
	
	for i in range(cantidadFuerzas):
		fuerzas[i]		= float(input("Ingrese una fuerza porfavor: "))
		distancias[i]	= float(input("Ingrese la distancia asociada a esa fuerza porfavor: "))
		resultados[i]	= (fuerzas[i] * distancias[i])
		totalSuma		= totalSuma + resultados[i]
		
	HyDistance			= float(input("Ingrese la distancia asociada al vértice contrario: "))
	Hy					= -(totalSuma/HyDistance)
	totalFuerzas		= float(input("Ingrese la sumatoria de las fuerzas en el eje Y, NEGATIVO!!: "))
	Ay					= totalFuerzas + Hy
	if (Ay < 0): Ay = Ay * -1
	
	print(totalSuma," --- > resultado de la suma y dividendo")
	print("_______________")
	print(HyDistance," ---> divisor")
	print(Hy," ---> vértice de la derecha, vector ascendente")
	print(Ay," ---> vértice de la izquierda, vector ascendente")

obtenerAy()
