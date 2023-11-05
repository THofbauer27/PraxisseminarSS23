from ultralytics import YOLO
import os
import json 

#Variable setup
dir_path = os.getcwd()
model = YOLO("./model.pt")
topDouble = False
sideDouble = False
nameT =""
nameS =""
dataT ={'productName': 'Error', 'barcodeID': -2, 'wheightMin': 1, 'wheightMax': 0, 'price': 0}
dataS ={'productName': 'Error', 'barcodeID': -2, 'wheightMin': 1, 'wheightMax': 0, 'price': 0}
confidenceT = 0
confidenceS = 0
dataB =""
minimalConfidence = 0.6
confidenceBoost = 0.2
resultEntryNum = 0
shapeNum = 0
maxObjectNum = 1
scaleThreshold = 0
with open(r'./product.json','r') as f:
    data=json.load(f) 
firstChar = ":1"

#Input
print("Barcode: ")
barcode = int(input())
print("Wheight: ")
wheight = float(input())

#handle different types of image input for the Top Image
print("Top Image")
tImage = input()
if tImage[:1] == "/":
    tImage = tImage
elif tImage[:1] == ".":
    tImage = tImage
elif tImage[-4:] == ".jpg":
    tImage = dir_path + "/pictures/"  + tImage
else: 
    tImage = dir_path + "/pictures/" + tImage+ ".jpg"

#handle different types of image input for the Top Image
print("Side Image")
sImage = input()
if sImage[:1] == "/":
    sImage = sImage
elif sImage[:1] == ".":
    sImage = sImage
elif sImage[-4:] == ".jpg":
    sImage = dir_path + "/pictures/" + sImage
else: 
    sImage = dir_path + "/pictures/" + sImage + ".jpg"


#function to decide output
def decideOutput(fData):
    if wheight < fData['wheightMin']: 
        print("Product is to light")
    elif wheight > fData["wheightMax"]:
        print("Product is to heavy")
    else:
        print("Product costs: "+str(fData["price"]))

#Barcode wurde angegeben. Daher keine Bilderkennung->
if barcode >= 0:
    for entry in data["default"]:
        #print("ID: "+ str(entry["barcodeID"])+ " " + str(barcode))
        if entry["barcodeID"] == barcode:
            dataB = entry
            decideOutput(dataB)            
            break 

#Kein Barkode angegeben->
else:
    #get image Recognition data for the top image.    
    resultT = model.predict(source=tImage)
    detection_countT = resultT[resultEntryNum].boxes.shape[shapeNum]
    if detection_countT >maxObjectNum:
        topDouble = True    
    for i in range(detection_countT):
        cls = int(resultT[resultEntryNum].boxes.cls[i].item())
        nameT = resultT[resultEntryNum].names[cls]
        confidenceT = float(resultT[resultEntryNum].boxes.conf[i].item())

    #get image Recognition data for the Side image.
    resultS = model.predict(source=sImage)
    detection_countS = resultS[resultEntryNum].boxes.shape[shapeNum]
    if detection_countS >maxObjectNum:
        sideDouble = True    
    for i in range(detection_countS):
        cls = int(resultS[resultEntryNum].boxes.cls[i].item())
        nameS = resultS[resultEntryNum].names[cls]
        confidenceS = float(resultS[resultEntryNum].boxes.conf[i].item())


    #Check if atleast one Image detection has more than the minimum confidence value.
    if (confidenceT<minimalConfidence and confidenceS<minimalConfidence) or (nameT=="" and nameS==""):
        print("No Product Recognized")
        if wheight >scaleThreshold:
            print("But Scale was activated.")
    #Check that every image only contains one object.
    elif topDouble == True or sideDouble== True:
        print("Please only place one Item at a time on the conveyor belt.")
    #Get the corresponding json entry for the detected Object
    else:
        for entry in data["default"]:
            if entry["productName"] == nameT:
                dataT = entry
                break 

        for entry in data["default"]:
            if entry["productName"] == nameS:
                dataS = entry
                break 



        #If both images contained the same object, the decide output function is called->
        if nameT == nameS:
            decideOutput(dataT)
        else:

            #if the two differing objects were detected, the level of confidence is compared, taking into acount if the wheight in the Json entry matches the measured wheight.->
            if dataT['wheightMin'] < wheight and wheight >dataT["wheightMax"]:
                confidenceT=confidenceT + confidenceBoost
            if dataS['wheightMin'] < wheight and wheight >dataS["wheightMax"]:
                confidenceS=confidenceS + confidenceBoost
            #Deciding which version to send to the decide output function
            if confidenceT > confidenceS:
                decideOutput(dataT)
            else:
                decideOutput(dataS)
       
