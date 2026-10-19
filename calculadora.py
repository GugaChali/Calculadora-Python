import math
import ast
print("┌"+"─" * 30+"┐")           
print("|"+"CALCULADORA PYTHON".center(35)+"|")
print("└"+"─" * 30+"┘")
while True:
 resultado = None
 print("1- Operações básicas")
 print("2- Potência")
 print("3- Raiz quadrada")
 print("4- Expressão numérica")
 print("5- Porcentagem")
 print("6- Equações do 1° e 2° Grau")
 print("=" * 30)
 resposta1 = input("Escolha 1 opção(Digite somente o número): ")
 print("")
 if len(resposta1) != 1 or resposta1 not in ("1","2","3","4","5","6"):
  print("Caráctere inválido")
  print("")
 else:
  break
if resposta1 == "1":
    while True:
        try:
            num1 = float(input("Escolha o primeiro número: ").replace(",", "."))
            print("=" * 30)
            num2 = float(input("Agora escolha o segundo: ").replace(",", "."))
            print("=" * 30)
            break  # Só sai do loop se os dois números forem válidos.
        except ValueError:
            print("❌ Valor incompatível, digite somente números ")
            # Sem break aqui, para o usuário poder tentar de novo.

    print("1- Multiplicação")
    print("2- Divisão")
    print("3- Soma")
    print("4- Subtração")
    
    while True:
        try:
            resposta3 = int(input("Escolha uma operação (Digite somente o número): "))
            if resposta3 in [1, 2, 3, 4]:
                break
            print("❌ Resposta inválida. Escolha entre 1 e 4. ")
        except ValueError:
            print("❌ Digite apenas um número inteiro válido. ")

    if resposta3 == 1:
        resultado = num1 * num2
    elif resposta3 == 2:
        if num2 == 0:
            print("❌ Não é possível dividir por zero ")
        else:
            resultado = num1 / num2
    elif resposta3 == 3:
        resultado = num1 + num2
    elif resposta3 == 4:
        resultado = num1 - num2

if resposta1 == "2":
   while True:
    try:   
     num1 = float(input("Escolha o número a ser elevado:"))
     print("=" * 30)
     num2 = float(input("Agora, escolha o expoente:"))
     print("=" * 30)
     break
    except ValueError:
     print("Valor incompatível, digite somente números:")     
   resultado = num1 ** num2
    
if resposta1 == "3":
   while True:
    try:
     num1 = float(input("Escolha o número para que a raiz seja calculada:"))
     resultado = math.sqrt(num1)
     break
    except ValueError:     
     print("Valor não compatível, digite somente números:")
   #math.sqrt é o cálculo de raiz quadrada
   #math.isqrt é o cálculo de raiz quadrada que só aceita números inteiros                                                                                                            
     break
if resposta1 == "4":
    expressao = input("Digite a expressão:").replace(",",".")
    print("=" * 30)
    arvore = ast.parse(expressao, mode="eval")
    print(ast.dump(arvore))
    def calcular(no):
        if isinstance(no, ast.Constant):
            return no.value
        elif isinstance(no, ast.BinOp):
            esquerda = calcular(no.left)
            direita = calcular(no.right)
            if isinstance(no.op, ast.Add):
                return esquerda + direita
            elif isinstance(no.op, ast.Mult):
                return esquerda * direita
            elif isinstance(no.op, ast.Sub):
                return esquerda - direita 
            elif isinstance(no.op, ast.Div): 
                return esquerda / direita
            elif isinstance(no.op, ast.Pow):
                return esquerda ** direita
            elif isinstance(no.op, ast.FloorDiv):
                return esquerda // direita
            elif isinstance(no.op, ast.Mod):
                return esquerda % direita
        elif isinstance(no, ast.UnaryOp):
                operando = calcular(no.operando)
                if isinstance(no.op, ast.USub):
                  return -operando
                elif isinstance(no.op, ast.UAdd):
                    return +operando
    resultado = calcular(arvore.body)                    

if resposta1 == "5":
   while True:            
           print("1- Porcentagem de um número") 
           print("")
           print("2- Aumentar Y(Número inteiro) em X%(porcentagem)")
           print("")                   
           print("3- Diminuir Y(Número inteiro) em X%(porcentagem)") 
           print("")
           while True:
            try:
             resposta3 = int(input("Escolha uma das opções(digite somente o número:)")) 
             print("")  
             if resposta3 in(1, 2, 3):
              break             
             else:
              print("Foi detectada uma letra ou número fora das opções")
            except ValueError:
             print("")              
             print("Digite somente números:") 
           if resposta3 == 1:
            while True:  
             try:  
              print("")            
              num1 = float(input("Escolha o número de porcentagem:"))
              print("")
              break
             except ValueError:
               print("Valor inválido, digite somente números")
            while True:
             try:
              print("") 
              num2 = float(input("Agora escolha o número a ser calculado a porcentagem:"))             
              print("")
              break
             except ValueError:
              print("Valor inválido, digite somente números:")
              print("")
            resultado = (num1/100)*num2          
            break
           if resposta3 == 2:
            while True:  
             try:
              print("")              
              num1 = float(input("Escolha o número:"))
              print("")
              break
             except ValueError:
               print("Valor inválido, digite somente números")
               print("")
            while True:
             try:
              print("") 
              num2 = float(input("Agora escolha o número de porcentagem a ser somado ao número anterior:"))             
              print("")
              break
             except ValueError:
              print("Valor inválido, digite somente números")
              print("")
            resultado = num1 + ((num2 / 100) * num1)
            break
           if resposta3 == 3:
            while True:  
             try: 
              print("")             
              num1 = float(input("Escolha o número:"))
              print("")
              break
             except ValueError:
               print("Valor inválido, digite somente números")
               print("")
            while True:
             try:
              print("")
              num2 = float(input("Agora escolha o número a ser subtraido a porcentagem:"))             
              print("")
              break
             except ValueError:
              print("Valor inválido, digite somente números")
              print("")
            resultado = num1 - ((num2 / 100) * num1)              
            break              
if resposta1 == "6":
  print("1- Equação do 1° Grau")
  print("2- Equação do 2° Grau")            
  
  resposta3 = input("Escolha uma das duas opções:")
  if len(resposta3) != 1 or resposta3 not in ("12"):
   print("Caráctere inválido")
   print("")
  else:   
   if resposta3 == "1":
    print("") 
    equacao1grau = input("Digite a equação:")
    esquerda, direita = equacao1grau.split ("=")
    esquerda = esquerda.strip()
    direita = direita.strip()
    for i in range(len(esquerda)):
     print(i, esquerda[i])
     print("")     
    print(esquerda.index("x"))
    print("")
    posicao_x = esquerda.index("x")
    if esquerda[0] == "-":
     sinal_x = -1
    else:
     sinal_x = 1
    if posicao_x == 0:
     coeficiente = 1

    elif posicao_x == 1:
     if esquerda[0] == "-":
        coeficiente = -1
     else:
      coeficiente = float(esquerda[:posicao_x])
    
    else:
     coeficiente = float(esquerda[:posicao_x])              
    print(f"{coeficiente}")     
                                                                                
print(f"O seu resultado é {resultado:.2f}")