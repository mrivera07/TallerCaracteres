name="Luis"
age="27"
favoriteFood=" la salsa Baloñesa"
text1=f"Hola! Mi nombre es {name}. yo tengo {age} años y mi comida favorita es {favoriteFood}"
print(text1)

# funcion len
fullname="Luis Alfonso vejarano"
text2 = len(fullname.replace(" ",""))
print(f"hola,{fullname} tu nombre tienen {text2} letras excluyendo los espacios")

#Funcion formar string
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
text3=f"las ventas de la empresa lactea aumentaron con {increaseSalesPercent:.2f} % y los ingresos crecieron {revenueGrowthPercent:.2f} %"
print(text3)

#slicing" o "rebanado" en Python.
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
decodedMessage = secretMessage[3::2]
print(decodedMessage)
# Funcion len(text.split()) para contar numero de palabras
text= 'El nombre "Python" viene dado por la afición de Van Rossum al grupo Monty Python.'
texto5 = len(text.split())
print(f"Número de palabras en la frase: {texto5}")
#remplazar
word = "Camila"
text6= word.replace("a","e")
print(text6)
#
# Frase proporcionada
sentence = "La historia del lenguaje de programación Python"
text7 = ' '.join(sentence.split()[::-1])
print(text7)