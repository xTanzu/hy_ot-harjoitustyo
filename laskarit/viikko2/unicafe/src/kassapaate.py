class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti_kateisella(self, maksu):
        return self.syo_kateisella(240, maksu)

    def syo_maukkaasti_kateisella(self, maksu):
        return self.syo_kateisella(400, maksu)

    def syo_kateisella(self, hinta, maksu):
        if maksu >= hinta:
            self.kassassa_rahaa += hinta
            self.edulliset += int(hinta == 240)
            self.maukkaat += int(hinta == 400)
            maksu -= hinta
        return maksu

    def syo_edullisesti_kortilla(self, kortti):
        return self.syo_kortilla(240, kortti)

    def syo_maukkaasti_kortilla(self, kortti):
        return self.syo_kortilla(400, kortti)
    
    def syo_kortilla(self, hinta, kortti):
        if kortti.saldo >= hinta:
            kortti.ota_rahaa(hinta)
            self.edulliset += int(hinta == 240)
            self.maukkaat += int(hinta == 400)
            return True
        return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        return
