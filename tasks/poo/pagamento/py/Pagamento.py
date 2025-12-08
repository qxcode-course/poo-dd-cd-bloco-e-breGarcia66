from abc import ABC, abstractmethod;

# Criando superclasse abstrata Pagamento
class Pagamento(ABC):

  # Construtor
  def __init__(self,
               valor: float,
               descricao: str):
    self._valor: float = valor;
    self._descricao: str = descricao;
  # Fim construtor

  # Métodos de acesso
  @property
  def valor(self) -> float:
    return self._valor;

  @property
  def descricao(self) -> str:
    return self._descricao;
  # Fim métodos de acesso

  # Métodos mutantes
  @valor.setter
  def valor(self, valor: float):
    self._valor = valor;
  
  @descricao.setter
  def descricao(self, descricao: str):
    self._descricao = descricao;
  # Fim métodos mutantes

  # Métodos concretos
  def resumo(self):
    print(f'Pagamento de R$ {self.valor:.2f}: {self.descricao}');

  def validarValor(self) -> bool:
    if self.valor <= 0:
      return False;

    return True;
  # Fim métodos concretos

  # Métodos abstratos
  @abstractmethod
  def processar(self):
    pass;
  # Fim métodos abstratos
# Fim superclasse abstrata Pagamento