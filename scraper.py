from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from curl_cffi import requests

link = "https://safebooru.org/index.php?page=post&s=list&tags=sunset"

images = []
response = requests.get(link, impersonate="chrome")
html_doc = response.text
img_tags = SoupStrainer("img")  

soup = BeautifulSoup(html_doc, "html.parser", parse_only=img_tags)

for img in soup:
    images.append(img.get("src"))

newImages = [img for img in images if img.startswith("http")]

for i in range(len(newImages)):
    image_response = requests.get(newImages[i], impersonate="chrome")
    image_data = image_response.content
    with open(f"images/output_image-{i}.jpg", "wb") as file:
        file.write(image_data)
