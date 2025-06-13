class TransporteEscolar:
    def __init__(self,marca,modelo,capacidade):
        self.marca=marca
        self.modelo=modelo
        self.capacidade=capacidade
    
    def descricao(self):
        desc=str(f"MARCA {self.marca}| Modelo {self.modelo} | capacidade {self.capacidade}")

        return desc
    

class Van(TransporteEscolar):
    def __init__(self, marca, modelo, capacidade,escolarizada):
        super().__init__(marca, modelo, capacidade)
        self.escolarizada=bool(escolarizada)
    
    def descricao(self):
     if self.escolarizada:
        return f"[VAN] {super().descricao()} | AUTORIZADA"
     else:
        return f"[VAN] {super().descricao()} | NÃO AUTORIZADA"

        



class Micro(TransporteEscolar):
    def __init__(self, marca, modelo, capacidade, ar_condicionado):
        super().__init__(marca, modelo, capacidade)
        self.ar_condicionado=bool(ar_condicionado)


    def descricao(self):
     if self.ar_condicionado:
        return f"[MICRO] {super().descricao()} | COM AR"
     else:
        return f"[MICRO] {super().descricao()} | SEM AR"


class Garagem:
  def __init__(self,nome):
      self.nome=nome
      self.veiculos = []

  def Adicionar_veiculos(self,veiculo):
       self.veiculos.append(veiculo)

       return str('Veiculo adicionado com sucesso !')
  def remover_veiculo(self, modelo):
        modelo = modelo.lower()
        for v in self.veiculos:
            if v.modelo.lower() == modelo:
                self.veiculos.remove(v)
                return "Veículo removido com sucesso!"
        return "Veículo não encontrado."

  def listar_veiculos(self):
    if not self.veiculos:
        return "Nenhum veículo cadastrado."
    return "\n".join([v.descricao() for v in self.veiculos])

  def contar_por_tipo(self):
      count_van=0
      count_micro=0
      for c in self.veiculos:
        if isinstance(c,Van):
            count_van+=1
        elif isinstance(c,Micro):
            count_micro+=1

      return str(f"Vans {count_van} | MICRO ONIBUS {count_micro}")
      




g = Garagem("Central")

v1 = Van("Renault", "Master", 12, True)
m1 = Micro("Volks", "9.160", 28, False)
v2 = Van("Fiat", "Ducato", 10, False)

g.Adicionar_veiculos(v1)
g.Adicionar_veiculos(m1)
g.Adicionar_veiculos(v2)

print(g.listar_veiculos())
print(g.contar_por_tipo())
print(g.remover_veiculo("Ducato"))
print(g.contar_por_tipo())
