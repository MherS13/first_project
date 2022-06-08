import requests
import threading
import os
import json
import time

""" Creating web_images folder for saving images in this folder and reading JSON file. """

try:
    os.mkdir("web_images")
except FileExistsError:
    pass

with open("task_urls.json") as file:
    urls = json.load(file)
path = "web_images"


"""Saving images in 'web_images' folder."""


def downloading(url, name):
    with open("web_images/" + "image" + name + ".png", "wb") as images:
        images.write(response.content)


start = time.time()

threads = []
for i, url in enumerate(urls["items"]):
    x = threading.Thread(target=downloading, args=(url["url"], str(i + 1)))
    try:
        response = requests.get(url["url"])
    except requests.exceptions.ConnectionError:
        print("Connection issues try again")
        break
    x.start()
    threads.append(x)

"""
   Working threads and check how many images was downloaded
   if no images downloaded delete 'web_images' folder.
"""

for loading in threads:
    loading.join()
if os.path.exists(path) and len(os.listdir(path)) == 0:
    print(f"Downloaded {len(os.listdir(path))} images")

end = time.time()

""" Checking program working time."""
print(end-start)
