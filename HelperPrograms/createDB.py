import json

dictionary = {
    "default": [
        {
            "productName": "AppleR",
            "barcodeID": 0,
            "wheightMin": 0.1,
            "wheightMax": 0.12,
            "price": 0.9
        },
        {
            "productName": "AppleG",
            "barcodeID": 1,
            "wheightMin": 0.1,
            "wheightMax": 0.12,
            "price": 0.9
        },
        {
            "productName": "DoseTomate",
            "barcodeID": 2,
            "wheightMin": 0.5,
            "wheightMax": 0.6,
            "price": 0.9
        },
        {
            "productName": "DoseWok",
            "barcodeID": 3,
            "wheightMin": 0.4,
            "wheightMax": 0.5,
            "price": 0.9
        },
        {
            "productName": "Vollmilch",
            "barcodeID": 4,
            "wheightMin": 1.0,
            "wheightMax": 1.2,
            "price": 0.9
        },
        {
            "productName": "Hafermilch",
            "barcodeID": 5,
            "wheightMin": 1.0,
            "wheightMax": 1.1,
            "price": 0.9
        },
        {
            "productName": "CornflakesJa",
            "barcodeID": 6,
            "wheightMin": 0.7,
            "wheightMax": 0.76,
            "price": 0.9
        },
        {
            "productName": "CornflakesDr",
            "barcodeID": 7,
            "wheightMin": 0.5,
            "wheightMax": 0.55,
            "price": 0.9
        },
        {
            "productName": "NudelnBarilla",
            "barcodeID": 8,
            "wheightMin": 0.6,
            "wheightMax": 0.66,
            "price": 0.9
        },
        {
            "productName": "NudelnBernbacher",
            "barcodeID": 9,
            "wheightMin": 0.5,
            "wheightMax": 0.6,
            "price": 0.9
        }
    ]
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to product.json
with open("product.json", "w") as outfile:
    outfile.write(json_object)


#AppleR, AppleG, DoseTomate, DoseWok, Vollmilch, Hafermilch, CornflakesJa, CornflakesDr, NudelnBarilla, NudelnBernbacher
