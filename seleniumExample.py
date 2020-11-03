from selenium import webdriver # import selenium

browser = webdriver.Firefox() # set automated webrowser - make sure geko is intalled and in a PATH directory
browser.get('https://www.google.com/') # send browser to URI

elem1 =  browser.find_element_by_css_selector('#introAgreeButton > span:nth-child(3) > span:nth-child(1)')
elem1.click() # define varianble as the object created from a CSS element

#elem = browser.find_element_by_css_selector('.gLFyf')
#elem.click()

searchElem = browser.find_element_by_css_selector('.search-field') # define search element object
searchElem.send_keys('zophie') # type in the search box
searchElem.submit() # submit the search
browser.back() 
browser.forward()
browser.refresh()

elem.text # all element object have a text element that allows you to grab the text - a string

