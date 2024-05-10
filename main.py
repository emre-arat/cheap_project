from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.minimize_window()
def trendyol_search(product):
    driver.get("https://www.trendyol.com/")
    search_box = driver.find_element(By.CLASS_NAME,"V8wbcUhU")
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)
    fiyat = driver.find_elements(By.CLASS_NAME,"prc-box-dscntd")

    for x in fiyat:
        print(f"Trendyol da '{x.text}' sonuç buldum." )




def hepsiburada_searh(product):
    driver.get(f"https://www.hepsiburada.com/ara?q={product}")
    source = driver.page_source
    source_list = source.split("<div")
    for x in source_list:
        if "price-current-price" in x:
            a_list = x.split(">")[1].split("<")[0]
            print(f"Hepsiburada da '{a_list}' sonuç buldum.")




def n11_search(product):
    driver.get("https://www.n11.com/")
    search_box = driver.find_element(By.ID,"searchData")
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)
    fiyat = driver.page_source.split("<ins>")
    for x in fiyat[1:]:
        fin_item = x.split("</ins")[0]
        print(f"N11 de '{fin_item}' sonuç buldum.")

user_input = input("Enter a product: ")
trendyol_search(user_input)
hepsiburada_searh(user_input)
n11_search(user_input)

driver.close()

