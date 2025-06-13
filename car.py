from dataclasses import dataclass,field

@dataclass
class Veiculo:
    marca:str
    modelo:str
    ano:int
    dados: list = field(default_factory=list,init=False)



    def adicionar_dados(self):
        self.dados.append({"Modelo":self.modelo,
                           "marca":self.marca,
                           "ano":self.ano
                           })
        
        return self.dados

    def exibir_info(self):
        for c in self.dados:
            print(c)


@dataclass
class Carro(Veiculo):
    qtd_portas:int


    def exibir_info(self):
        super().exibir_info()
        print(f"portas {self.qtd_portas}")
    
@dataclass
class Moto(Veiculo):
    cilindrada:str

    
    def empinar(self):
        print(f"A moto {self.modelo} Está empinando")




c1 = Carro(marca="Toyota", modelo="Corolla", ano=2020, qtd_portas=4)
m1 = Moto(marca="Yamaha", modelo="MT-03", ano=2023, cilindrada="321cc")

c1.adicionar_dados()
m1.adicionar_dados()

c1.exibir_info()
print()
m1.exibir_info()
m1.empinar()