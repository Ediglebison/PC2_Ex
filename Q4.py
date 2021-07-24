class Ingresso():

    def __init__(self):
        self.valorIngresso = None

    def imprimeValor(self):
        return 50 #valorIngresso

class VIP(Ingresso):

    def __init__(self):
        super().__init__()

    def valorVIP(self):
        ingresso = Ingresso()
        ingressoVIP = int(ingresso.imprimeValor()) + 100
        return ingressoVIP

class CamaroteInferior(VIP):

    def __init__(self):
        super().__init__()

    def valorCamInf(self):
        ingresso = VIP()
        ingressoCamInf = int(ingresso.valorVIP()) + 100
        return ingressoCamInf

class CamaroteSuperior(VIP):

    def __init__(self):
        super().__init__()

    def valorCamSup(self):
        ingresso = VIP()
        ingressoCamSup = int(ingresso.valorVIP()) + 200
        return ingressoCamSup

normal = Ingresso()
vip = VIP()
camaroteInferior = CamaroteInferior()
camaroteSuperior = CamaroteSuperior()


print("Ingresso Pista: "+str(normal.imprimeValor()))
print("Ingresso VIP: "+str(vip.valorVIP()))
print("Ingresso Cam. Inferior: "+str(camaroteInferior.valorCamInf()))
print("Ingresso Cam. Superior: "+str(camaroteSuperior.valorCamSup()))
