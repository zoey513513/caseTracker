from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By class
import pandas as pd


web = "https://www.audible.com/search"
path = "/Users/yan/Documents/SDW/webscrape"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(web)
driver.maximize_window

container =driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
books = container.find_elements(By.XPATH,'./div/span/ul/li')
book_tiltes = []
book_authors = []
book_runtimes = []
for book in books:
    book_tilte = book.find_element(By.XPATH,'.//h3[contains(@class,"bc-heading")]').text
    book_tiltes.append(book_tilte)
    book_author = book.find_element(By.XPATH,'.//li[contains(@class,"authorLabel")]').text
    book_authors.append(book_author)
    book_runtime = book.find_element(By.XPATH,'.//li[contains(@class,"runtimeLabel")]').text
    book_runtimes.append(book_runtime)
df = pd.DataFrame({'book_tiltes':book_tiltes, 'book_authors':book_authors, 'book_runtimes':book_runtimes})
df.to_csv('booklist.csv', index=False)

driver.quit()