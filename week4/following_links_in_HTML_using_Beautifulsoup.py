# import modules
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# input and parsing HTML
url = input('Enter URL :- ')	# enter url example:  http://py4e-data.dr-chuck.net/known_by_Fawaz.html
count = int(input("Enter count :"))  # enter count, sample count:4
position = int(input("Enter position :"))  # enter position, sample position: 3
for i in range(count):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	s = []
	t = []
	for tag in tags:
		x = tag.get('href', None)
		s.append(x)
		y = tag.text
		t.append(y)
    
	print("Retrieving:---",s[position-1])  #prints page url
	print("Name:-",t[position-1])		# prints the name of the page
	url = s[position-1]



