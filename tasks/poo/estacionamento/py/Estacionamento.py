from Veiculo import Veiculo;
from Carro import Carro;
from Bike import Bike;
from Moto import Moto;

# Criando classe Estacionamento
class Estacionamento:

  # Construtor
  def __init__(self):
    self.__veiculos: list[Veiculo] = [];
    self.__horaAtual: int = 0;
  # Fim construtor

  # Métodos str
  def __str__(self) -> str:
    formattedText: str = '';
    for veiculo in self.veiculos:
      if self.veiculos.index(veiculo) == len(self.veiculos):
        formattedText += str(veiculo);

      formattedText += f'{veiculo}\n';
    
    formattedText += f'Hora atual: {self.horaAtual}';
    
    return formattedText;
  # Fim método str

  # Métodos de acesso
  @property
  def veiculos(self) -> list[Veiculo]:
    return self.__veiculos;

  @property
  def horaAtual(self) -> int:
    return self.__horaAtual;
  # Fim métodos de acesso

  # Métodos do objeto
  def _procurarVeiculo(self, id: str) -> int:
    for veiculo in self.veiculos:
      if (veiculo.id == id):
        return self.veiculos.index(veiculo);

    return -1;

  def estacionar(self, veiculo: Veiculo):
    veiculo.horaEntrada = self.horaAtual;
    self.veiculos.append(veiculo);

  def passarTempo(self, tempo: int):
    if tempo <= 0:
      raise Exception('Erro: valor invalido para tempo');
  
    self.__horaAtual += tempo;

  def pagar(self, id: str):
    self.veiculos[self._procurarVeiculo(id)].calcularValor(self.horaAtual);

  def sair(self, id: str):
    self.veiculos.pop(self._procurarVeiculo(id));
  # Fim métodos do objeto
# Fim classe Estancionamento
