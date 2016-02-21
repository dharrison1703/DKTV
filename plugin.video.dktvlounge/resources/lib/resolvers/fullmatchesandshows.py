import re, urllib2
#from resources.lib import common

#open = common.common_Modules

def open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
	
def resolve(url):
	getHTML = open_Url(url)
	playLink = re.compile('<script data-config="(.*?)"',re.DOTALL).findall(getHTML)
	foundLink = ''
	print 'FOUND PLAY LINKS: ' + str(len(playLink)) 
	for link in playLink:
		print 'Play Link Grabbed: ' + link
		foundLink = link
	
	if '/v2' in foundLink:
		foundLink = foundLink.replace('/v2','')
	if 'zeus.json' in foundLink:
		foundLink = foundLink.replace('zeus.json','video-sd.mp4?hosting_id=21772')
	if 'config.playwire.com' in foundLink:
		foundLink = foundLink.replace('config.playwire.com','cdn.video.playwire.com')
	if 'http:' not in foundLink:
		foundLink = 'http:' + foundLink
	
	print 'Cleaned Play Link: ' + foundLink
	
	return foundLink