import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
#The user will specify the search terms using command line arugments, when they launch the program.
#These arguments will be stored as strings in a list in sys.argv.
#Remember that you have to start at the list 1 index after, because sys.argv prints itself.
#The command is python webscraping.py power rangers.
res.raise_for_status
#If any other number error happens than 200, than this gives you the status update.

#retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
