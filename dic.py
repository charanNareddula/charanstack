camdic = {
        "cam1" : "entrance",
        "cam1" : "Hall",
        "cam3" : "living room",
        "cam4" : "Dining room"
    }
print(dir(dict))
print(type(camdic))
camdic.update({"cam5" :"parking"})
del camdic['cam3']
print(camdic)
for key, values in camdic.items():
    print(type(key), type(values))
    print(key , values)

