# programa para simular el lanzamiento de un dado

import random

print("------------------------------------------")
print("---------LANZAMIENTO DE UN DADO----------")
print("------------------------------------------")

# input 

# processing
d1 = random.randint(1,6)
# d2 = random.randint(1,6)
d2 = int(input("Adivina el numero que salio en el dado:"))


"""if (d1==1):
    rta = "UNO"
elif (d1==2):
    rta = "DOS"
elif (d1==3):
    rta = "TRES"
elif (d1==4):
    rta = "CUATRO"
elif (d1==5):
    rta = "CINCO"
elif (d1==6):
    rta = "SEIS"
else:
    rta = "NO ES LA CARA DE UN DADO"""

if (d2>6):
    rta = "USTED DIGITÓ UN NÚMERO NO VALIDO"
else: 
    if (d1==d2):
        rta = "ADIVINASTE EL NUMERO"
    else:
        rta = "I AM SORRY..... NO ADIVINASTE"

# output
print(rta)
print("Dado : " +str(d1))
print("USTED DIGITO: " +str(d2))