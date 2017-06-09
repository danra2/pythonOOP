from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
# <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
Web Scraping 259
try:
 elem = browser.find_element_by_class_name('bookcover')
 print('Found <%s> element with that class name!' % (elem.tag_name))
except:
 print('Was not able to find an element with that name.')


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
# <class 'selenium.webdriver.remote.webelement.WebElement'>
linkElem.click() # follows the "Read It Online" link
