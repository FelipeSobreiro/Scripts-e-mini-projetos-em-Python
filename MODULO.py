from dataclasses import dataclass
from datetime import datetime
import json


@dataclass
class Cadastro:
    nome:str
    estado:str
    tel:int
    CPF:int
    email:str
    
    def __post_init__(self):

        if not isinstance(self.tel,int) or self.tel<=0:
            raise ValueError ("Telefone informado não está correto !")

        if len(str(self.CPF)) !=11:
            raise ValueError ("CPF INFORMADO NÃO ESTÁ CORRETO !")
        

        if "@" not in self.email or "." not in self.email:
    
            raise ValueError("Email invalido !")
        
        
    def dados_clientes(self,dados):
        dados.append({"Cliente":self.nome,"ES":self.estado,"Telefone":self.tel,"CPF":self.CPF,"EMAIL":self.email})

        return dados
    
@dataclass
class Produtos:
    nome:str
    categoria:str
    unidade:int
    preco:float
    

    def cadastro_produto(self,dados):
        dados.append({"NOME":self.nome,"Categoria":self.categoria,"UNIDADE DE VENDA":self.unidade,"PREÇO":self.preco})

        return dados




@dataclass
class RegistroCompra:
    cliente:Cadastro
    produto:Produtos
    data:str


    def valor_total(self):
        return self.produto.preco*self.produto.unidade
    



    def resumo_compra(self):
        resumo={
            "CLIENTE":self.cliente.nome,
            "PRODUTOS":[],
            "Valor_total":self.valor_total(),
            "DATA DA COMPRA":self.data
        }

        return resumo

    def dados_preco_produtos(self):
        dados={
            "Produto":self.cliente.nome,
            "PREÇO":self.produto.preco
        }

        with open("dados_preços.json","w") as f:
         json.dump({"preço":dados},f,indent=4)

        return dados




@dataclass
class Atualização(Cadastro,Produtos):


    def atualizar_dados_clientes(self,I:int,novo_valor):

        if I ==1:
            self.nome=novo_valor
        elif I==2:
            self.email=novo_valor
        elif I==3:
            self.estado=novo_valor
        elif I==4:
            self.tel=int(novo_valor)
        elif I==5:
            self.CPF=int(novo_valor)
    

    def atualizar_produtos(self,j:int,novo_valor):

        if j==1:
            self.nome=novo_valor
        elif j==2:
            self.categoria=novo_valor
        elif j==3:
            self.unidade=int(novo_valor)
        elif j==4:
            self.preco=float(novo_valor)
    

        
@dataclass
class Estilo:

    def espaço():
        pass
    
    def centro(texto,caracter=20):
      j=texto.center(caracter,"-")
    

      return print(j)
 

    def collor(self,cor):
      cores={
        "vermelho":f"\033[91m {self}\033[0m",
        "verde":f"\033[92m{self}\033[0m",
        "amarelo":f"\033[93m {self}\033[0m",
        "azul":f"\033[94m{self}\033[0m",
        "ciano":f"\033[96m{self}\033[0m",
        "magenta":f"\033[95m{self}\033[0m"

    }
      return cores.get(cor.lower(),str(self))






    
        
