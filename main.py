from flask import Flask, render_template_string

app = Flask(__name__)

# Load index.html content
with open("index.html") as f:
    html_content = f.read()

@app.route("/")
def home():
    return render_template_string(html_content)

app.run(host='0.0.0.0', port=3000)
