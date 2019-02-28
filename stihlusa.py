
# coding: utf-8

# In[1]:


from requests import get
from bs4 import BeautifulSoup


# In[3]:


product = []
link = []
for i in range(1,14):
    Soup_html = get("https://www.stihlusa.com/products/stihl-top-rated-products/?page="+str(i))
    soup = BeautifulSoup(Soup_html.text,"html.parser")
    for k in soup.find_all(class_=["clickable-product"]):
        product.append(k.get("data-name"))
    for p in soup.find_all(class_=["clickable-product-element"]):
        link.append(p.get("href"))


# In[4]:


#creating dataframe
import pandas as pd
df = pd.DataFrame({"product_name":product,"product_url":link[0::2]})
#df.to_excel("SthilUSA")


# In[5]:


df.to_csv('product.csv',index=False)

