# Esto es un comentario
edad = 29
nombre = 'Felix'
apellido = "Espinoza"

# No se pieden usar los backtips (comillas invertidas) para los string
#! Saludo = `Holo como estas, mi nombre es ${nombre}`

mensaje = '''el dia de 
hoy el modulo de 
backend'''

despedida = """El dia de hoy nos despedimos hasta 
una nueva 
oportunidad"""

#Para un apellido que tenga comilla simples es mejor usas comillas dobles en el string
lastName = "O'neil"
print(nombre)

#En python no hay ni null ni undefined ni NaN (Not a Number) todo ello se resume en None
especialidad = None
print(especialidad)

#No hay validacion al monento de cambiar el tipo de dato
lastName = 80
lastName = None

# type(var) > devolver que tipo de dato es esa variable
print(type(nombre))
print(type(edad))

# tambien se puede declarar varias variables en una sola linea
curso, grupo, mes, dia, nota = 'CodiGo', 'Backend', 'Octubre', 20, 15.4

print(grupo)

# id(var) > Mostrar la posicion de memoria en la cual se esta alojando la variable funcion, clase, etc
print(id(curso))

# del > Elimina la variable (liberar la memoria), no se puede volver a utilizar esa variable nunca mas 

del curso

print(curso)
