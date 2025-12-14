from Veiculo import Veiculo;

# Criando subclasse Carro
class Carro(Veiculo):

  # Construtor
  def __init__(self, id: str):
    super().__init__(id, 'carro', 0);
  # Fim construtor

  # Métodos do objeto
  def calcularValor(self, horaSaida: int):
    valor = (horaSaida - self.horaEntrada) / 10 ;
    valorFinal = valor if valor >= 5 else 5;
    print(f'Carro chegou {self.horaEntrada} saiu {horaSaida}. Pagar R$ {valorFinal:.2f}');
  # Fim métodos do objeto
# Fim subclasse Carro
