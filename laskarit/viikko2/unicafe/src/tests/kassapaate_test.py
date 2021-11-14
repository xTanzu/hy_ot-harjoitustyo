import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
    
    # Luotu kassapääte
    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodun_kassapaatteen_myytyjen_edullisten_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luodun_kassapaatteen_myytyjen_maukkaiden_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    # edullisten käteisosto
    def test_edullisten_kateisosto_kassan_rahamaara_kasvaa_edullisen_verran(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisten_kateisosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000), (1000-240))

    def test_edullisten_kateisosto_edullisten_maara_kasvaa_yhdella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisten_kateisosto_jos_raha_ei_riita_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisten_kateisosto_jos_raha_ei_riita_kaikki_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(239), 239)

    def test_edullisten_kateisosto_jos_raha_ei_riita_edullisten_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # maukkaiden käteisosto
    def test_maukkaiden_kateisosto_kassan_rahamaara_kasvaa_maukkaan_verran(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaiden_kateisosto_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), (1000-400))

    def test_maukkaiden_kateisosto_maukkaiden_maara_kasvaa_yhdella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaiden_kateisosto_jos_raha_ei_riita_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_kateisosto_jos_raha_ei_riita_kaikki_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)

    def test_maukkaiden_kateisosto_jos_raha_ei_riita_maukkaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    # edullisten korttiosto
    def test_edullisten_korttiosto_kortilta_veloitetaan_edullisen_verran(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 500-240)
    
    def test_edullisten_korttiosto_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_edullisten_korttiosto_edullisten_maara_kasvaa_yhdella(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisten_korttiosto_jos_raha_ei_riita_kortin_saldo_ei_muutu(self):
        for i in range(3):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 500-(2*240))
    
    def test_edullisten_korttiosto_jos_raha_ei_riita_edullisten_maara_ei_muutu(self):
        for i in range(3):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 2)
    
    def test_edullisten_korttiosto_jos_raha_ei_riita_palautetaan_false(self):
        for i in range(3):
            palautusarvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(palautusarvo, False)
    
    def test_edullisten_korttiosto_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    # maukkaiden korttiosto
    def test_maukkaiden_korttiosto_kortilta_veloitetaan_maukkaan_verran(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 500-400)
    
    def test_maukkaiden_korttiosto_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
    
    def test_maukkaiden_korttiosto_maukkaiden_maara_kasvaa_yhdella(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaiden_korttiosto_jos_raha_ei_riita_kortin_saldo_ei_muutu(self):
        for i in range(2):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 500-400)
    
    def test_maukkaiden_korttiosto_jos_raha_ei_riita_maukkaiden_maara_ei_muutu(self):
        for i in range(2):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaiden_korttiosto_jos_raha_ei_riita_palautetaan_false(self):
        for i in range(2):
            palautusarvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(palautusarvo, False)
    
    def test_maukkaiden_korttiosto_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    # rahan lataus kortille
    def test_kortille_rahaa_ladatessa_kortin_saldo_muuttuu_ladatun_verran(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 696)
        self.assertEqual(self.maksukortti.saldo, 500+696)
    
    def test_kortille_rahaa_ladatessa_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 696)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+696)
    
    def test_kortille_epapositiivista_summaa_ladattaessa_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 0)
        self.assertEqual(self.maksukortti.saldo, 500)
    
    def test_kortille_epapositiivista_summaa_ladattaessa_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)