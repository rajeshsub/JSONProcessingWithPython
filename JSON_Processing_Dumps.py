import json

data = {
    "FirstName":"Bhairav",
    "MiddleName":"S",
    "LastName":"Ram",
    "DateOfBirth":"09-01-1984",
    "Contact":{
        "Phone":9988776655,
        "Email":"bhairav@gmail.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":560056,
            "Street":"Nagarbhavi Road",
            "City":"Bangalore",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":560004,
            "Street":"Gandhi Bazaar Road",
            "City":"Bangalore",
            "Country":"India"
        }
    ]
}

#json.dumps() method turns a Python data structure into JSON:
jsonData = json.dumps(data, indent=4)
print(jsonData)

# Writing JSON data into a file called JSONData.json
outputFile = open("JSONData.json", "w+")
	outputFile.write(jsonData)
