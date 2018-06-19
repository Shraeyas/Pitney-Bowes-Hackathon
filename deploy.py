from flask import Flask, render_template, request, jsonify
import FAQbot
app = Flask (__name__)

@app.route ('/')
def homepage ():
    return render_template ('bot.html')

@app.route ('/api/bot', methods = ['POST'])
def say_name ():
    json = request.get_json ()
    class_, question, response, suggestions = FAQbot.chat (json['query'])

    dict = {}
    for i in range (0, len(suggestions)):
        dict[str(i)] = (suggestions[i][0])

    return jsonify (type = class_, ques = question, answer = response, suggest = dict)

if __name__ == '__main__':
    app.run ()
