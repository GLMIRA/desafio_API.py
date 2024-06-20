from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from fastapi import FastAPI

app = FastAPI()



@app.get("/raspador")
def raspador():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://bianca.com")
    conteudo = browser.find_element(By.TAG_NAME, "body").text
    print(conteudo)
    browser.close()
    return conteudo
