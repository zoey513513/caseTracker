from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

web = "https://www.audible.com/search"
path = "/Users/yan/Documents/SDW/webscrape"

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(web)
pagination = driver.find_element(By.XPATH,'//ul[contains(@class,"pagingElements")]')
lastpage = pagination.find_elements(By.XPATH,'.//li')[-2].text
book_tiltes = []
book_authors = []
book_runtimes = []
currentpage = 1
while currentpage <= int(lastpage):
    time.sleep(2) # give web enough time to render the page, more robust code
    container =driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
    books = container.find_elements(By.XPATH,'./div/span/ul/li')

    for book in books:
        book_tilte = book.find_element(By.XPATH,'.//h3[contains(@class,"bc-heading")]').text
        book_tiltes.append(book_tilte)
        book_author = book.find_element(By.XPATH,'.//li[contains(@class,"authorLabel")]').text
        book_authors.append(book_author)
        book_runtime = book.find_element(By.XPATH,'.//li[contains(@class,"runtimeLabel")]').text
        book_runtimes.append(book_runtime)
    currentpage += 1
    try:
        nextButton = container.find_element(By.XPATH,'//span[contains(@class,"nextButton")]')
        nextButton.click()
    except:
        pass

df = pd.DataFrame({'book_tiltes':book_tiltes, 'book_authors':book_authors, 'book_runtimes':book_runtimes})
df.to_csv('booklist.csv', index=False)

driver.quit()