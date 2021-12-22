# CoWallet #
Sovelluksen avulla käyttäjät voivat pitää kirjaa ryhmän sisäisestä taloudesta, joka syntyy kun ostetaan ryhmässä jotain yhteisiä palveluita ja tarvikkeita. Käyttöskenaario voisi olla esimerkiksi, kun kaveriporukka lähtee yhdessä mökkireissulle, jossa ihmiset ostavat yhteiskäyttöön erilaisia hyödykkeitä. Mökkivuokra maksetaan tietenkin tasan, joka on helppoa, mutta kun aletaan ostamaan ruokia, juomia, snackeja, tarvikkeita, bensoja jne. alkaa summien laskeminen olemaan monimutkaisempaa, ja yleensä tyydytään jonkinlaiseen sinnepäin ratkaisuun. Ehkä osa syö vain kasviruokaa, ehkä kaikki ei tullut autolla eli ei maksa bensoja, ehkä joku tykkää juuri tietystä sipsistä, ehkä jokin pienempi osaryhmä haluaa ostaa keskenään jonkin erikoisen pullon viskiä, ehkä osa halusi maksaa lisää ja vuokrata paljun heille lisäksi tms. Kaikki nämä on hyvin uniikkeja juuri tämän ryhmän sisäisiä ominaisuuksia, ja ne on ratkaistava case-by-case tyylillä juuri tämän kyseisen reissun tai kokoontumisen ajalta.

CoWallet on sovellus, joka pyrkii ratkaisemaan juuri tämän ongelman. Sovelluksessa käyttäjät voivat luoda keskenään ryhmiä eli klikkejä ("clique"), ja jokainen ryhmän jäsen voi lisätä ryhmälle ostoksia. Klikki voi olla mikä tahansa ryhmä joka jakaa minkä tahansa kokoelman menoja. Se voi olla esimerkissämme koko mokkireissun ryhmä, se voi olla jokin sen aliryhmä, tai se voi olla yhdistelmä näitä. Nämä ryhmät yhdessä ratkaisevat tämän taloudenpito ongelman. Sovellus laskee ryhmän sisäisesti sen velat, ja ilmoittaa sen jäsenille kuinka paljon he joko ovat velkaa ryhmälle, tai kuinka paljon ryhmällä on maksettavaa käyttäjälle. Kun tulee velan tasauksen hetki, voivat käyttäjät maksaa velkansa, jonka jälkeen sovellus suuntaa maksetut varat niiden oikeille omistajilleen.

## Huomio Python-versiosta ##
Sovellus on testattu toimivaksi Pythonin versiolla '3.8'. Tämän kyseisen, tai sitä uudemman Python-version käyttö sovellusta suoritettaessa on hyvin suositeltavaa. Vanhemmilla Python-versioilla saattaa ilmentyä ongelmia.

## Releaset ##
- [Viikko 6](https://github.com/xTanzu/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio ##
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [määrittelydokumentti](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [työaikakirjanpito](./dokumentaatio/tyoaika.txt)



## Sovelluksen käynnistäminen ##
Sovellus käyttää poetry-virtuaaliympäristöä. Poetry asennusohjeet löydät [täältä](https://python-poetry.org/docs/).

1. Asenna poetry koneellesi.

2. Ennen sovelluksen ensimmäistä käynnistykertaa, siirry komentorivillä `coWallet`-kansioon ja asenna sovelluksen riippuvuudet potryn avulla komennolla:
```
poetry install
```
3. Käynnistä sovellus komennolla:
```
poetry run invoke start
```





## Komentorivitoiminnot ##
### Sovelluksen käynnistäminen ###
Sovelluksen pystyy suorittamaan komennolla:
```
poetry run invoke start
```

### Testaus ###
Sovelluksen testit suoritetaan komennolla:
```
poetry run invoke test
```

### Testikattavuus ###
Komentoriville tulostettavan testikattavuusraportin saa tulostettua komennolla:
```
poetry run invoke coverage-report
```
Html-tiedostoon tulostettavan testikattavuusraportin saa tulostettua komennolla:
```
poetry run invoke coverage-html-report
```
Raportti luodaan sovelluskansion juureen kansioon `htmlcov`, ja sen saa käynnistettyä avaamalla index.html tiedoston selaimella

### Pylint-laatutarkistus ###
Tiedoston .pylint kuvatut koodin laatutarkistukset voi suorittaa komennolla:
```
poetry run invoke lint
```

Jatketaan tästä
