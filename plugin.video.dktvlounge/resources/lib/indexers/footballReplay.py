import re, xbmc, xbmcgui, xbmcplugin, urllib, urllib2, sys
from resources.lib.resolvers import fullmatchesandshows
dialog = xbmcgui.Dialog()
defaultIcon = ''

def open_Url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def play(name, url, thumbail=None):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=thumbail,thumbnailImage=thumbail); liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	xbmc.Player().play(url, liz, False)
	return ok

def addItem(name, url, mode, thumb, fanart, description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumb="+urllib.quote_plus(thumb)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=defaultIcon, thumbnailImage=thumb)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)

def addFolder(name, url, mode, thumb, fanart, description, icon):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumb="+urllib.quote_plus(thumb)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
	ok=True
	folderIcon = ''
	liz=xbmcgui.ListItem(name, iconImage=folderIcon, thumbnailImage=thumb)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

class footballIndexer():

	def __init__(self, url):
		self.baseURL = url
		self.storedHTML = ''
		self.itemsFound = 0
		self.itemsComplete = 1
		request_HTML = open_Url(self.baseURL)
		self.storedHTML = request_HTML
	
	def getRowItems(self):
		getItems = re.compile('<div class="td-block-span4">(.*?)</div>',re.DOTALL).findall(self.storedHTML)
		self.itemsFound = len(getItems)
		for rowItem in getItems:
			self.getItemData(rowItem)
			self.itemsComplete = self.itemsComplete + 1
	
	def getItemData(self, item):
		getDATA = re.compile('<div class="td-module-thumb">(.*?)</a>',re.DOTALL).findall(item)
		for dataBlock in getDATA:
			self.cleanDataBlock(dataBlock)
	
	def cleanDataBlock(self, block):
		cleanedData = re.compile('<a href="(.*?)" rel=".*?" title="(.*?)">.*?<img width=".*?" height=".*?" itemprop=".*?" class=".*?" src="(.*?)" alt=".*?" title=".*?"/>',re.DOTALL).findall(block)
		print 'Clean Data Found: ' + str(len(cleanedData))
		for url, title, image in cleanedData:
			addItem(self.cleanTitle(title), url, 63, image, '', '')
		
		if self.itemsComplete == self.itemsFound: self.nextPage()
		else: pass
	
	def nextPage(self):
		navigation = re.compile('<div class="page-nav td-pb-padding-side">(.*?)<span class="pages">.*?</span></div>',re.DOTALL).findall(self.storedHTML)
		html = ''
		print 'Nav Found: ' + str(len(navigation))
		print str(navigation)
		for nav in navigation:
			html = nav
		nextPage = re.compile('<span class="current">.*?</span><a href="(.*?)" class="page" title="(.*?)">',re.DOTALL).findall(html)
		if len(nextPage) > 0:
			for url, pageNO in nextPage:
				print 'Next Page URL: ' + url
				addFolder('Next: Page ' + pageNO, url, 62, 'fff', 'fff', 'This is the description', 'TV_Folder.png')
		else: pass

	
	def cleanTitle(self, titleString):
		if '&#038;' in titleString:
			titleString = titleString.replace('&#038;', '&')
		if '&#8211;' in titleString:
			titleString = titleString.replace('&#8211;', '-')
		
		return titleString
		
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class videoIndexer():
	
	def __init__(self, url, name):
		self.pageURL = url
		self.name = name
	
	def findVideos(self):
		
		getHTML = open_Url(self.pageURL)
		videoList = re.compile('<li tabindex="0" class=".*?" id=".*?"><a href="(.*?)"><div class="acp_title">(.*?)</div></a></li>',re.DOTALL).findall(getHTML)
		data = ''
		title = ''
		print 'Found Lists: ' + str(len(videoList))
		
		playLinks = []
		linkTitles = []
		for url, title in videoList:
			playLinks.append(self.pageURL + url)
			linkTitles.append(title)
		
		if len(videoList) == 0:
			get = fullmatchesandshows.resolve(self.pageURL)
			play(self.name, get, thumbail='')
			
		if len(playLinks) > 0:
			select = dialog.select(self.name,linkTitles)
			if select == -1:
				return
			else:
				check_Link = playLinks[select]
				get = fullmatchesandshows.resolve(check_Link)
				play(linkTitles[select], get, thumbail='')









		