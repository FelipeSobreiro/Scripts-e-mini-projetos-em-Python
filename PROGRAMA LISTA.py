#programa que adiciona materias, notas e calcula a media


materias=[]

def adicionar(materias):
  x=str(input("DIGITE O NOME DA MATÉRIA  :")).upper()
  materias.append({"MATERIA": x, "NOTAS": []})
  print("MATERIA CADASTRADA COM SUCESSO !")
  return materias

def notas(materias):
  print(materias['MATERIA'])
  l=str(input("DIGITE O NOME DA MATERIA :")).upper()
  for c in materias:
    if c['MATERIA']==l:
     while True:
      y=float(input("DIGITE A NOTA : "))
      c['NOTAS'].append(y)
      tex=str(input("DESEJA CONTINUAR ? [S|N]")).upper()
      if tex in ['N']:
       break
    else:
      print("NOME DIGITADO ERRADO")
  return materias


def remover(materias):
  for d in materias:
    g=input("DIGITE O PRODUTO QUE DESEJA REMOVER").upper()
    materias[:]=[materias for materia in materias if materia["NOME"]!=g]
    print("PRODUTO REMOVIDO COM SUCESSO !") 
    return materias


def remover_notas(materias):
  x=str(input("DIGITE A MATERIA  :"))
  for c in materias:
    if c['MATERIA']==x:
      print(materias['NOTAS'])
      while True:
       i=float(input("DIGITE A NOTA PARA REMOVER :"))
       remover(materias["NOTAS"]==i)
       quest=str(input("DESEJA CONTINUAR ? [S|N]")).upper()
       if quest in ['N']:
         break
  return materias


def media(materias):
  perg=str(input("DIGITE O NOME DA MATERIA :"))
  for c in materias:
    if c['MATERIA'] == perg:
        if c["NOTAS"]:  
            media = sum(c["NOTAS"]) / len(c["NOTAS"])
            print(f"MÉDIA DA MATÉRIA {perg}: {media:.2f}")
        else:
            print("ESSA MATÉRIA NÃO POSSUI NOTAS CADASTRADAS.")




def dados(materias):
  x=str(input("DIGITE O NOME DA MATERIA : "))
  for c in materias:
    if c['MATERIA']==x:
     print(c["NOTAS"])




print('==LISTA DE MATERIAS E NOTAS==')
print("ADICIONAR MATERIA         [1]")
print('ADICIONAR NOTA            [2]')
print('REMOVER MATERIA           [3]')
print('REMOVER NOTA              [4]')
print('CALCULAR MEDIA            [5]')
print("MOSTRAR DADOS ESPECIFICOS [6]")
print("MOSTRAR LISTA             [7]")
print("SAIR DO PROGRAMA          [0]")





while True:
 escolha=int(input("ESCOLHA UMA DAS OPÇÔES ACIMA"))

 if escolha==1:
   adicionar(materias)
 elif escolha==2:
   notas(materias)
 elif escolha==3:
    remover(materias)
 elif escolha==4:
   remover_notas(materias)

 elif escolha==5:
   media(materias)


 elif escolha==6:
   dados(materias)
 
 elif escolha==7:
   print(materias)
   
   


 elif escolha not in [1,2,3,4,5,6,7,0]:
    print("ERRO :  ESCOLHA INVALIDA")
    print("TENTE NOVAMENTE")
 elif escolha==0:
   print("PROGRAMA ENCERRADO")
   break


