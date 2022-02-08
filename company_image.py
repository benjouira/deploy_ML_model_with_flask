from bs4 import BeautifulSoup
import requests
import csv

def scrape_company_info(company="Dollar-General"):
    url = f"https://www.indeed.com/cmp/{company}/reviews?start=00"

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    company_image = soup.find("div", class_="css-1268hzc").find("img")['src']
    company_rating = soup.find("span", class_="css-htn3vt").text

    return (company_image, company_rating)

# ***********************************************************

# url = scrape_company_info()[0]

# from PIL import Image
# import requests
# from io import BytesIO

# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# img.show()

# import requests, io
# import matplotlib.pyplot as plt 

# response = requests.get(url).content
# img = plt.imread(io.BytesIO(response), format='JPG')
# plt.imshow(img)