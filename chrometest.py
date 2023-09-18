from selenium import webdriver
from selenium.webdriver.common.by import By

service = webdriver.ChromeService(executable_path="D:\Project\pygame\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options, service=service)


driver.get("https://elearn.citrakasih.sch.id/mod/quiz/edit.php?cmid=303690")

google_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn")
google_button.click()
print(google_button)