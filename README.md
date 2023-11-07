# PraxisseminarSS23
##  Automatic Grocery Scanner
### Inhalt:
-grocery programm enthält das eigentliche Programm, sowie das trainierte Modell des Projektes
-Helper Programms: Zusätzliche Programme, die im Laufe des Projektes entstanden sind.
-ImageDetectionValidationData: Die Validation, die am Ende des Trainings des models von Yolov8 erstellt wurde.
-ValidationOfOurProgram: Enthält die Excel, die zur Validierung benutzt wurde, das Log der Command-Line Ausgaben und den Text zur Validierung
-OrdnerDokumentation: Lastenheft, Pflichtenheft; Projektdokumentation_Praxisseminar; ProjektmanagementDokumentation;




## How to install the Program:
In order to use the GroceryProgramm multiple prerequisites have to be met.
    1.The PC needs to be able to execute Python code.
    2.Yolov8 must be installed.
Otherwise, the grocery program can be immediately used.

Installation of Yolov8
    There are different ways of installing Yolov8. They can be found on the Ultralitics website: 
    [https://docs.ultralytics.com/quickstart/]
    If the Computer is capable of using pip one way is to type the command: "pip install ultralytics" 
    in a Shell or Python program. yolov8 will automatically be installed along with its dependencies.
    To verify the installation, the following commands can be used in Python.
        >>import torch
        >>torch.__version__
    If the ending of the version contains CPU it is the version that uses the CPU. If the ending 
    contains cu it is the  version that can utilize the GPU. For training, the CPU version is 
    slow, but for use in the GroceryProgram it should be sufficient.
    
## How to use the Program
    To Start the Grocery Program, open a command terminal in the GroceryProgram folder, where the start.py file is.
    One way to start the program is to use the following command:
        >>python start.py
    The program will ask for four inputs. The BarcodeID, the Weight, the top image, and the side image
    -The BarcodeID can be 0-9 for the ten different Products. The Products are listed in the product.json 
    file, along with their BarcodeIDs. The BarcodeID -1 stands for no-barcode. Only if no-barcode is given 
    will the Program use the image detection? This is to incorporate the sugestion made during the Presentation, 
    as to only use the Image detection for Products without Barcodes, like Fruits. Some of the 
    Products we trained the Image detection on do in fact have barcodes, like the can of tomatoes, but when the 
    BarcodeID -1 is entered, the program will pretend that they do not have Barcodes and are frute. 
    This was done because we lacked the necessary time to replace 6400 Images of Barcode having products
    with images of fruits. Not only would the Images have to be retaken, but they would also have to be relabeled 
    and the AI would have to be retrained.
    -The weight. Since this is only a program and not the actual device, no scales are implemented and 
    the User enteres the weight by hand. The ranges of weights of the Products can again be found in 
    the product.json file.
    -The top and side images. These represent the images the cameras of the device would have taken. 
    The image source can have different formats.
        1. Complete file path
        2. Relative file path
        3. Name.fileType if it is placed in the pictures folder
        4. Name if it is placed in the pictures folder and is a .jpg(not if .JPG)
    The Program will then give one of the following responses.
        -If the inputs and the Object detected in the two images fit, the Program will 
        write the Price of the Product.
        -If the Image detection could not find an object with more than 60% confidence,
        It will write, "No Product Recognized." But if the weight is higher than 0 it will also write:
        "But Scale was activated."
        -If more than one object is detected in an image, then it will write: "Please only place one 
        Item at a time on the conveyor belt."
        -If for the two images, different objects have been detected, the Program will compare the 
        confidence of the two object detections, taking into account whether they also match the height 
        the user gave the program. Depending on those two criteria, the program will choose one of the 
        two detected objects.
        -If the weight given by the user falls outside the range of the chosen detected Object, the 
        program will write either "Product is to light" or "Product is too heavy" The weight ranges 
        of each object can also be found in the product.json file.
        


# !!! Linux!!!
    The Program was developed for Linux, specifically Linux Mint 21.2 Cinnamon.
    For different operating systems like Windows or Mac, it will likely not work, since they have different Path structures.
     
## Teammitglieder:
Thomas Hofbauer
Stefan Röhr


