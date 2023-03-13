# File for me to test features
from semantic3.units import ConversionService
from semantic3.solver import MathService
from semantic3.numbers import NumberService

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