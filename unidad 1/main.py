
# estaturas = {
#     "joel" : 180,
# }

# for nombre, estatura in estaturas.items(): 
#     print(f"{nombre} mide {estatura}")


# # #iteracion en multiples secuencias
# nombres = ['joel', 'maria']
# edades  = [21,21]

# for nombre, edad in zip(nombres, edades):
#     print(f"{nombre} tiene {edad} años ")


# interacion con enumerate para obtner los indices
# nombres = ['joel', 'maria', 'pedro']
# for indice, nombre in enumerate(nombres): 
#     print(f"indice: {indice}, nombre: {nombre}")


# contador = 0
# while(contador < 5): 
#     print(f"contador: {contador}!")
#     contador+=1


# continuar = True
# while(continuar) :
#     respuesta = input('Quieres continuar (s/n) ? ')
#     if(respuesta.lower() == 'n'):
#         continuar = False


# valor = None
# while(valor is None) :
#     entrada = input('Introduce un numero entero')
#     try: 
#         valor = int(entrada)
#     except ValueError:
#         print('Error')

# while(True):
#     respuesta = input('Quierres salir')
#     if(respuesta.lower() == 's'): 
#         break


# nombres = ["jiuan", 'maria', 'ana']
# while(nombres): 
#     print(nombres.pop())

# nombres = ['juan', 'maria', 'ana', 'pedro']
# while(len(nombres) > 0):
#     print(nombres.pop())