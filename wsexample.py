from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/sony-alpha-ilce-6100y-aps-c-mirrorless-camera-dual-lens-16-50-mm-55-210-zoom-featuring-eye-af-4k-movie-recording/p/itm"

response = requests.get(url)
htmlcontent = response.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    title = d.find('div', attrs={'class':'_4rR01T'})
    # print(title.string)

    price = d.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # print(title.string)

    image = d.find('img', attrs={'class':'_396cs4 _3exPp9'})
    # print(image.get('src'))

    titles.append(title.string)
    prices.append(price.string)
    images.append(image.get('src'))

    print(titles)
    print(prices)
    print(images)