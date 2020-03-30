
# Importing libraries
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# initiating lists
product = []
link = []

# scraping data
for i in range(1,14):
    Soup_html = get("https://www.stihlusa.com/products/stihl-top-rated-products/?page="+str(i))
    soup = BeautifulSoup(Soup_html.text,"html.parser")
    for k in soup.find_all(class_=["clickable-product"]):
        product.append(k.get("data-name"))
    for p in soup.find_all(class_=["clickable-product-element"]):
        link.append(p.get("href"))


#creating dataframe
df = pd.DataFrame({"product_name":product,"product_url":link[0::2]})
df.to_excel("SthilUSA")
df.to_csv('product.csv',index=False)

