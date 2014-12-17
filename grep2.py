import urllib2
import re
from pprint import pprint
import json

url = "http://www.reddit.com/hot"
website = urllib2.urlopen(url)
json_html = json.loads(website.read())
print json_html
##links = re.findall('"((http|ftp)s?://.*?)"', html)

##pprint(links[0])

