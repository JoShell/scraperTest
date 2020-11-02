from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com/')

elem1 =  browser.find_element_by_css_selector('#introAgreeButton > span:nth-child(3) > span:nth-child(1)')
elem1.click()