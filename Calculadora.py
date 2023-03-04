
# Estabelecendo Variaveis

print(" \n****** Calculadora ****** ")

num1 = float(input(" \nInsira o Primeiro Número: "))
             
num2 = float(input(" \nInsira o Segundo Número: ")) 
             
operacao = input(" \nSelecione uma operacao (+ , -, *, /):")

# usando if , elif , else 

if operacao == "+":
    resultado = num1 + num2
    print("\nResultado é: ", resultado )
    
elif operacao == "-":
    resultado = num1 - num2
    print("\nResultado é: ", resultado)
    
elif operacao == "*":
    resultado = num1 * num2
    print("\nResultado é: " , resultado)
    
elif operacao == "/":
    resultado = num1 / num2
    print("\nResultado é: " , resultado)
    
else:
    print(" \nOperacao Invalida ")
      





