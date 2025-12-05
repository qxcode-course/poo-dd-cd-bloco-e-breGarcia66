from abc import ABC, abstractmethod;

# Criando classe abstrada Animal
class Animal(ABC):
  
  # Construtor
  def __init__(self, nome: str = 'criatura'):
    self._nome: str = nome;
  # Fim construtor

  # Métodos de acesso
  @property
  def nome(self) -> str:
    return self._nome;
  # Fim métodos de acesso

  # Métodos mutantes
  @nome.setter
  def nome(self, nome: str):
    self._nome = nome;
  # Fim métodos mutantes

  # Métodos concretos
  def apresentarNome(self):
    print(f'eu sou um(a) {self.nome}');
  # Fim métodos concretos

  # Métodos abstratos
  @abstractmethod
  def fazerSom(self):
    pass

  @abstractmethod
  def mover(self):
    pass
  # Fim métodos abstratos
# Fim classe abstrata Animal
  