class Imovel():

    def __init__(self):
        self._endereco = None
        self._valor = None

    def setEndereco(self, endereco):
        self._endereco = endereco

    def getEndereco(self):
        return self._endereco

    def setValor(self, valor):
        self._valor = valor

    def getValor(self):
        return self._valor

    def informaImovel(self):
        self.setEndereco(input("informa o Endereco: "))
        self.setValor(float(input("informa o Valor: ")))

class Novo(Imovel):

    def __init__(self):
        super().__init__()

    def getAdicional(self):
        return self.adicional

    def setAdicional(self, adicional):
        self.adicional = adicional

    def novo(self):
        #imovel = Imovel()
        #valorNovo = float(imovel.getValor())/0.7
        valorNovo = super().getValor() * self.getAdicional()
        return round(valorNovo, 2)

class Velho(Imovel):

    def __init__(self):
        super().__init__()

    def getDesconto(self):
        return self.desconto

    def setDesconto(self, desconto):
        self.desconto = desconto

    def velho(self):
        imovel = Imovel()
        valorVelho = float(imovel.getValor()) * self.getDesconto()
        return round(valorVelho, 2)

imovel = Imovel()
novo = Novo()
velho = Velho()
novo.setAdicional(1.25)
velho.setDesconto(0.75)

imovel.informaImovel()
print("O imovel é Novo ou Velho:")
print("1 - Novo")
print("2 - Velho:")
op = (input(">"))
if op == "1":
    print("Valor com adicional: ", (novo.novo()))
elif op == "2":
    print("Valor com desconto: ", (velho.velho()))

    