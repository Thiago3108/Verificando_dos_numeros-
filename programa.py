# programa para identificar cual de los dos numeros que se incerten, son mayores y menores 

print("-------------------------------------")
print("----DOS NUMEROS MAYORES O MENORES----")
print("-------------------------------------")


# Input
print("inserte dos numeros")
n1 = int(input("valor 1: " ))
n2 = int(input("valor 2: " ))

# procesing 

valor = n1 < n2 

# output 


if (valor == True):
       print( "Rta: " + str(n1) + " < " + str(n2))

else:
     print( "Rta: " + str(n1) + " > " + str(n2))
