info= {
    "NAME": "GARGI",
    "CLASS": "9-C",
    "ROLL NO.": 12,
    45 : "HELLO GARGI"
    }
print(info)
print (type(info))

#PRINT A PERTICULAR VALUE
print(info[45])

#TO ASSIGN A NEW VALUE
info["NAME"]="AADITYA"
print(info)

#OPERATIONS ON DICTIONARY

dict_1= {
    "name": "Gargi",
    "class": "10-A",
    "roll no.":12,
}

print(dict_1.keys())            #to print all the keys of a dictionary

print(list(dict_1))            #convertion of dictionary to list

print(dict_1.values())          #to print all the values of the dcitionary

print(dict_1.items())           #to print all the items

print(dict_1.get("name"))       #to get the value of a specific key

dict_1.update({                 #to update the value in existing dictionary
    "city":"New Delhi"
})
print(dict_1)