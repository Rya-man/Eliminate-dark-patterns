from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

app = Flask(__name__)

bart = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", truncation=True)

class Product:
    def __init__(self, link):
        self.link = link
        self.image = "https://rukminim2.flixcart.com/image/416/416/l2urv680/action-figure/d/p/w/3-batman-bobble-head-action-figure-head-stand-with-mobile-holder-original-image3ykdueb2t82.jpeg?q=70&crop=false"
        self.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

products_list = []
links = []

def get_products(query):
    r = requests.get(query)
    soup = BeautifulSoup(r.content, 'lxml')

    cols = soup.find_all("a", href=True)

    for i, col_entry in enumerate(cols):
        if ("marketplace=FLIPKART" in str(col_entry["href"])):
            link = "https://www.flipkart.com" + str(col_entry["href"])

            if (link not in links):
                links.append(link)
                product_instance = Product(link)
                products_list.append(product_instance)

def get_details(p):
    r = requests.get(p.link)
    soup = BeautifulSoup(r.content, 'lxml')

    try:
        p.image = soup.find("img", class_="_396cs4 _2amPTt _3qGmMb").get("src")
        p.description = soup.text
    except:
        pass

def get_webpage():
    web_page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #333;
            color: #fff;
        }

        .product {
            border: 1px solid #555;
            padding: 10px;
            margin-bottom: 20px;
            background-color: #444;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }

        .product img {
            max-width: 100%;
            height: auto;
        }

        .product a {
            text-decoration: none;
            color: #00aaff;
            font-weight: bold;
        }

        .product a:hover {
            color: #ffbb00;
        }

        #home-button {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            background-color: #00aaff;
            padding: 10px;
            border-radius: 5px;
            color: #fff;
            text-decoration: none;
        }

        #home-button:hover {
            background-color: #0077cc;
        }
        }
    </style>
</head>
<body>
    <a href="/" id="home-button">Home</a>

    <h1>Product List</h1>"""
    i = 0
    j = 0
    for product in products_list:
        get_details(product)

        if (product.image !=
                "https://rukminim2.flixcart.com/image/416/416/l2urv680/action-figure/d/p/w/3-batman-bobble-head-action-figure-head-stand-with-mobile-holder-original-image3ykdueb2t82.jpeg?q=70&crop=false"):
            product.description = bart(product.description[2000:])

            element = (f"""<div class="product">
            <h2>Product:</h2>
            <img src={product.image} alt="Product 1 Image">
            <p>Description:{product.description[0]['summary_text']}.</p>
            <p><a href="{product.link}" target="_blank">View Product</a></p>
        </div>""")
            j = j + 1

            web_page = web_page + element

        i = i + 1
        print(f"{i}/{len(products_list)} and {j} done")

        if (j == 5):
            break

    web_page = web_page + """</body></html>"""
    return web_page

def search(query):
    get_products(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    return get_webpage()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['search']
        return search(query)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
