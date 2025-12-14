from Veiculo import Veiculo;

# Criando subclasse Moto
class Moto(Veiculo):

  # Construtor
  def __init__(self, id: str):
    super().__init__(id, 'moto', 0);
  # Fim construtor

  # Métodos do objeto
  def calcularValor(self, horaSaida: int):
    valor = (horaSaida - self.horaEntrada) / 20;
    print(f'Moto chegou {self.horaEntrada} saiu {horaSaida}. Pagar R$ {valor:.2f}');
  # Fim métodos de objeto
# Fim subclasse Moto
