# File for me to test features
from semantic3.units import ConversionService
from semantic3.solver import MathService
from semantic3.numbers import NumberService
from mathparse import mathparse
import rottentomatoes as rt

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


            


userText=input()
rtlk = rt.tomatometer(userText)
print(str(rt.movie_title(userText)) + " ("+rt.rating('everything everywhere all at once')+", "+rt.year_released(userText)+")"+": Tomatometer - " + str(rtlk['value']) + "% "  + "Audience - " + str(round((float(rt.audience_score(userText)['averageRating']) / 5) * 100, 0)))
