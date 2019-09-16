from selenium import webdriver
import random
import time

browser = webdriver.Chrome()

urls = []

entries = []

for i in range(0, 10):
    randomNumber = random.randint(1, 1719)
    urls.append("https://eksisozluk.com/mustafa-kemal-ataturk--34712?p={}".format(randomNumber))

for url in urls:
    browser.get(url)
    elements = browser.find_elements_by_css_selector('.content')
    for element in elements:
        entries.append(element.text)

eksiFile = open("100_random_eksi_entries.txt", "w", encoding = "utf-8")

for entry in range(0, len(entries)):
    if(entry % 10 == 0):
        eksiFile.write("**************************************************************************************\n")
        eksiFile.write("{}\n".format(urls[int(entry / 10)]))
        eksiFile.write("--------------------------------------------------------------------------------------\n")
    eksiFile.write("{}) {}".format(entry + 1, entries[entry]))
    eksiFile.write("\n________________________________________________________________________________________\n")
    
browser.close()
