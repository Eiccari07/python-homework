
import json


def lue_paikat(nimet):
    paikat = {}

    for nimi in nimet:
        tiedostonimi = nimi + ".json"

        with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
            tiedot = json.load(tiedosto)

        paikat[nimi] = tiedot

    return paikat
