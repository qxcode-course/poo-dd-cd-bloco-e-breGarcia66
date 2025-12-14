from Estacionamento import Estacionamento, Moto, Bike, Carro;

# Método main
def main():
  estacionamento: Estacionamento = Estacionamento();
  
  while True:
    line: str = input();
    args: list[str] = line.split(' ');
    print(f'${line}');

    match args[0]:
      case 'show':
        print(estacionamento);

      case 'tempo':
        estacionamento.passarTempo(int(args[1]));

      case 'estacionar':
        match args[1]:
          case 'bike':
            estacionamento.estacionar(Bike(args[2]));

          case 'moto':
            estacionamento.estacionar(Moto(args[2]));

          case 'carro':
            estacionamento.estacionar(Carro(args[2]));
      
      case 'pagar':
        estacionamento.pagar(args[1]);
        estacionamento.sair(args[1]);

      case 'end':
        break;

      case _:
        print('Erro: comando invalido');

# Executando main()
main()