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
		
def TESTCATS1():
    html=OPEN_URL(Decode('aHR0cHM6Ly9jb3B5LmNvbS8xeDZmNkQzTUo3TGFYZW43'))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,22,image)
		
def TESTCATS4():
    html=OPEN_URL(Decode('aHR0cHM6Ly9jb3B5LmNvbS9XdlI4M3RNVVFPeml1dGIw'))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,22,image)
		
def TESTCATS5():
    html=OPEN_URL(Decode('aHR0cHM6Ly9jb3B5LmNvbS9PeGJpSGFKSHBnRmVQVjYy'))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,22,image)
		
def TESTCATS2():
    html=OPEN_URL(Decode('aHR0cHM6Ly9jb3B5LmNvbS8xeDZmNkQzTUo3TGFYZW43'))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,22,image)
		
def TESTCATS3():
    html=OPEN_URL(Decode9('aHR0cDovL2Rldmlsc29yaWdpbmJ1aWxkLmNvbS9hZGRvbi9VUkxTaG93cy5waHA='))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addList(name,url,22,image)
		
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
        addDir3(name,url,18,'http://devilsoriginbuild.com/addon/Icon.png')
        
def LISTS2(url):
    html=OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url in match:
        addDir3(name,url,19,'http://devilsoriginbuild.com/addon/Icon.png')
        
def LISTS3(url):
    html=OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        addDir4('STREAM',url,16,'http://devilsoriginbuild.com/addon/Icon.png')

def TestPlayUrl(name, url, iconimage=None):
    print '--- Playing "{0}". {1}'.format(name, url)
    listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
    listitem.setInfo(type="Video", infoLabels={ "Title": name })
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def Build_MenuMovies():
	url1 = Decode('aHR0cDovL2RsMi5teTk4bXVzaWMuY29tL0RhdGEvRmlsbS84Ljk0Lw==')
	url2 = Decode('aHR0cDovL2RsMi5teTk4bXVzaWMuY29tL0RhdGEvRmlsbS85Ljk0Lw==')
	url3 = Decode('aHR0cDovL2RsMi5teTk4bXVzaWMuY29tL0RhdGEvRmlsbS8xMC45NC8=')
	streams.ParseURL(url1)
	streams.ParseURL(url2)
	streams.ParseURL(url3)
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
	
def Build_MenuTrailers():
	url1 = Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL0NvbWluZ1Nvb24vMjAxNS8=')
	url2 = Decode('aHR0cDovL2RsLmZpbG1paGEuY29tL0NvbWluZ1Nvb24vMjAxNi8=')
	streams.ParseURL(url1)
	streams.ParseURL(url2)
	
def Build_MenuTVshows():
	url1 = Decode('aHR0cDovL2RsMi5teTk4bXVzaWMuY29tL0RhdGEvU2VyaWFsLw==')
	streams.ParseURL(url1)

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
