from flask import Flask, request, render_template
import scaraper as sc

app = Flask(__name__)



@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

@app.route('/<path:encoded_url>')
def hello_url(encoded_url):
    # Decode the URL
    decoded_url = request.path[1:]  # remove the leading '/'
    try:
        sc.get_code(encoded_url)
    finally:
        return render_template("output.html")
if __name__ == '__main__':
    app.run(debug=True)
