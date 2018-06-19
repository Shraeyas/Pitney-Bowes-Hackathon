from flask import Flask, render_template, request, jsonify
import FAQbot
app = Flask (__name__)

@app.route ('/')
def homepage ():
    return render_template ('bot.html')

if __name__ == '__main__':
    app.run ()
