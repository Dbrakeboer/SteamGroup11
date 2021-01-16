# Steam Dashboard

Het Steam Dashboard maakt het mogelijk om uw eigen gamestatistieken op een overzichtelijke wijze in te zien. Daarnaast is het ook mogelijk om uw vriendenlijst te bekijken en te zien wie er binnen deze lijst online/offline is.

## Authors: 

Daniel Brakeboer - 1782643

Diederik Roovers - 1779316

Jelle Hille - 1785577

Giorgio Kersten - 1757974

## Installation Requirements

- Raspberry Pi
- Python IDE
- Libraries: json, tkinter, requests, matplotlib, RPi.GPIO, time, sys, pillow
- Hardware: servo, schuifregister, knop, afstandssensor, ledstrip, 4x led, breadboard en bijbehorende kabels

## Usage

* Voor de beste ervaring plaatst u de afstandssensor naast uw scherm met de sensor naar u zelf gericht. 

Na het installeren van bovenstaande benodigdheden kan "aisprint1.py" geopend worden via de gewenste IDE. Bovenaan de code kan het Steam ID ingevuld worden van de desbetreffende gebruiker. Zie hiervoor onderstaande afbeeldingen:

[Steam ID Finder](https://imgur.com/a/dFJpQH2)

[Steam User ID wijzigen](https://imgur.com/a/xSSwXSL)

Nadat het gewenste Steam ID ingevuld is kunt u "steam_dashboard_gui.py" openen. Wanneer deze gestart wordt zal de servo activeren om aan te geven dat alles goed geinstalleerd is. Zodra de servo stopt zal het welkomstscherm getoond worden met de naam behorend bij het ingevulde Steam ID en de online status. De aangesloten ledstrip zal van kleur veranderen zodra de online status veranderd. 

Na enkele seconden zal het hoofdmenu zichtbaar zijn. Onderaan zal wederom de online status getoond worden met de afstand tot het scherm. Het hoofdmenu bevat vier knoppen:

### *Most Played Games*
Binnen dit venster zal een top 5 weergegeven worden van de meest gespeelde games. Tevens zal de waarde van het account in euro's getoond worden met daaronder een histogram waarin de frequentie van de gespeelde uren van alle games (met een speeltijd 1-500 uur) zichtbaar is.

### *Friend List*
De linkerzijde van dit venster laat een lijst zien met alle vrienden van de gebruiker met hun online status op dit moment. De rechterzijde bevat een pie chart om dit overzichtelijk weer te geven.

### *Recently Played Games*
Alle games die in de afgelopen twee weken gespeeld zijn zullen in een lijst getoond worden met het aantal uur dat deze gespeeld zijn.

### *Exit Dashboard*
Sluit het dashboard. Dit kan ook gedaan worden middels de knop op het breadboard.

## Roadmap

Naar verwachting zullen in toekomstige versies onderstaande functies toegevoegd worden aan het dashboard:

- Meest gespeelde games bij vrienden zichtbaar maken 
- Populairste tijdstippen wanneer men games speelt zichtbaar maken

## Support/Feedback

Voor vragen of suggesties:

- daniel.brakeboer@student.hu.nl
