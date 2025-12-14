from Veiculo import Veiculo;

# Criando subclasse Bike
class Bike(Veiculo):

  # Construtor
  def __init__(self, id):
    super().__init__(id, 'bike', 0);
  # Fim construtor

  # Métodos do objeto
  def calcularValor(self, horaSaida: int):
    print(f'Bike chegou {self.horaEntrada} saiu {horaSaida}. Pagar R$ 3.00');
  # Fim métodos do objeto
# Fim subclasse Bike