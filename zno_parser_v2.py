# coded by Radiazz
import urllib
import urllib.request
import os
from bs4 import BeautifulSoup

def main():
    mainLINK = input("Введите ссылку на ЗНО по математике: ")
    webUrl = urllib.request.urlopen(mainLINK)
    print("result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    soup = BeautifulSoup(data, "html.parser")
    for pre_link in soup.find_all("div", class_="explanation"):
      link = pre_link.find_all("img")[0]["src"]
      file_name = link.split('math-')[-1] if len(link.split('math-')) > 1 else link.split('/')[-1];
      urllib.request.urlretrieve("https://zno.osvita.ua" + link, __file__.split(os.path.basename(__file__))[0] + "/" + file_name)
      print(link)
 
if __name__ == "__main__":
  main()