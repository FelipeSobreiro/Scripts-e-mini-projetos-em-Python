#REGRAS :
# SO PODE USAR O CHAT PRA PERGUNTAR SE ESTÁ DE ACORDO E NÃO COPIAR NADA DE DELE
# USAR DOCUMENTAÇÃO PARA VERIFICAR E BUSCAR A JUDA


estoque=[]
def adicionar_produto(estoque):
    nome=input('Digite o nome do produto').upper()
    quantidade=int(input("Quantidade em estoque"))
    preco=float(input("Digite o preço do produto R$:"))
    estoque.append({"NOME":nome,'Quantidade':quantidade,'PREÇO':preco})
    print("PRODUTO CADASTRADO COM SUCESSO !")
    return estoque


def Mudar_quantidade(estoque):
    print(estoque)
    x=input('Digite o nome do produto').upper()
    y=int(input("PARA aumentar digite o valor desejado, para diminuir digite sinal de menos e o numero desejado'"))
    for c in estoque:
     if c['NOME']==x:
        c['Quantidade']=c['Quantidade']+y
        print("ITEM ALTERADO COM SUCESSO")
    return estoque


def remover(estoque):
    g=input("DIGITE O PRODUTO QUE DESEJA REMOVER").upper()
    estoque[:]=[produto for produto in estoque if produto["NOME"]!=g]
    print("PRODUTO REMOVIDO COM SUCESSO !") 
    return estoque
               

def mostrar(estoque):
   print(estoque)

def soma(estoque):
    count=0
    preco=0
    print(estoque)
    i=str(input("DESEJA SOMAR TODOS OS PRODUTOS ?[S|N] :")).upper()
    if i in['S']:
      for l in estoque:
        count+=l['Quantidade']
        preco+=l['PREÇO']
    print(f"QUANTIDADE TOTAL: {count} | VALOR TOTAL: R$ {count * preco:.2f}")

    return {"Quantidade Total": count, "Valor Total": count * preco}

def filtro(estoque):
    filtro=[]
    x=str(input("DIGITE O NOME DO ITEM :")).upper()
    for k in estoque:
      if k['NOME']==x:
        filtro.append({"NOME":k['NOME'],"Quantidade":k["Quantidade"],"PREÇO":k['PREÇO']})
        
    return filtro

while True:
    print("LISTA DE ESTOQUE")
    print('ESCOLHA UMA DAS OPÇÕES ')
    print("ADICIONAR PRODUTO [1]")
    print('MUDAR QUANTIDADE DE ESTOQUE [2]')
    print('REMOVER PRODUTO[3]')
    print('SOMAR VALOR DOS PRODUTOS[4]')
    print('FILTRAR ITENS [5]')
    print("MOSTAR LISTA [0]")
    print('SAIR [6]')

    
    escolha=int(input('ESCOLHA :'))
    if escolha not in [1,2,3,4,5,0,6]:
        print("ESCOLHA INVALIDADA, TENTE NOVAMENTE")
        print("          ")
        print("           ")

    if escolha==1:
        adicionar_produto(estoque)

    elif escolha==2:
        Mudar_quantidade(estoque)
    
    elif escolha==3:
       remover(estoque)
    

    elif escolha==4:
       soma(estoque)
    
    elif escolha==0:
       mostrar(estoque)
    
    elif escolha==5:
       filtro(estoque)
      
             
             

    elif escolha==6:
       print("VOCÊ SAIU !!")
       break

 
       
       
        
        