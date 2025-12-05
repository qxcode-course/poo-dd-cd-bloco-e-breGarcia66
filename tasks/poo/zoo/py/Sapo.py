from Animal import Animal;

# Criando classe Sapo
class Sapo(Animal):

  # Construtor
  def __init__(self, nome: str):
    super().__init__(nome)
  # Fim construtor

  # Métodos do objeto
  def fazerSom(self):
    print('croac-corac... croac');

  def mover(self):
    print(f'O sapo {self.nome} está se movendo pulando pelo úmido pantano...')
  # Fim métodos do objeto
# Fim classe Sapo