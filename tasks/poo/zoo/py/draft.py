from abc import ABC, abstractmethod;

class Animal(ABC):
  @abstractmethod
  def apresentar_nome(self) -> None:
    pass;

  @abstractmethod
  def fazer_som(self) -> None:
    pass;

  @abstractmethod
  def mover(self) -> None:
    pass;