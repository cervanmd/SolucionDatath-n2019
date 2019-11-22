def ecuacion(b):
	
	return(65.92+(float(b)*-64.19))

def ecuacion2(b,a):
	return(43.84712+(float(b)*-41.50459)+(float(a)*-0.02713))

print("Ingrese el tipo de diagnostico:")
print('ingrese la letra a para un Diagnostico no invasivo 92% de exactitud')
print("ingrese la letra b para un Diagnositico invasivo 98% de exactitud")

select = input()

if select == 'a':
	print("Ingrese el resultado del examen de orina: ")
	a = input()
	a = ecuacion(a)
	if a > 0.5:
		print("No estas en Riesgo")
	else:
		print("Estas en Riesgo")
else:
	print("Ingrese el resultado del examen de orina: ")
	a = input()
	print("Ingresa el resultado de tu examen de sangre: ")
	b = input()
	r = ecuacion2(a,b)
	if r > 0.5:
		print("No estas en Riesgo")
	else:
		print("Estas en Riesgo")	
