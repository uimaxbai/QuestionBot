# from vardata import *
from search import *
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)