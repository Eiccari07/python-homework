
from paikat import lue_paikat
from pprint import pp

nimet = [
    "sisapiha",
    "teiskontien-aula",
    "palvelukatu",
    "tietotalon-aula",
    "juhlasali",
    "kuntokadun-aula"
]

paikat = lue_paikat(nimet)

pp(paikat)
