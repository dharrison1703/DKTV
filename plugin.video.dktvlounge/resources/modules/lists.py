import base64
import sys
import urlparse
import yt
import time
import urllib,urllib2,re,base64,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import base64
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
from resources.modules import modules, streams

addon_id='plugin.video.dktvlounge'
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
PATH = "DKTV Lounge"
VERSION = "1.0.1"
ADDONS      =  xbmc.translatePath(os.path.join('special://home','addons',''))
ART 		=  os.path.join(ADDONS,addon_id,'resources','art')+os.sep
FANART      =  xbmc.translatePath(os.path.join(ADDONS,addon_id,'fanart.jpg'))
net = Net()

Decode = base64.decodestring
BASE2=base64.decodestring('aHR0cDovL2RsLmZpbG0ybW92aWUuaW5mby9zZXJpYWwv')
BASE3=base64.decodestring('aHR0cDovL3dhdGNoLXNpbXBzb25zLmNvbS9kb3dubG9hZHMv')
BASE4=base64.decodestring('aHR0cDovL2dheml6b3ZhLm5ldC9wdWIvU2VyaWFscy9QZXBwYSUyMFBpZy9QZXBwYSUyMFBpZyUyMC0lMjBDb21wbGV0ZSUyMFNlcmllcyUyMDEsJTIwMiwlMjAzLCUyMDQv')
BASE5=base64.decodestring('aHR0cDovL3NlZWR1cmdyZWVkLngxMGhvc3QuY29tL29yaWdpbi8=')
BASE6=base64.decodestring('aHR0cDovL2dheml6b3ZhLm5ldC9wdWIvU2VyaWFscy9PdGhlclRvb25zL1Rhei1NYW5pYS8=')
BASE7=base64.decodestring('aHR0cDovL2ljaGkxMzQubmV0MTYubmV0L0lQVFYv')
CAT = base64.decodestring('LnBocA==')
BASE = base64.decodestring('aHR0cDovL2JhY2syYmFzaWNzLngxMGhvc3QuY29tL2JhY2syYmFzaWNzL3Rlc3Qv')

def addList(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def TESTCATS2():
    html=OPEN_URL('http://devil666wizard.x10host.com/addon/movieurl/URL.php')
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,22,image)

def TESTCATS3():
    html=OPEN_URL('http://devil666wizard.x10host.com/addon/movieurl/URLShows.php')
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,22,image)

def TESTCATS4():
    html=OPEN_URL(Decode('aHR0cDovL2JhY2syYmFzaWNzLngxMGhvc3QuY29tL2JhY2syYmFzaWNzL3Rlc3QvcmVjZW50ZXBpc29kZXMucGhw'))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,28,image)
		
def OPEN_URL(url):
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read(	)
		response.close()
		return link
		
def LISTS(url):
    html=OPEN_URL(url)
    match = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,url,18,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png')
        
def LISTS2(url):
    html=OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url in match:
        addDir3(name,url,19,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png')
        
def LISTS3(url):
    html=OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        addDir4('STREAM',url,16,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png')

def TestPlayUrl(name, url, iconimage=None):
    print '--- Playing "{0}". {1}'.format(name, url)
    listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
    listitem.setInfo(type="Video", infoLabels={ "Title": name })
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def Build_MenuMovies():
	url1 = Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDE0Lw==')
	url2 = Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDEzLw==')
	url3 = Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL01vdmllcy8yMDEyLw==')
	streams.ParseURL(url1)
	streams.ParseURL(url2)
	streams.ParseURL(url3)
	
def Build_MenuTrailers():
	url1 = Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL0NvbWluZ1Nvb24vMjAxNS8=')
	url2 = Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL0NvbWluZ1Nvb24vMjAxNi8=')
	streams.ParseURL(url1)
	streams.ParseURL(url2)


def Live(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
                addList3('%s'%(name).replace('DKTV Lounge','DKTV Lounge').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),15,'%s'%(iconimage))


def addList3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def List_LiveTVCats():
    modules.addDir('All Channels','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Entertainment','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Movies','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Music','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('News','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Sports','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Documentary','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Kids','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Food','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Religious','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('USA Channels','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')
    modules.addDir('Other','',13,'http://devil666wizard.x10host.com/BackgroundArt/Icon.png','','')

def List_LiveTVFull(Cat_Name):
    Find_all = False
    cat_id = '0'
    if Cat_Name == 'All Channels': Find_all = True
    if Cat_Name == 'Entertainment': cat_id = '1'
    if Cat_Name == 'Movies': cat_id = '2'
    if Cat_Name == 'Music': cat_id = '3'
    if Cat_Name == 'News': cat_id = '4'
    if Cat_Name == 'Sports': cat_id = '5'
    if Cat_Name == 'Documentary': cat_id = '6'
    if Cat_Name == 'Kids': cat_id = '7'
    if Cat_Name == 'Food': cat_id = '8'
    if Cat_Name == 'Religious': cat_id = '9'
    if Cat_Name == 'USA Channels': cat_id = '10'
    if Cat_Name == 'Other': cat_id = '11'

    html=OPEN_URL(Decode('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz'))
    match = re.compile('"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}',re.DOTALL).findall(html)
    print 'Len Match: >>>' + str(len(match))
    for name,img, CatNO in match:
        Image = 'http://uktvnow.desistreams.tv/' + (img).replace('\\','')
        if CatNO == cat_id:
		    modules.addDir(name,'',12,Image,Image,'')
        elif Find_all == True:
		    modules.addDir(name,'',12,Image,Image,'')
        else: pass
		
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def LiveTVFull(Search_Name):
    html=OPEN_URL(Decode('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz'))
    match = re.compile('"id":".+?","name":"'+Search_Name+'","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}',re.DOTALL).findall(html)
    for img,url,url2,url3 in match:
		Image = 'http://uktvnow.desistreams.tv/' + (img).replace('\\','')
		modules.AddTestDir(Search_Name + ': Link 1', (url).replace('\\',''), 15, Image, description="", isFolder=False, background=Image)
		modules.AddTestDir(Search_Name + ': Link 2', (url2).replace('\\',''), 15, Image, description="", isFolder=False, background=Image)
		modules.AddTestDir(Search_Name + ': Link 3', (url3).replace('\\',''), 15, Image, description="", isFolder=False, background=Image)
