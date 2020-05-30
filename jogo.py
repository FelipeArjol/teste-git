print("*********************************")
print("Tente adivinhar o número! ")
print("*********************************")

numero_secreto = 42                                 #Variaveis
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas + 1):                     #1 bloco de execução
  print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
  chute_str = input("Digite o seu número entre 1 e 50: ")
  print("Você digitou " , chute_str)
  chute = int(chute_str)

  if(chute < 1):                                                      #2 bloco de execução
    print("Você deve digitar um número entre 1 e 50: ")
    continue
  elif(chute > 100):
    print("Você deve digitar um número menor ou igual a 50: ")
  

  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):                                                        #3 bloco de execução
      print("Parabéns! Você acertou!")
      break
  else:
      if(maior):
          print("O seu chute foi maior do que o número secreto!")
      elif(menor):
          print("O seu chute foi menor do que o número secreto!")


print("Fim do jogo")                                                  #fim do programa