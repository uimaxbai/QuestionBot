import json

userText = "hey"

try:
    print(0 / 0)
except Exception as err:
        err_json = open("errors.json", "r")
        json1 = json.load(err_json)
        json1[str(json1['highestNumber']+1)] = {}
        json1[str(json1['highestNumber']+1)]["err"] = str(repr(err))
        json1[str(json1['highestNumber']+1)]["userData"] = userText
        json1["highestNumber"] = json1['highestNumber']+1

        err_json.close()
        err_json1 = open("errors.json", "w")
        json.dump(json1, err_json1)
        err_json1.close()
    
    