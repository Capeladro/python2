print(' Programa expresso\n')
print('1 cadastrar restaurante')
print('2 listar restaurante')
print('3 ativa restaurante')
print('4 sair\n')

opcao_digitada = int(input("Escolha uma opção"))
print("Você escolheu:", opcao_digitada, "\n")

if(opcao_digitada==1):
    print("Você escolheu Cadastrar Restaurante\n")
elif(opcao_digitada==2):
    print("Você escolheu Listar Restaurante\n")
elif(opcao_digitada==3):
    print("Você escolheu Ativar Restaurante\n")
else:
    print ("Voce escolheu sair\n")