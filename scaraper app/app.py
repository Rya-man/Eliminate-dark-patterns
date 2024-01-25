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
    product_data = {
        'product_name': "place holder hfbfbsf",
        'product_image': 'https://img.freepik.com/premium-vector/photo-icon-picture-icon-image-sign-symbol-vector-illustration_64749-4409.jpg',
        'product_description': sc.get_content(decoded_url),
        "product_price":"6969"
    }
    
    #return sc.get_content(decoded_url)
    return render_template("product.html", **product_data)
if __name__ == '__main__':
    app.run(debug=True)
