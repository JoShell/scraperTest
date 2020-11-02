from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.google.com/')

elem1 =  browser.find_element_by_css_selector('#introAgreeButton > span:nth-child(3) > span:nth-child(1)')
elem1.click()

#elem = browser.find_element_by_css_selector('.gLFyf')
#elem.click()

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()

