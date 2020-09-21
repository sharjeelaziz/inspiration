from pixabay import Image
import requests
import shutil
import random
import time
import os

API_KEY = os.getenv('API_KEY')

image = Image(API_KEY)

while True:
    for n in range(1,2):
        try:
            ims = image.search(
                q="streets",
                lang="en",
                image_type="all",
                orientation="all",
                category="all",
                min_width=0,
                min_height=0,
                colors="",
                editors_choice="false",
                safesearch="true",
                order="popular",
                page=n,
                per_page=200,
                callback="",
                pretty="true")
                
            imageUrls = []
            for i in range(0, 200):
                payload = ims['hits'][i]['largeImageURL']
                imageUrls.append(payload)
                    
            if imageUrls:
                for k in range(0,6):
                    selPayload = random.choice(imageUrls)
                    resp = requests.get(selPayload, stream=True)
                    local_file = open(str(k+1)+".jpg", 'wb')
                    resp.raw.decode_content = True
                    shutil.copyfileobj(resp.raw, local_file)
                    del resp
                    print(str(k) + "URL of image: {}".format(selPayload))
                        # urllib.request.urlretrieve(payload,i)
        except Exception as e:
            print(e)
        
        time.sleep(3660)