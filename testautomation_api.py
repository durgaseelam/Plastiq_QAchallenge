# '''
# I'm using google module which  uses google api. So this will not illustrate search using web page.
# Required beautifulsoup4 and google modules

# query : query string that we want to search for.
# tld : tld stands for top level domain which means we want to search our result on google.com or google.in
# or some other domain.
# lang : lang stands for language.
# num : Number of results we want.
# start : First result to retrieve.
# stop : Last result to retrieve. Use None to keep searching forever.
# pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP.
# Keeping significant lapse will make your program slow but its safe and better option.
# Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop
# '''

from google search import search 
query='test automation is awesome'
for  _link in search(query,tld='com',num=10,stop=1,pause=2):
  print(_link)
