#importando biblioteca Pickle
import pickle





#função para adicionar contato à lista.

def adicionar(lista):
    
    while True:
        nome = input("Digite o nome do Contato   ")

        if not existe_contato(lista, nome):
            break

        else:
            print("Esse contato já foi cadastrado.")
            print("Por favor, tente um novamente.")

    contato = {
        "nome": nome,
        "tel":  input("Digite o Telefone:   "),
        "email": input("Digite o Email: "),
        "twitter": input("Digite o Twitter "),
        "insta": input("Digite o Instagram: ")
    }

    lista.append(contato)

    print("O contato {} foi cadrastrado com sucesso!\n".format(contato['nome']))










#função para salvar o contato na lista em um banco de dados "data_base_agenda.bin".
def salvar_contatos(lista):
    arquivo = open("data_base-agenda.bin" , "wb")


    pickle.dump(lista, arquivo)     
    
    arquivo.close()










#função para alterar contato previamente já salvo.

def alterar(lista):

    print(" === Alterar de Contato === ")

    if len(lista) > 0:
        nome = input("Digite o nome do contato a ser encontrado\n")

        if existe_contato(lista, nome):
            print("O contato foi encontrado. As informações seguem abaixo\n")

            for contato in (lista):

                if contato['nome'] == nome:
                    print("Nome: {}" .format(contato['nome']))
                    print("Telefone: {}" .format(contato['tel']))
                    print("Email: {}" .format(contato['email']))
                    print("Twitter: {}" .format(contato['twitter']))
                    print("Instagram: {}" .format(contato['insta']))
                    print("============================================\n")

                    contato['tel'] = input("Digite o novo Telefone do contato: ")
                    contato['email'] = input("Digite o novo Email do contato: ")
                    contato['twitter'] = input("Digite o novo Twitter do contato: ")
                    contato['insta'] = input("Digite o novo Instagram do contato: ")

                    print("Os dados do contato com nome {}, foram alterados com sucesso!"
                            .format(contato['nome']))

                    break             

        else:
            print("Não existe contao cadastrado no sistema com este nome {}.\n" .format(nome))

    else:
      print("Não existe nenhum contato cadastrado no sistema.\n")










#função para exclusão de contato previamente já salvo.

def excluir(lista):

    print(" === Excluir de Contato === ")

    if len(lista) > 0:
        nome = input("\nDigite o nome do contato a ser excluido\n")

        if existe_contato(lista, nome):
            print("O contato foi encontrado. As informações seguem abaixo\n")

            for i, contato in enumerate(lista):

                if contato['nome'] == nome:
                    print("Nome: {}" .format(contato['nome']))
                    print("Telefone: {}" .format(contato['tel']))
                    print("Email: {}" .format(contato['email']))
                    print("Twitter: {}" .format(contato['twitter']))
                    print("Instagram: {}" .format(contato['insta']))
                    print("============================================\n")

                    del lista[i]

                    print("O contato foi apagado com sucesso da lista!\n")

                    break
                    
        else:
            print("Não existe contao cadastrado no sistema com este nome {}." .format(nome))
    else:
      print("Não existe nenhum contato cadastrado no sistema.\n")









#função para buscar contato previamente já salvo.

def buscar(lista):

    print(" === Buscar de Contato === ")

    if len(lista) > 0:
        nome = input("\nDigite o nome do contato a ser encontrado\n")

        if existe_contato(lista, nome):
            print("O contato foi encontrado. As informações seguem abaixo\n")

            for contato in (lista):
                if contato['nome'] == nome:
                    print("Nome: {}" .format(contato['nome']))
                    print("Telefone: {}" .format(contato['tel']))
                    print("Email: {}" .format(contato['email']))
                    print("Twitter: {}" .format(contato['twitter']))
                    print("Instagram: {}" .format(contato['insta']))                   
                    print("============================================\n")

                    break
        else:
            ("Não existe contao cadastrado no sistema com este nome {}.\n" .format(nome))

    else:
      print("Não existe nenhum contato cadastrado no sistema.\n")










#função para carregar os contato de um banco de dados "contatos.bin".

def carregar_contatos():
    lista = []

    try:
        arquivo = open("data_base-agenda.bin", "rb")
        
        lista = pickle.load(arquivo)

        arquivo.close()
    except FileNotFoundError:
        pass
    return lista










#função que identifica um contato previamente cadastrado, evitando duplicatas.

def existe_contato(lista, nome):               
    if len(lista) > 0:
        for contato in lista:
            if contato['nome'] == nome:
                return True
    
    return False










#função para listar contatos já salvos.

def listar(lista):

  print(" === Lista de Contatos === ")

  if len(lista) > 0:
      for i, contato in enumerate(lista):
        print("Contato {}:" .format(i+1))
        print("\tNome: {}" .format(contato['nome']))
        print("\tTelefone: {}" .format(contato['tel']))
        print("\tEmail: {}" .format(contato['email']))
        print("\tTwitter: {}" .format(contato['twitter']))
        print("\tInstagram: {}" .format(contato['insta']))
       
      print("Quantidade de contatos: {}\n" .format(len(lista)))

  else:
      print("Não existe nenhum contato cadastrado no sistema.\n")










#função para exportar toda a lista em uma csv

def imprimir(lista):

    if len(lista) > 0:
        print("Lista gerada com sucesso!")
        print("Os contatos foram armazenados no Arquivo: contatos.csv")

        arquivo = open("contatos.csv" , "w")
        arquivo.write("Nome,Telefone,Email,Twitter,instagram\n")
        for contato in lista:
            arquivo.write("{},{},{},{},{}\n" .format(contato['nome'], contato['tel'], contato['email'], contato['twitter'], contato['insta']))      
        
        arquivo.close()
    else:
     print("Não existe nenhum contato cadastrado no sistema.\n")









#função principal, menu para realizar todas as operações possiveis na agenda, de acordo com as funções já programadas.

def principal():

    lista = carregar_contatos()  
    
    while True:
        print(" === Agenda Telefônica === ")
        print(" 1 - adicionar contato")
        print(" 2 - alterar contato")
        print(" 3 - excluir contato")
        print(" 4 - buscar contato")
        print(" 5 - listar contatos")
        print(" 6 - Imprimir Agenda")
        print(" 7 - sair")

        opção = int(input("> "))

        if opção == 1:
            adicionar(lista)
            salvar_contatos(lista)

        elif opção == 2:
            alterar(lista)
            if len(lista) > 0:
                salvar_contatos(lista)

        elif opção == 3:
            excluir(lista)
            if len(lista) > 0:
                salvar_contatos(lista)

        elif opção == 4:
            buscar(lista)

        elif opção == 5:
          listar(lista)

        elif opção == 6:
          imprimir(lista)

        elif opção == 7:
            print("Saindo do progama...")
            break
        else:
            print("Opção Inválida! Por favor, Selecione a Opção corretamente!!!\n")        
principal()