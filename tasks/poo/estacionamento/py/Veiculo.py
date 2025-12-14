from abc import ABC, abstractmethod;
from typing import Literal;

# Literal para tipo de veículos válidos
veiculosValidos = Literal['bike', 'carro', 'moto'];
#

# Criando classe abstrata Veiculo
class Veiculo(ABC):

  # Construtor
  def __init__(self,
               id: str,
               tipo: veiculosValidos,
               horaEntrada: int):
    self._id: str = id;
    self._tipo: str = tipo;
    self._horaEntrada: int = horaEntrada;
  # Fim construtor

  # Método str
  def __str__(self) -> str:

    return f'{self.tipo.capitalize():_>10} : {self.id:_>10} : {self.horaEntrada}';
  # Fim método str

  # Métodos de acesso
  @property
  def id(self) -> str:
    return self._id;

  @property
  def tipo(self) -> str:
    return self._tipo;

  @property
  def horaEntrada(self) -> int:
    return self._horaEntrada;
  # Fim métodos de acesso

  # Métodos mutantes
  @horaEntrada.setter
  def horaEntrada(self, hora: int):
    self._horaEntrada = hora;
  # Fim métodos mutantes

  # Métodos abstratos
  def calcularValor(self, horaSaida: int):
    pass;
  # Fim métodos abstratos
# Fim classe abstrata Veiculo

