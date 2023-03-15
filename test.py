# File for me to test features
from semantic3.units import ConversionService
from semantic3.solver import MathService
from semantic3.numbers import NumberService
from mathparse import mathparse

service1 = MathService()
service2 = NumberService()
print(service2.longestNumber("Seven and a half kilograms to pounds"))


# 4.70048

service = ConversionService()

print(service.convert("Seven and a half kilograms to pounds"))
# (16.534, 'lbs')

print(service.convert("Seven and a half pounds per square foot to kilograms per meter squared"))
# (36.618, 'kg/m**2')

# print(service.convert("How is your day"))
# (16.534, 'lbs')

def get_bot_response():
    userText = input("> ")
    try:
        convertedUnits = service.convert(str(userText))
        UnitsMsg = str(service2.longestNumber(userText)) + str(service.extractUnits(userText)[0]) + """ -> """ + str(convertedUnits)
        return UnitsMsg
    except:
        try:
            math = mathparse.parse(userText, language='ENG')
            return "Maths: " + str(math)
        except:
            if "what is" in userText.lower():
                return str(search(userText))
            elif "what's" in userText.lower():
                return str(search(userText))
            elif "near me" in userText.lower():
                return str(search(userText))
            elif "who is" in userText.lower():
                return str(search(userText))
            elif "who was" in userText.lower():
                return str(search(userText))
            else:
                return str(bott.get_response(userText)).title()
            
print(get_bot_response())