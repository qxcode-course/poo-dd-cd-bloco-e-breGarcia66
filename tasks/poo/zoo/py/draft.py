from Animal import Animal;
from Cachorro import Cachorro;
from Urso import Urso;
from Sapo import Sapo;

# Instanciando classes
cachorro: Cachorro = Cachorro('Carlitos');
urso: Urso = Urso('Kenai');
sapo: Sapo = Sapo('Alfredo');

# Apresentando animais diversos
def apresentarAnimal(animal: Animal):
  print(f'=====[{type(animal).__name__}]=====');
  animal.apresentarNome();
  animal.fazerSom();
  animal.mover();
  print(f'=====[{type(animal).__name__}]=====\n');


# Execução de código
listaAnimais = [cachorro, urso, sapo];
for animal in listaAnimais:
  apresentarAnimal(animal);
# Fim execução