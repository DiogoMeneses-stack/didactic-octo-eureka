print("="*30,"GERADOR DE CÓDIGO DE BARRA","="*30, "\n")

iniciar = str(input("Deseja iniciar programa S/n: "))

if (iniciar == 'S') or (iniciar == 's'): 

        nome_do_produto = str(input("Digite o nome do produto: "))
        id = str(input("Qual o numero do produto: "))
        unidade_do_produto = str(input("Seu produto é vendido como Kg ou Un: "))
        preco = str(input("Qual o preço do produto: "))
        lista_de_produtos_cadastrados = [ 1000 ] 
        
        i = nome_do_produto,",","2"+id+"000,", unidade_do_produto, "preco:R$ "+preco, unidade_do_produto 
        print(nome_do_produto,"2"+id+"000,", unidade_do_produto,"preco:R$ "+preco, unidade_do_produto)
        
        continuar = str(input("\n Deseja continuar S/n: "))
        
        if (continuar == 's') or (continuar == 'S'):
          for continuar in range((continuar != 'S') or (continuar != 's')):
                lista_de_produtos_cadastrados.append(i)
                nome_do_produto = str(input("Digite o nome do produto: "))
                id = str(input("Qual o numero do produto: "))
                unidade_do_produto = str(input("Seu produto é vendido como Kg ou Un: "))
                preco = str(input("Qual o preço do produto: "))
                lista_de_produtos_cadastrados = [i] 
                
                i = nome_do_produto,"2"+id+"000,", unidade_do_produto, "preco:R$ "+preco, unidade_do_produto
                print(nome_do_produto,",","2"+id+"000,", unidade_do_produto,"preco:R$ "+preco, unidade_do_produto)
                continuar = str(input("\n Deseja continuar S/n: "))

                if (continuar != 's') or (continuar != 'S'):
                  print("\nLista de Produtos registrados: \n")
                  lista_de_produtos_cadastrados.append(i)
                  print(lista_de_produtos_cadastrados)
                  print("="*30,"Programa Finalizado","="*30)
                  break
        else:
          print("\nLista de Produtos registrados: \n")
          lista_de_produtos_cadastrados.append(i)
          print(lista_de_produtos_cadastrados)
          print("="*30,"Programa Finalizado","="*30)
      
else:
  print("="*30,"Programa Finalizado","="*30)