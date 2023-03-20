# Import modules
from search import *
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from semantic3.units import ConversionService
from semantic3.solver import MathService
from semantic3.numbers import NumberService
from mathparse import mathparse
import rottentomatoes as rt
import json

app = Flask(__name__)
service1 = MathService()
service = ConversionService()
service2 = NumberService()


# Declare chatbot
bott = ChatBot("Slangy Chatbot")

# Train on CommonSenseQA
# trainer3 = ListTrainer(bott)
# trainer3.train(commonsense)

# Simple conversation
conversation1 = [
    "Hello",
    "Hi, there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear!",
    "How can I help you?",
    "Thank you.",
    "You're welcome."
]

trainer2 = ListTrainer(bott)

trainer2.train(conversation1)

trainer = ChatterBotCorpusTrainer(bott)
# trainer.train("chatterbot.corpus.english")
# trainer2.train(["Thank You","You're welcome"])


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    try:
        try:
            rtlk = rt.tomatometer(userText)
            if rt.movie_title(userText).lower() != userText.lower():
                raise Exception("Not exact")
            return str(rt.movie_title(userText)) + " ("+rt.rating('everything everywhere all at once')+", "+rt.year_released(userText)+")"+": Tomatometer - " + str(rtlk['value']) + "% "  + "Audience - " + str(int(round((float(rt.audience_score(userText)['averageRating']) / 5) * 100, 0))) + "%"
        except Exception:
            try:
                convertedUnits = service.convert(str(userText))
                UnitsMsg = str(service2.longestNumber(userText)) + str(service.extractUnits(userText)[0]) + """ -> """ + str(convertedUnits)
                return UnitsMsg
            except Exception:
                try:
                    math = mathparse.parse(userText, language='ENG')
                    return "Maths: " + str(math)
                except Exception:
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

        return "Error: "+repr(err)+". This error has been reported."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)