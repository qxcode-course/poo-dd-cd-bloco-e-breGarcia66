from CartaoCredito import CartaoCredito;
from Pix import Pix;
from Boleto import Boleto;
from Pagamento import Pagamento;

# Lista de instâncias de pagamentos
pagamentos = [
    Pix(150, 'Camisa esportiva', 'email@ex.com', 'Banco XPTO'),
    CartaoCredito(400, 'Tênis esportivo', '1234 5678 9123 4567', 'Cliente X', 500),
    Boleto(89.90, 'Livro de Python', '123456789000', '2025-01-10'),
    CartaoCredito(800, 'Notebook', '9999 8888 7777 6666', 'Cliente Y', 700),  # deve falhar
];

# Método processarPagamento
def processarPagamento(pagamento: Pagamento):
  if pagamento.validarValor() is False:
    print('Erro: pagamento invalido');
    return;

  pagamento.resumo();
  pagamento.processar();

  return;

# Processando instâncias de pagamentos
for pagamento in pagamentos:
  processarPagamento(pagamento);
