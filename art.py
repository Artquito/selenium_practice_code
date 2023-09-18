from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

textarea = driver.find_element(by=By.NAME, value="my-textarea")
heading = driver.find_element(by=By.CSS_SELECTOR, value=".display-6")
button = driver.find_element(by=By.CSS_SELECTOR, value=".btn")

textarea.send_keys("test")
print(heading.text)
button.click()

# driver.quit()
