import requests
from bs4 import BeautifulSoup 
from transformers import pipeline


url=r"https://www.flipkart.com/search?q=notebook&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off" #url of site optimized for flipkart

bart = pipeline("summarization",model="sshleifer/distilbart-cnn-12-6",truncation=True)

class Product:
    def __init__(self, link):
        """
        Initialize a Product object.

        Parameters:
        - link (str): Link to the product.
        - image_src (str): Source file of the product image.
        - description (str): Description of the product.
        """
        self.link = link
        self.image = "https://rukminim2.flixcart.com/image/416/416/l2urv680/action-figure/d/p/w/3-batman-bobble-head-action-figure-head-stand-with-mobile-holder-original-image3ykdueb2t82.jpeg?q=70&crop=false"
        self.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

products_list=[] #empty list for product links
links=[]
def get_products(site):
    r = requests.get(site) #getting html
    #print(r)
    soup = BeautifulSoup(r.content, 'lxml') #parsing html

    cols=soup.find_all("a",href=True)  #getting links 
    #print(len(cols))

    for i, col_entry in enumerate(cols):
        if("marketplace=FLIPKART"  in str(col_entry["href"])):
            link = "https://www.flipkart.com" + str(col_entry["href"])
            

            if(link not in links):
                links.append(link)
            # Create a Product instance with the link
                product_instance = Product(link)

            # Append the product instance to the list
                products_list.append(product_instance)

def get_details(p):
    r=requests.get(p.link) #getting html of product page
    soup = BeautifulSoup(r.content, 'lxml') #parsing through html

    try:
        p.image=soup.find("img",class_="_396cs4 _2amPTt _3qGmMb").get("src")
        p.description=soup.text
    except:
        pass


def get_html():
    web_site=r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
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
    </style>
</head>
<body>
    <h1>Product List</h1>"""
    i=0
    j=0
    for product in products_list:
        get_details(product)

        
        if(product.image!="https://rukminim2.flixcart.com/image/416/416/l2urv680/action-figure/d/p/w/3-batman-bobble-head-action-figure-head-stand-with-mobile-holder-original-image3ykdueb2t82.jpeg?q=70&crop=false"):
            #products_list.remove(product)
            #print(product.image+"\n")
            #print(product.link+"\n\n")
            product.description=bart(product.description[2000:])  

            element=(f"""<div class="product">
            <h2>Product:</h2>
            <img src={product.image} alt="Product 1 Image">
            <p>Description:{product.description[0]['summary_text']}.</p>
            <p><a href="{product.link}" target="_blank">View Product</a></p>
        </div>""")
            j=j+1
            
            web_site=web_site+element
            

        i=i+1
        print(f"{i}/{len(products_list)} and {j} done")

        if(j==5):
            break
    
    web_site=web_site+"""</body></html>"""
    return web_site


#print(len(products_list))
def get_code(website):
    get_products(website)
    with open("templates/output.html", "w", encoding="utf-8") as file:
        file.write(get_html())

#get_code(url)