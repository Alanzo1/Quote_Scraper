from bs4 import BeautifulSoup
import requests
import csv
#Variables
page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.find_all("span", attrs={"class":"text"})
authors = soup.find_all("small", attrs={"class":"author"})
#Csv setup
file = open("Scraped_Quotes.csv", "w")
writer = csv.writer(file)
#Rows 
writer.writerow(["QUOTES", "AUTHORS"])
#Loop to go through quotes and authors. 
for quote, author in zip(quotes,authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()