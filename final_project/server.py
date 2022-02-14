from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    
    try:
        return machinetranslation.translator.english_to_french(textToTranslate)
    except:
        return "An exception occured"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    
    try:
        return machinetranslation.translator.french_to_english(textToTranslate)
    except:
        return "An exception occured"

@app.route("/")
def renderIndexPage():
    return "Machine translation webpage"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
