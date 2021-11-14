import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
    
    # def test_negatiivinen_lataaminen_ei_vahenna_saldoa(self):
    #     self.maksukortti.lataa_rahaa(-10)
    #     self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_ota_rahaa_metodi_palauttaa_true_jos_rahat_riittivat(self):
        palautusarvo = self.maksukortti.ota_rahaa(10)
        self.assertEqual(palautusarvo, True)
    
    def test_ota_rahaa_metodi_palauttaa_false_jos_rahat_eivat_riittaneet(self):
        palautusarvo = self.maksukortti.ota_rahaa(20)
        self.assertEqual(palautusarvo, False)