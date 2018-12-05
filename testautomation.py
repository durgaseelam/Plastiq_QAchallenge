# Automating google search using python - selenium 
# for this task we need browser driver running . I used chrome browser which can be downloaded form 'http://chromedriver.chromium.org/downloads'
#pip install selenium 
#Tested on windows machine. we have to give local installation path while loading chrome webdriver 


from selenium import webdriver
_browser=webdriver.Chrome(r'c:\chromedriver_win32\chromedriver.exe')
_query='test automation is awesome'
_browser.get('http://google.com/search?q='+_query)

#browser.get() method returns all the properties of the webpage as elements. I'm filtering by xpath which returns
# element object of hyperlinks
print('Title : '+_browser.title)
_results=_browser.find_elements_by_xpath('.//a')
for _link in _results:
  print(_link.getattribute('href'))
  
