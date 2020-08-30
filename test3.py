import urllib.request

url1 = "https://i.pinimg.com/736x/3c/7d/46/3c7d467e5831894576a66afa954876b8.jpg"
url2 = "https://ih1.redbubble.net/image.762606806.6231/st,small,507x507-pad,600x600,f8f8f8.jpg"
url3 = "https://i.pinimg.com/736x/b7/06/2a/b7062ac5c7ff89bffdfec874f1aab7e1.jpg"

urllistesi = [url1, url2, url3]
say = 1
for url in urllistesi:
    urllib.request.urlretrieve(url, "Resim"+str(say)+".jpg")
    say += 1
