import math
def kosten_berekening_vloerder():
    aantal_projecten_per_week = int(input("Hoeveel projecten doe je per week? "))
    for i in range(1,aantal_projecten_per_week+1):
        werkuren_lijst = []
        prijs_project = []
        week_uren = []
        week_prijs_incl_btw = []
        week_prijs_exl_btw = []
        aantal_werkuren = 0
        print(f"--- Project {i} --- ")
        bouwjaar_huis = int(input("Wat is het bouwjaar van het huis?"))
        if bouwjaar_huis <= 6:
            btw_percentage = 0.06
        else:
            btw_percentage = 0.21
        aantal_vloeren = int(input(f"Hoeveel kamers in project {i}?"))
        for j in range(1,aantal_vloeren+1):
            prijs_tegels = 0
            prijs_plinten = 0
            lengte = int(input(f"Wat is de lengte van kamer {j}?"))
            breedte = int(input(f"Wat is de breedte van kamer {j}?"))
            uitbreken = input(f"Moet kamer {j} eerst uitgebroken worden? ja/nee")
            maat_tegels = input("""Welke maat tegels is er gevraagd?    
                                   a: 30x30cm
                                   b. 40x40 cm
                                   c. 50x50 cm """)
            plinten = input("Moeten er ook plinten geplaats worden? ja/nee")
            if plinten.lower() == "ja":
                prijs_plinten = ((2*lengte) + (2*breedte)) * 10
            if maat_tegels.lower() == "a":
                prijs_tegels = (lengte*breedte)* 10
            elif maat_tegels.lower() == "b":
                prijs_tegels = (lengte*breedte)* 12.5
            elif maat_tegels.lower() == "c":
                prijs_tegels = (lengte*breedte)* 15
            else:
                print("tegelprijs niet gevonden, kies een geldige maat")
            if uitbreken.lower() == "ja":
                aantal_werkuren += (lengte * breedte) / 9
            aantal_werkuren += (lengte * breedte) / 12
            werkuren_lijst.append(math.ceil(aantal_werkuren))
            prijs_per_vloer = ((math.ceil(aantal_werkuren)*45) + prijs_tegels + prijs_plinten)
            prijs_project.append(prijs_per_vloer)
            btw_project = sum(prijs_project)*btw_percentage
        print(f"De hoeveelheid werkuren van dit project zijn: {werkuren_lijst}, in totaal {sum(werkuren_lijst)} uur werk")
        week_uren.append(sum(werkuren_lijst))
        week_prijs_exl_btw.extend(prijs_project)
        week_prijs_incl_btw.append(float(sum(prijs_project))+btw_project)
    print(f"De kostprijs van de projecten van deze week bedragen {week_prijs_incl_btw}, in totaal {sum(week_prijs_incl_btw)}")
    print(f"Het duurste project kostte {max(week_prijs_incl_btw)} euro")
    print(f"Totale omzet van deze week is {float(sum(week_prijs_exl_btw))} euro")
kosten_berekening_vloerder()