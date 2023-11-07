
class Conta:
    def __init__(self, titular, numero_de_conta, quantidade):
        self.titular = titular
        self.numero_de_Conta = numero_de_conta
        self.quantidade = quantidade

    def __gt__(self, quantidadeconta):
        return self.quantidade > quantidadeconta.quantidade

    def __eq__(self, quantidadeconta):
        return self.quantidade == quantidadeconta.quantidade

    def ExibirInformacoesDestaConta(self):
        print(self.titular, self.numero_de_Conta, self.quantidade)

conta1 = Conta('Rosicleite Monteiro', '123456789' , '5.200 Euros')
conta1.ExibirInformacoesDestaConta()
conta2 = Conta('Raquel Sofia', '789654123', '1.200 Euros')
conta2.ExibirInformacoesDestaConta()


if conta1 > conta2:
    print('Conta1 tem mais dinheiro.')

elif conta1 == conta2:
    print('Conta com Valores iguais')

else:
    print('Conta 2 tem mais dinheiro.')

