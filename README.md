# PraxisseminarSS23
##  Automatic Grocery Scanner
### Inhalt:
-GroceryProgramm enthält das eigentliche Programm, sowie das trainierte Modell des Projektes

-HelperProgramms: Zusätzliche Programme, die im Laufe des Projektes entstanden sind.

-ImageDetectionValidationData: Die Validation, die am Ende des Trainings des models von Yolov8 erstellt wurde.

-ValidationOfOurProgram: Enthält die Excel, die zur Validierung benutzt wurde, das Log der Command-Line Ausgaben und den Text zur Validierung

-OrdnerDokumentation: Lastenheft, Pflichtenheft; Projektdokumentation_Praxisseminar; ProjektmanagementDokumentation;




## So wird das Programm installiert:
Um das GroceryProgramm nutzen zu können, müssen mehrere Voraussetzungen erfüllt sein.

   1) Der PC muss Python-Code ausführen können.
    2) Yolov8 muss installiert sein.
      
Abgesehen davon kann das Lebensmittelprogramm sofort verwendet werden.

Installation von Yolov8
    Es gibt verschiedene Möglichkeiten, Yolov8 zu installieren. Sie sind auf der Ultralitics-Website zu finden: 
    [https://docs.ultralytics.com/quickstart/]
    Wenn der Computer pip-fähig ist, ist eine Möglichkeit, den Befehl einzugeben: "pip install ultralytics" 
    in ein Shell- oder Python-Programm eingeben. yolov8 wird dann automatisch zusammen mit seinen Abhängigkeiten installiert.
    Um die Installation zu überprüfen, können die folgenden Befehle in Python verwendet werden.
        >>import torch
        >>torch.__version__
    Wenn die Endung der Version CPU enthält, handelt es sich um die Version, die die CPU verwendet. Wenn die Endung 
    cu enthält, handelt es sich um die Version, die die GPU nutzen kann. Für das Training ist die CPU-Version 
    langsam, aber für die Verwendung im GroceryProgramm sollte sie ausreichend sein.
    
## Wie man das Programm benutzt
    Um das Lebensmittelscanningprogramm zu starten, öffnen Sie ein Befehlsterminal im Ordner GroceryProgram, in dem sich die Datei start.py befindet.
    Eine Möglichkeit, das Programm zu starten, ist die Verwendung des folgenden Befehls:
        >>python start.py
    Das Programm fragt nach vier Eingaben. Die BarcodeID, das Gewicht, das obere Bild und das seitliche Bild
    -Die BarcodeID kann 0-9 für die zehn verschiedenen Produkte sein. Die Produkte sind in der Datei product.json 
    Datei aufgelistet, zusammen mit ihren BarcodeIDs. Die BarcodeID -1 steht für no-barcode. Nur wenn no-barcode angegeben wird 
    wird das Programm die Bilderkennung verwenden? Damit soll der Vorschlag aus der Präsentation umgesetzt werden, 
    nämlich die Bilderkennung nur für Produkte ohne Barcode, wie z.B. Obst, zu verwenden. Einige der 
    Produkte, für die wir die Bilderkennung trainiert haben, haben tatsächlich Barcodes, wie die Tomatendose, aber wenn die 
    BarcodeID -1 eingegeben wird, tut das Programm so, als hätten sie keine Strichcodes und seien Früchte. 
    Dies geschah, weil uns die nötige Zeit fehlte, um 6400 Bilder von Produkten mit Barcode
    durch Bilder von Früchten zu ersetzen. Die Bilder müssten nicht nur neu aufgenommen werden, sondern auch neu beschriftet werden 
    und die KI müsste neu trainiert werden.
    -Das Gewicht. Da es sich nur um ein Programm und nicht um das eigentliche Gerät handelt, ist keine Waage implementiert und 
    der Benutzer gibt das Gewicht von Hand ein. Die Gewichtsbereiche der Produkte finden sich wiederum in der 
    der Datei product.json.
    -Die Bilder von oben und von der Seite. Diese stellen die Bilder dar, die die Kameras des Geräts aufgenommen hätten. 
    Die Bildquelle kann verschiedene Formate haben.
        1. Vollständiger Dateipfad
        2. Relativer Dateipfad
        3. Name.fileType, wenn die Datei im Bilderordner abgelegt ist
        4. Name, wenn es sich im Bilderordner befindet und ein .jpg ist (nicht bei .JPG)
        Das Programm wird dann eine der folgenden Antworten geben.
        -Wenn die Eingaben und das in den beiden Bildern erkannte Objekt übereinstimmen, wird das Programm 
        den Preis des Produkts aus.
        -Wenn die Bilderkennung ein Objekt mit mehr als 60 % Sicherheit nicht finden konnte,
        Es wird geschrieben: "Kein Produkt erkannt". Aber wenn das Gewicht höher als 0 ist, wird es auch geschrieben:
        "Aber die Waage wurde aktiviert."
        -Wenn mehr als ein Objekt in einem Bild erkannt wird, dann wird geschrieben: "Bitte legen Sie nur einen 
        Gegenstand auf einmal auf das Förderband legen."
        -Wenn für zwei Bilder unterschiedliche Objekte erkannt wurden, vergleicht das Programm die 
        das Programm die Konfidenz der beiden Objekterkennungen, wobei es berücksichtigt, ob sie auch mit der Höhe übereinstimmen, die der 
        die der Benutzer dem Programm gegeben hat. Abhängig von diesen beiden Kriterien wählt das Programm eines der 
        zwei erkannten Objekte.
        -Wenn das vom Benutzer angegebene Gewicht außerhalb des Bereichs des gewählten erkannten Objekts liegt, schreibt das Programm entweder 
        schreibt das Programm entweder "Das Produkt ist zu leicht" oder "Das Produkt ist zu schwer". 
        der einzelnen Objekte sind auch in der Datei product.json zu finden.
        


# !!! Linux!!!
 Das Programm wurde für Linux entwickelt, speziell für Linux Mint 21.2 Cinnamon.
    Für andere Betriebssysteme wie Windows oder Mac wird es wahrscheinlich nicht funktionieren, da sie andere Pfadstrukturen haben.
     
## Teammitglieder:
Thomas Hofbauer
Stefan Röhr


