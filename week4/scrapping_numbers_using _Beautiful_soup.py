# importing modules
import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#input and HTML parsing
url = input('Enter URL Please:- ') 	# enter the required url example:  http://py4e-data.dr-chuck.net/comments_42.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
# output
print("count is ",count) # print count
print("sum is ",sum)	# print sum
