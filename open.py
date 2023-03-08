import os
import json

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def decode_json(file):
    file = open('commonsense.json', 'r')
    json_decoded = json.load(file)
    for item in json_decoded:
        dict = {}
        dict['question'] = item.get('question').get('stem')
        correctAnswer = item.get('answerKey')
        for choice in item.get('question').get('choices'):
            if item.get('question').get('choices').get('label') == correctAnswer:
                