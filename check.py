# python code to check if a website is using shopify or not
#  to do this we check if a website contains shopify object
# We need to open the website and check if it contains shopify object
# if it does then it is using shopify

import requests
import sys


# get the website from the command line
website = sys.argv[1]

# open the website
r = requests.get(website)

# check if the website contains shopify object
if "shopify" in r.text:
    print("yes")    # if it does then print yes
    # get theme id and name from shopify object
    # get the shopify object
    shopify = r.text.split("Shopify.theme = ")[1].split(";")[0]
    # get the theme id
    theme_id = shopify.split('"id":')[1].split(",")[0]
    # get the theme name
    theme_name = shopify.split('"name":')[1].split(",")[0]
    # print the theme id and name
    print(theme_id)
    print(theme_name)
   

else:
    print("no")     # if it does not then print no

