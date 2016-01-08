import xbmc, xbmcgui, xbmcplugin, xbmcaddon, os, sys, control, Plp
import time, urllib, urllib2, base64
import re, urlparse, json, hashlib, CNF_Studio_Indexer
import urlresolver

import server, config, load_channels

from BeautifulSoup import BeautifulStoneSoup, BeautifulSOAP
from resources.modules.bs4 import BeautifulSoup
from resources.modules import modules, yt, premierleague, speedtest, lists, streams, SoapsOD, sys_Check
from resources.lib.libraries import client
from resources.modules.parsers import parser
from resources.menus import LiveTvMenu, ODMenu
from resources.scrapers import Wsimpsons
from addon.common.addon import Addon
from addon.common.net import Net
from HTMLParser import HTMLParser

#---------------------------------------------------------------------------------------------------------------
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') ) 

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
go = True;
Decode = base64.decodestring
dp = xbmcgui.DialogProgress()

#---------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Variables **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PATH = "DKTV Lounge"
VERSION = "0.1.0"
ADDON_ID = 'plugin.video.dktvlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)

HOME = ADDON.getAddonInfo('path')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'icon.png'))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
ADDON_DATA = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/' + ADDON_ID + '/'))
PROFILE_DATA = xbmc.translatePath(os.path.join('special://home/userdata/'))
BaseURL = 'http://devil66wizard.x10host.com/addon/'
SKIN = xbmc.translatePath(os.path.join('special://home/addons/skin.aeon.nox.silvo/'))
HERE = xbmc.translatePath(os.path.join('special://home/addons/plugin.program.Devil666/'))
PASSCODE = ADDON.getSetting('passcode')
PASSWORD = ADDON.getSetting('password')
u_tube = 'http://www.youtube.com'
online_movielist = ADDON.getSetting('online_movielist')
online_m3u = ADDON.getSetting('online_m3u')
online_PLP = ADDON.getSetting('online_PLP')
online_LiveTV = ADDON.getSetting('online_LiveTV')
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'
DCPWC = ADDON.getSetting('Donators Code')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Menu's **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason

def hidden_Input(action):
	dialog = xbmcgui.Dialog()
	input = ''
	if action == 'PWord':
		input = dialog.input('Enter Password', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	elif action == 'PCode':
		input = dialog.input('Enter Passcode', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
	else: pass
	
	return input
	
def code_Input():
	if PASSCODE == '': 
		action = 'PCode'
		passcode = hidden_Input(action)
		ADDON.setSetting(id='passcode', value = passcode)
	else: pass

def pass_Input():
	if PASSWORD == '': 
		action = 'PWord'
		password = hidden_Input(action)
		ADDON.setSetting(id='password', value = password)
	else: pass
	#xbmc.sleep(500)
	
def Home_Menu(PASSCODE, PASSWORD):
    
    input_Failed = False
    
    if PASSWORD != '':
        if PASSCODE != '':
            if os.path.exists(SKIN):
                if os.path.exists(HERE):
                    if sys_Check.system_Check(PASSWORD, PASSCODE):
        
                        modules.addDir('Live TV',u_tube,48,ART+'icon.png',FANART,'')						
                        modules.addDir('Sports Centre','',2,ART+'icon.png',FANART,'')
                        modules.addDir('Movies','',1,ART+'icon.png',FANART,'')
                        modules.addDir('TV Shows','',5,ART+'icon.png',FANART,'')
                        #modules.addDir('Soaps','http://uksoapshare.blogspot.co.uk/',30,ART+'TvShows.png',FANART,'')
                    
                    else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
                else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
            else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
        else:
            eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
            input_Failed = True
    else: 
        eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
        input_Failed = True
    
    if input_Failed:
        code_Input()
        pass_Input()
        PASSCODE = ADDON.getSetting('passcode')
        PASSWORD = ADDON.getSetting('password')
        Home_Menu(PASSCODE, PASSWORD)
        input_Failed = False
    else: pass


    
	
def Movies(PASSCODE, PASSWORD): # add this into ()
    
	input_Failed = False
    
	if PASSWORD != '':
		if PASSCODE != '':
			if os.path.exists(SKIN):
				if os.path.exists(HERE):
					if sys_Check.system_Check(PASSWORD, PASSCODE):
					
						modules.addDir('All Movies A-Z',u_tube,46,ART+'icon.png',FANART,'')						
						
					else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
				else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
			else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
		else:
			eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
			input_Failed = True
	else:
		eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
		input_Failed = True
	
	if input_Failed:
		code_Input()
		pass_Input()
		PASSCODE = ADDON.getSetting('passcode')
		PASSWORD = ADDON.getSetting('password')
		Movies(PASSCODE, PASSWORD) #This line will change depending on where you are mate
		input_Failed = False
	else: pass

def Premium_TV(PASSCODE, PASSWORD): # add this into ()
    
	input_Failed = False
    
	if PASSWORD != '':
		if PASSCODE != '':
			if os.path.exists(SKIN):
				if os.path.exists(HERE):
					if sys_Check.system_Check(PASSWORD, PASSCODE):
					
						modules.addDir('Premium TV','',49,ART+'icon.png',FANART,'')						
						
					else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
				else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
			else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
		else:
			eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
			input_Failed = True
	else:
		eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
		input_Failed = True
	
	if input_Failed:
		code_Input()
		pass_Input()
		PASSCODE = ADDON.getSetting('passcode')
		PASSWORD = ADDON.getSetting('password')
		Premium_TV(PASSCODE, PASSWORD) #This line will change depending on where you are mate
		input_Failed = False
	else: pass


def TV_Shows(PASSCODE, PASSWORD): # add this into ()
    
	input_Failed = False
    
	if PASSWORD != '':
		if PASSCODE != '':
			if os.path.exists(SKIN):
				if os.path.exists(HERE):
					if sys_Check.system_Check(PASSWORD, PASSCODE):
					
						modules.addDir('All Shows','',23,ART+'icon.png',FANART,'')
						
					else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
				else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
			else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
		else:
			eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
			input_Failed = True
	else:
		eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
		input_Failed = True
	
	if input_Failed:
		code_Input()
		pass_Input()
		PASSCODE = ADDON.getSetting('passcode')
		PASSWORD = ADDON.getSetting('password')
		TV_Shows(PASSCODE, PASSWORD) #This line will change depending on where you are mate
		input_Failed = False
	else: pass

	
def Sports_Centre(PASSCODE, PASSWORD): # add this into ()
    
	input_Failed = False
    
	if PASSWORD != '':
		if PASSCODE != '':
			if os.path.exists(SKIN):
				if os.path.exists(HERE):
					if sys_Check.system_Check(PASSWORD, PASSCODE):
					
						modules.addDir('Sports Channels','',43,ART+'icon.png',FANART,'')						
						modules.addDir('Sports Replays','',6,ART+'SportsReplays.png',FANART,'')
						modules.addDir('Live Events','',40,ART+'icon.png',FANART,'')
						
					else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
				else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
			else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
		else:
			eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
			input_Failed = True
	else:
		eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
		input_Failed = True
	
	if input_Failed:
		code_Input()
		pass_Input()
		PASSCODE = ADDON.getSetting('passcode')
		PASSWORD = ADDON.getSetting('password')
		Sports_Centre(PASSCODE, PASSWORD) #This line will change depending on where you are mate
		input_Failed = False
	else: pass
	
def Sports_Channels(PASSCODE, PASSWORD): # add this into ()
    
	input_Failed = False
    
	if PASSWORD != '':
		if PASSCODE != '':
			if os.path.exists(SKIN):
				if os.path.exists(HERE):
					if sys_Check.system_Check(PASSWORD, PASSCODE):
					
						modules.addDir('UK Sports',Decode('aHR0cDovL2Rldmlsc29yaWdpbmJ1aWxkLngxMGhvc3QuY29tL2FkZG9uL1Nwb3J0c0NoYW5uZWxzLnhtbA=='),8,ART+'icon.png',FANART,'')						
						modules.addDir('All Sports',Decode('aHR0cDovL2Rldmlsc29yaWdpbmJ1aWxkLngxMGhvc3QuY29tL2FkZG9uL1NQT3J0Uy5waHA='),42,ART+'icon.png',FANART,'')						
						
					else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
				else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
			else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
		else:
			eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
			input_Failed = True
	else:
		eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
		input_Failed = True
	
	if input_Failed:
		code_Input()
		pass_Input()
		PASSCODE = ADDON.getSetting('passcode')
		PASSWORD = ADDON.getSetting('password')
		Sports_Channels(PASSCODE, PASSWORD) #This line will change depending on where you are mate
		input_Failed = False
	else: pass


def Sports_Replays(PASSCODE, PASSWORD): # add this into ()
    
	input_Failed = False
    
	if PASSWORD != '':
		if PASSCODE != '':
			if os.path.exists(SKIN):
				if os.path.exists(HERE):
					if sys_Check.system_Check(PASSWORD, PASSCODE):
					
						modules.addDir('Football','',4,ART+'footballod.png',FANART,'')
						modules.addDir('Boxing',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1JlcGxheXMvQm9YaU5nLnBocA=='),39,ART+'BoxingOD.png',FANART,'')
						modules.addDir('UFC',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1JlcGxheXMvVWZDckVwTGFZcy5waHA='),39,ART+'icon.png',FANART,'')
						modules.addDir('WWE','',29,ART+'icon.png',FANART,'')
						
					else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
				else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
			else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
		else:
			eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
			input_Failed = True
	else:
		eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
		input_Failed = True
	
	if input_Failed:
		code_Input()
		pass_Input()
		PASSCODE = ADDON.getSetting('passcode')
		PASSWORD = ADDON.getSetting('password')
		Sports_Replays(PASSCODE, PASSWORD) #This line will change depending on where you are mate
		input_Failed = False
	else: pass
	
def WWE_Home():
	modules.addDir('Raw',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1JlcGxheXMvUmF3LnBocA=='),39,ART+'icon.png',FANART,'')
	modules.addDir('Smackdown',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1JlcGxheXMvU21hY2tkb3duLnBocA=='),39,ART+'icon.png',FANART,'')
	modules.addDir('PPVs',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1JlcGxheXMvV3dFcFB2Uy5waHA='),39,ART+'icon.png',FANART,'')
	modules.addDir('Other',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1JlcGxheXMvV3dFLnBocA=='),39,ART+'icon.png',FANART,'')

def Live_Today(PASSCODE, PASSWORD): # add this into ()
    
	input_Failed = False
    
	if PASSWORD != '':
		if PASSCODE != '':
			if os.path.exists(SKIN):
				if os.path.exists(HERE):
					if sys_Check.system_Check(PASSWORD, PASSCODE):
					
						modules.addDir('Premier League',u_tube,47,ART+'LiveFootball.png',FANART,'')						
						modules.addDir('ROW Football',Decode('aHR0cDovL2Rldmlsc29yaWdpbmJ1aWxkLngxMGhvc3QuY29tL2FkZG9uL0FsbEZvb3RiYWxsLnhtbA=='),8,ART+'LiveFootball.png',FANART,'')						
						modules.addDir('NFL',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL0xpdmVTcG9ydHMvTGl2ZU5GTC5waHA='),42,ART+'icon.png',FANART,'')						
						modules.addDir('Rugby',Decode('aHR0cDovL2Rldmlsc29yaWdpbmJ1aWxkLngxMGhvc3QuY29tL2FkZG9uL0xpdmVSdWdieS54bWw='),8,ART+'icon.png',FANART,'')						
						modules.addDir('PPV Events',Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1BwVmVWZU50Uy54bWw='),8,ART+'PPV.png',FANART,'')
						
					else: eval(Decode('c3lzX0NoZWNrLmZhaWxlZF9WZXJpZmljYXRpb24oKQ=='))
				else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
			else: eval(Decode('c3lzX0NoZWNrLmluY29ycmVjdF9TeXN0ZW0oKQ=='))
		else:
			eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzY29kZSgp'))
			input_Failed = True
	else:
		eval(Decode('c3lzX0NoZWNrLm5vX1N5c19QYXNzd29yZCgp'))
		input_Failed = True
	
	if input_Failed:
		code_Input()
		pass_Input()
		PASSCODE = ADDON.getSetting('passcode')
		PASSWORD = ADDON.getSetting('password')
		Live_Today(PASSCODE, PASSWORD) #This line will change depending on where you are mate
		input_Failed = False
	else: pass
	
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Replays **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def replay_Menu():
	modules.addDir('Shows',Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS9jYXRlZ29yeS9zaG93Lw=='),3,'https://upload.wikimedia.org/wikipedia/en/8/84/Match_of_the_Day.png',FANART,'')
	modules.addDir('Premier League',Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS9wcmVtaWVyLWxlYWd1ZS8='),3,'https://footballseasons.files.wordpress.com/2013/05/premier-league.png',FANART,'')
	modules.addDir('Champions League',Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS9jaGFtcGlvbnMtbGVhZ3VlLw=='),3,'http://www.ecursuri.ro/images/teste/test-champions-league.jpg',FANART,'')
	modules.addDir('La Liga',Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS9sYS1saWdhLw=='),3,'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png',FANART,'')
	modules.addDir('Bundesliga',Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS9idW5kZXNsaWdhLw=='),3,'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg',FANART,'')
	modules.addDir('Serie A',Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS9jYXRlZ29yeS9zZXJpZS1hLw=='),3,'http://files.jcriccione.it/200000223-2484526782/serie%20a.png',FANART,'')
	modules.addDir('Ligue 1',Decode('aHR0cDovL3d3dy5mdWxsbWF0Y2hlc2FuZHNob3dzLmNvbS9jYXRlZ29yeS9saWd1ZS0xLw=='),3,'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg',FANART,'')

#_________________________________________________________________________________________________________________________________________________________

# Get All Rows

def get_All_Rows(url):
	request_HTML = OPEN_URL(url)
	get_Rows = re.compile('<div class="td-block-row">(.*?)</div><!--./row-fluid-->',re.DOTALL).findall(request_HTML)
	for row in get_Rows:
		for_Each_Row(row)

# Get Each Video From The Row

def for_Each_Row(row):
	Get_Row_Item = re.compile('<div class="td-block-span4">(.+?)<!-- ./td-block-span4 -->',re.DOTALL).findall(row)
	for row_Item in Get_Row_Item:
		get_Each_Item_Data(row_Item)

# For Each Video In Row Get Link & Title

def get_Each_Item_Data(row_Item):
	get_item_Data = re.findall(r'<a href="(.+?)" rel="bookmark" title="(.+?)">',str(row_Item))
	item_Data = []
	link = ''
	for link, title in get_item_Data:
		item_Data.append(title)
		link = link
	
	get_Each_Item_Image(item_Data, row_Item, link)

# For Each Video In Row Get Image

def get_Each_Item_Image(item_Data, row_Item, link):
	get_Item_Image = re.compile('<img width=".+?" height=".+?" itemprop=".+?" class="entry-thumb" src="(.+?)" alt=".+?" title=".+?"/>',re.DOTALL).findall(row_Item)
	for image in get_Item_Image:
		item_Data.append(image)
	
	get_Each_Item_PLink(item_Data, link)

# For Each Video In Row Get Play Link
	
def get_Each_Item_PLink(item_Data, link):
	get_HTML = OPEN_URL(link)
	get_Play_Link = re.compile('<script data-config="(.+?)" data-css=".+?" data-height=".+?" data-width=".+?" src=".+?" type="text/javascript"></script>',re.DOTALL).findall(get_HTML)
	for pLink in get_Play_Link:
		item_Data.append(pLink)
		
	clean_And_Build_Item(item_Data)

# For Each Video In Row Clean And Build Item

def clean_And_Build_Item(item_Data):
	Name = item_Data[0]
	Image = item_Data[1]
	Play_Link = item_Data[2]
	
	Name = Name.decode("utf-8")
	Name = Name.replace('&#8211;', '-').replace('&#038;', '&')
	Play_Link = Play_Link.replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
	
	addLink('http:' + Play_Link, Name, Image,'','','','','',None,'',1)
#_________________________________________________________________________________________________________________________________________________________





	
#--------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Movies **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Structure **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import traceback
import cookielib
import xbmcvfs

debug = ADDON.getSetting('debug')
profile = xbmc.translatePath(ADDON.getAddonInfo('profile').decode('utf-8'))
favorites = os.path.join(profile, 'favorites')
source_file = os.path.join(profile, 'source_file')

if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else: FAV = []
if os.path.exists(source_file)==True:
    SOURCES = open(source_file).read()
else: SOURCES = []

def getData(url,fanart):
    SetViewLayout = "List"
     
    soup = getSoup(url)
    #print type(soup)
    if isinstance(soup,BeautifulSOAP):
        if len(soup('layoutype')) > 0:
            SetViewLayout = "Thumbnail"		    

        if len(soup('channels')) > 0:
            channels = soup('channel')
            for channel in channels:
#                print channel

                linkedUrl=''
                lcount=0
                try:
                    linkedUrl =  channel('externallink')[0].string
                    lcount=len(channel('externallink'))
                except: pass
                #print 'linkedUrl',linkedUrl,lcount
                if lcount>1: linkedUrl=''

                name = channel('name')[0].string
                print '~~~~~~~~~~~~~~~~~~'
                print name
                print '~~~~~~~~~~~~~~~~~~'
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    thumbnail = ''

                try:
                    if not channel('fanart'):
                        if addon.getSetting('use_thumb') == "true":
                            fanArt = thumbnail
                        else:
                            fanArt = fanart
                    else:
                        fanArt = channel('fanart')[0].string
                    if fanArt == None:
                        raise
                except:
                    fanArt = fanart

                try:
                    desc = channel('info')[0].string
                    if desc == None:
                        raise
                except:
                    desc = ''

                try:
                    genre = channel('genre')[0].string
                    if genre == None:
                        raise
                except:
                    genre = ''

                try:
                    date = channel('date')[0].string
                    if date == None:
                        raise
                except:
                    date = ''

                try:
                    credits = channel('credits')[0].string
                    if credits == None:
                        raise
                except:
                    credits = ''

                try:
                    if linkedUrl=='':
                        print name.encode('utf-8', 'ignore')
                        addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),48,thumbnail,fanArt,desc,genre,date,credits,True)
                    else:
                        #print linkedUrl
                        print name.encode('utf-8')
                        addDir(name.encode('utf-8'),linkedUrl.encode('utf-8'),47,thumbnail,fanArt,desc,genre,date,None,'source')
                except:
                    addon_log('There was a problem adding directory from getData(): '+name.encode('utf-8', 'ignore'))
        else:
            addon_log('No Channels: getItems')
            getItems(soup('item'),fanart)
    else:
        parse_m3u(soup)

    if SetViewLayout == "Thumbnail":
       SetViewThumbnail()
	   
#----------------------------------------------- getItems(items,fanart) -----------------------------------------------

def getItems(items,fanart):
        total = len(items)
        #print 'START GET ITEMS *****'
        addon_log('Total Items: %s' %total)
        for item in items:
            isXMLSource=False
            isJsonrpc = False
            try:
                name = item('title')[0].string
                print '~~~~~~~~~~~~~~~~~~'
                print name
                print '~~~~~~~~~~~~~~~~~~'
                if name is None:
                    name = 'unknown?'
            except:
                addon_log('Name Error')
                name = ''


            try:
                if item('epg'):
                    if item.epg_url:
                        addon_log('Get EPG Regex')
                        epg_url = item.epg_url.string
                        epg_regex = item.epg_regex.string
                        epg_name = get_epg(epg_url, epg_regex)
                        if epg_name:
                            name += ' - ' + epg_name
                    elif item('epg')[0].string > 1:
                        name += getepg(item('epg')[0].string)
                else:
                    pass
            except:
                addon_log('EPG Error')
            try:
                url = []
                if len(item('link')) >0:
#                    print 'item link', item('link')
                    for i in item('link'):
                        if not i.string == None:
                            url.append(i.string)
                    
                elif len(item('sportsdevil')) >0:
                    for i in item('sportsdevil'):
                        if not i.string == None:
                            sportsdevil = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +i.string
                            referer = item('referer')[0].string
                            if referer:
                                #print 'referer found'
                                sportsdevil = sportsdevil + '%26referer=' +referer
                            url.append(sportsdevil)
                elif len(item('p2p')) >0:
                    for i in item('p2p'):
                        if not i.string == None:
                            if 'sop://' in i:
                                sop = 'plugin://plugin.video.p2p-streams/?url='+i.string +'&amp;mode=2&amp;' + 'name='+name 
                                url.append(sop) 
                            else:
                                p2p='plugin://plugin.video.p2p-streams/?url='+i.string +'&amp;mode=1&amp;' + 'name='+name 
                                url.append(p2p)
                elif len(item('vaughn')) >0:
                    for i in item('vaughn'):
                        if not i.string == None:
                            vaughn = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel='+i.string
                            url.append(vaughn)
                elif len(item('ilive')) >0:
                    for i in item('ilive'):
                        if not i.string == None:
                            if not 'http' in i.string:
                                ilive = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/'+i.string+'&amp;link=99&amp;mode=iLivePlay'
                            else:
                                ilive = 'plugin://plugin.video.tbh.ilive/?url='+i.string+'&amp;link=99&amp;mode=iLivePlay'
                elif len(item('yt-dl')) >0:
                    for i in item('yt-dl'):
                        if not i.string == None:
                            ytdl = i.string + '&mode=18'
                            url.append(ytdl)
                elif len(item('utube')) >0:
                    for i in item('utube'):
                        if not i.string == None:
                            if len(i.string) == 11:
                                utube = 'plugin://plugin.video.youtube/play/?video_id='+ i.string 
                            elif i.string.startswith('PL') and not '&order=' in i.string :
                                utube = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + i.string
                            else:
                                utube = 'plugin://plugin.video.youtube/play/?playlist_id=' + i.string 
                    url.append(utube)
                elif len(item('imdb')) >0:
                    for i in item('imdb'):
                        if not i.string == None:
                            if addon.getSetting('genesisorpulsar') == '0':
                                imdb = 'plugin://plugin.video.genesis/?action=play&imdb='+i.string
                            else:
                                imdb = 'plugin://plugin.video.pulsar/movie/tt'+i.string+'/play'
                            url.append(imdb)                      
                elif len(item('f4m')) >0:
                        for i in item('f4m'):
                            if not i.string == None:
                                if '.f4m' in i.string:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)
                                elif '.m3u8' in i.string:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)+'&amp;streamtype=HLS'
                                    
                                else:
                                    f4m = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(i.string)+'&amp;streamtype=SIMPLE'
                        url.append(f4m)
                elif len(item('ftv')) >0:
                    for i in item('ftv'):
                        if not i.string == None:
                            ftv = 'plugin://plugin.video.F.T.V/?name='+urllib.quote(name) +'&url=' +i.string +'&mode=125&ch_fanart=na'
                        url.append(ftv)                        
                if len(url) < 1:
                    raise
            except:
                addon_log('Error <link> element, Passing:'+name.encode('utf-8', 'ignore'))
                continue
                
            isXMLSource=False

            try:
                isXMLSource = item('externallink')[0].string
            except: pass
            
            if isXMLSource:
                ext_url=[isXMLSource]
                isXMLSource=True
            else:
                isXMLSource=False
            try:
                isJsonrpc = item('jsonrpc')[0].string
            except: pass
            if isJsonrpc:
                ext_url=[isJsonrpc]
                isJsonrpc=True
            else:
                isJsonrpc=False            
            try:
                thumbnail = item('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:
                if not item('fanart'):
                    if addon.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                    else:
                        fanArt = fanart
                else:
                    fanArt = item('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                fanArt = fanart
            try:
                desc = item('info')[0].string
                if desc == None:
                    raise
            except:
                desc = ''

            try:
                genre = item('genre')[0].string
                if genre == None:
                    raise
            except:
                genre = ''

            try:
                date = item('date')[0].string
                if date == None:
                    raise
            except:
                date = ''

            regexs = None
            if item('regex'):
                try:
                    reg_item = item('regex')
                    regexs = parse_regex(reg_item)
                except:
                    pass            
           
            try:
                if len(url) > 1:
                    
                    alt = 0
                    playlist = []
                    for i in url:
                    	if addon.getSetting('ask_playlist_items') == 'true':
	                        if regexs:
	                            playlist.append(i+'&regexs='+regexs)
	                        elif  any(x in i for x in resolve_url) and  i.startswith('http'):
	                            playlist.append(i+'&mode=19')                            
                        else:
                            playlist.append(i)
                    if addon.getSetting('add_playlist') == "false":                    
                            for i in url:
                                alt += 1
                                #print 'ADDLINK 1'
                                addLink(i,'%s) %s' %(alt, name.encode('utf-8', 'ignore')),thumbnail,fanArt,desc,genre,date,True,playlist,regexs,total)                            
                    else:
                        print name
                        addLink('', name.encode('utf-8', 'ignore'),thumbnail,fanArt,desc,genre,date,True,playlist,regexs,total)
                else:
                    if isXMLSource:
                        print name
                    	addDir(name.encode('utf-8'),ext_url[0].encode('utf-8'),47,thumbnail,fanart,desc,genre,date,None,'source')
                    elif isJsonrpc:
                        print name
                        addDir(name.encode('utf-8'),ext_url[0],53,thumbnail,fanart,desc,genre,date,None,'source')
                    elif url[0].find('sublink') > 0:
                        print name
                        addDir(name.encode('utf-8'),url[0],30,thumbnail,fanArt,desc,regexs,'','','')
                        #addDir(name.encode('utf-8'),url[0],30,thumbnail,fanart,desc,genre,date,'sublink')				
                    else: 
                        print name
                        addLink(url[0],name.encode('utf-8', 'ignore'),thumbnail,fanArt,desc,genre,date,True,None,regexs,total)

                    #print 'success'
            except:
                addon_log('There was a problem adding item - '+name.encode('utf-8', 'ignore'))
        #print 'FINISH GET ITEMS *****' 

#----------------------------------------------- SetViewThumbnail() -----------------------------------------------

def SetViewThumbnail():
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.confluence':
        xbmc.executebuiltin('Container.SetViewMode(500)')
    elif skin_used == 'skin.aeon.nox':
        xbmc.executebuiltin('Container.SetViewMode(511)') 
    else:
        xbmc.executebuiltin('Container.SetViewMode(500)')
		
#----------------------------------------------- addDir -----------------------------------------------
		
def addDir(name,url,mode,iconimage,fanart,description,genre,date,credits,showcontext=False):
        
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        liz.setProperty("Fanart_Image", fanart)

        if showcontext:
            contextMenu = []
            if showcontext == 'source':
                if name in str(SOURCES):
                    contextMenu.append(('Remove from Sources','XBMC.RunPlugin(%s?mode=8&name=%s)' %(sys.argv[0], urllib.quote_plus(name))))
            elif showcontext == 'download':
                contextMenu.append(('Download','XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            elif showcontext == 'fav':
                contextMenu.append(('Remove from E.L. Favorites','XBMC.RunPlugin(%s?mode=6&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
									
            if not name in FAV:
                contextMenu.append(('Add to E.L. Favorites','XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

        return ok

#----------------------------------------------- addLink -----------------------------------------------

def addLink(url,name,iconimage,fanart,description,genre,date,showcontext,playlist,regexs,total,setCookie=""):
        #print 'url,name',url,name
        contextMenu =[]
        try:
            name = name.encode('utf-8')
        except: pass
        ok = True
       
        if regexs: 
            mode = '11'
           
            contextMenu.append(('[COLOR white]!!Download Currently Playing!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))           
        elif  any(x in url for x in resolve_url) and  url.startswith('http'):
            mode = '19'
          
            contextMenu.append(('[COLOR white]!!Download Currently Playing!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))           
        elif url.endswith('&mode=18'):
            url=url.replace('&mode=18','')
            mode = '18' 
          
            contextMenu.append(('[COLOR white]!!Download!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name)))) 
            if addon.getSetting('dlaudioonly') == 'true':
                contextMenu.append(('!!Download [COLOR seablue]Audio!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
                                        %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))                                     
        elif url.startswith('magnet:?xt=') or '.torrent' in url:
          
            if '&' in url and not '&amp;' in url :
                url = url.replace('&','&amp;')
            url = 'plugin://plugin.video.pulsar/play?uri=' + url
            mode = '10'
                     
        else: 
            mode = '10'
      
            contextMenu.append(('[COLOR white]!!Download Currently Playing!![/COLOR]','XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))           
        u=sys.argv[0]+"?"
        play_list = False
      
        if playlist:
            if addon.getSetting('add_playlist') == "false":
                u += "url="+urllib.quote_plus(url)+"&mode="+mode
            else:
                u += "mode=13&name=%s&playlist=%s" %(urllib.quote_plus(name), urllib.quote_plus(str(playlist).replace(',','||')))
                name = name + '[COLOR magenta] (' + str(len(playlist)) + ' items )[/COLOR]'
                play_list = True
        else:
            u += "url="+urllib.quote_plus(url)+"&mode="+mode
        if regexs:
            u += "&regexs="+regexs
        if not setCookie == '':
            u += "&setCookie="+urllib.quote_plus(setCookie)
  
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date })
        liz.setProperty("Fanart_Image", fanart)
        
        if (not play_list) and not any(x in url for x in g_ignoreSetResolved):#  (not url.startswith('plugin://plugin.video.f4mTester')):
            if regexs:
                if '$pyFunction:playmedia(' not in urllib.unquote_plus(regexs) and 'notplayable' not in urllib.unquote_plus(regexs)  :
                    #print 'setting isplayable',url, urllib.unquote_plus(regexs),url
                    liz.setProperty('IsPlayable', 'true')
            else:
                liz.setProperty('IsPlayable', 'true')
        else:
            addon_log( 'NOT setting isplayable'+url)
       
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(
                    ('Remove from E.L. Favorites','XBMC.RunPlugin(%s?mode=6&name=%s)'
                     %(sys.argv[0], urllib.quote_plus(name)))
                     )
            elif not name in FAV:
                fav_params = (
                    '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
                    %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart))
                    )
                if playlist:
                    fav_params += 'playlist='+urllib.quote_plus(str(playlist).replace(',','||'))
                if regexs:
                    fav_params += "&regexs="+regexs
                contextMenu.append(('Add to E.L. Favorites','XBMC.RunPlugin(%s)' %fav_params))
            liz.addContextMenuItems(contextMenu)
       
        if not playlist is None:
            if addon.getSetting('add_playlist') == "false":
                playlist_name = name.split(') ')[1]
                contextMenu_ = [
                    ('Play '+playlist_name+' PlayList','XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
                     %(sys.argv[0], urllib.quote_plus(playlist_name), urllib.quote_plus(str(playlist).replace(',','||'))))
                     ]
                liz.addContextMenuItems(contextMenu_)
        #print 'adding',name
 #       print url,totalitems
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,totalItems=total)
        #print 'added',name
        return ok

#----------------------------------------------- getSoup(url,data=None) -----------------------------------------------

def getSoup(url,data=None):
        #print 'getsoup',url,data
        if url.startswith('http://') or url.startswith('https://'):
            data = makeRequest(url)
            if re.search("#EXTM3U",data) or 'm3u' in url: 
                #print 'found m3u data',data
                return data
                
        elif data == None:
            if xbmcvfs.exists(url):
                if url.startswith("smb://") or url.startswith("nfs://"):
                    copy = xbmcvfs.copy(url, os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    if copy:
                        data = open(os.path.join(profile, 'temp', 'sorce_temp.txt'), "r").read()
                        xbmcvfs.delete(os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    else:
                        addon_log("failed to copy from smb:")
                else:
                    data = open(url, 'r').read()
                    if re.match("#EXTM3U",data)or 'm3u' in url: 
                        #print 'found m3u data',data
                        return data
            else:
                addon_log("Soup Data not found!")
                return
        return BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		
#----------------------------------------------- makeRequest(url, headers=None) -----------------------------------------------

def makeRequest(url, headers=None):
        try:
            if headers is None:
                headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
            req = urllib2.Request(url,None,headers)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            addon_log('URL: '+url)
            if hasattr(e, 'code'):
                addon_log('We failed with error code - %s.' % e.code)
                xbmc.executebuiltin("XBMC.Notification(DKTV Lounge,We failed with error code - "+str(e.code)+",10000,"+icon+")")
            elif hasattr(e, 'reason'):
                addon_log('We failed to reach a server.')
                addon_log('Reason: %s' %e.reason)
                xbmc.executebuiltin("XBMC.Notification(DKTV Lounge,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")

#-----------------------------------------------  addon_log(string) -----------------------------------------------

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.DKTVLounge3-%s]: %s" %(string))



resolve_url=['180upload.com', 'allmyvideos.net', 'bestreams.net', 'clicknupload.com', 'cloudzilla.to', 'movshare.net', 'novamov.com', 'nowvideo.sx', 'videoweed.es', 'daclips.in', 'datemule.com', 'fastvideo.in', 'faststream.in', 'filehoot.com', 'filenuke.com', 'sharesix.com', 'docs.google.com', 'plus.google.com', 'picasaweb.google.com', 'gorillavid.com', 'gorillavid.in', 'grifthost.com', 'hugefiles.net', 'ipithos.to', 'ishared.eu', 'kingfiles.net', 'mail.ru', 'my.mail.ru', 'videoapi.my.mail.ru', 'mightyupload.com', 'mooshare.biz', 'movdivx.com', 'movpod.net', 'movpod.in', 'movreel.com', 'mrfile.me', 'nosvideo.com', 'openload.io', 'played.to', 'bitshare.com', 'filefactory.com', 'k2s.cc', 'oboom.com', 'rapidgator.net', 'uploaded.net', 'primeshare.tv', 'bitshare.com', 'filefactory.com', 'k2s.cc', 'oboom.com', 'rapidgator.net', 'uploaded.net', 'sharerepo.com', 'stagevu.com', 'streamcloud.eu', 'streamin.to', 'thefile.me', 'thevideo.me', 'tusfiles.net', 'uploadc.com', 'zalaa.com', 'uploadrocket.net', 'uptobox.com', 'v-vids.com', 'veehd.com', 'vidbull.com', 'videomega.tv', 'vidplay.net', 'vidspot.net', 'vidto.me', 'vidzi.tv', 'vimeo.com', 'vk.com', 'vodlocker.com', 'xfileload.com', 'xvidstage.com', 'zettahost.tv']
g_ignoreSetResolved=['plugin.video.dramasonline','plugin.video.f4mTester','plugin.video.shahidmbcnet','plugin.video.SportsDevil','plugin.stream.vaughnlive.tv','plugin.video.ZemTV-shani']


#----------------------------------------------- getChannelItems(name,url,fanart)-----------------------------------------------

def getChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('channel', attrs={'name' : name.decode('utf-8')})
        items = channel_list('item')
        try:
            fanArt = channel_list('fanart')[0].string
            if fanArt == None:
                raise
        except:
            fanArt = fanart
        for channel in channel_list('subchannel'):
            name = channel('name')[0].string
            print name
            try:
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:
                if not channel('fanart'):
                    if addon.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                else:
                    fanArt = channel('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                pass
            try:
                desc = channel('info')[0].string
                if desc == None:
                    raise
            except:
                desc = ''

            try:
                genre = channel('genre')[0].string
                if genre == None:
                    raise
            except:
                genre = ''

            try:
                date = channel('date')[0].string
                if date == None:
                    raise
            except:
                date = ''

            try:
                credits = channel('credits')[0].string
                if credits == None:
                    raise
            except:
                credits = ''

            try:
                addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),3,thumbnail,fanArt,desc,genre,credits,date)
            except:
                addon_log('There was a problem adding directory - '+name.encode('utf-8', 'ignore'))
        getItems(items,fanArt)

#----------------------------------------------- getSubChannelItems(name,url,fanart) -----------------------------------------------

def getSubChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('subchannel', attrs={'name' : name.decode('utf-8')})
        items = channel_list('subitem')
        getItems(items,fanart)

def ClearCachedData():
	print 'Clear Cache Started'
	try: os.remove(ADDON_DATA + Decode('aHR0cF9tdzFfaXB0djY2X3R2'))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9tdzFfaXB0djY2X3R2LWdlbnJlcw=='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnByaXZhdGVzZXJ2ZXJfdHY='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnByaXZhdGVzZXJ2ZXJfdHYtZ2VucmVz'))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnJvY2tldF90dg=='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnJvY2tldF90di1nZW5yZXM='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('c2V0dGluZ3MueG1s'))
	except: pass

	print 'Clear Cache Ended'

	dialog = xbmcgui.Dialog()
	dialog.ok("Cached Data Cleared", "All Done, Cached Data Has Now Been Cleared.")
		
#----------------------------------------------- GetSublinks(name,url,iconimage,fanart)-----------------------------------------------

def GetSublinks(name,url,iconimage,fanart):
    print name
    List=[]; ListU=[]; c=0
    all_videos = regex_get_all(url, 'sublink:', '--#')
    for a in all_videos:
        if 'LISTSOURCE:' in a:
            vurl = regex_from_to(a, 'LISTSOURCE:', '::')
            linename = regex_from_to(a, 'LISTNAME:', '::')
        else:
            vurl = a.replace('sublink:','').replace('--#','')
            linename = name
        if len(vurl) > 10:
            c=c+1; List.append(linename); ListU.append(vurl)
 
    if c==1:
        try:
            liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=ListU[0],listitem=liz)
            xbmc.Player().play(urlsolver(ListU[0]), liz)
        except:
            pass
    else:
         dialog=xbmcgui.Dialog()
         rNo=dialog.select('E.L. Select A Source', List)
         if rNo>=0:
             rName=str(List[rNo])
             rURL=str(ListU[rNo])
             #print 'Sublinks   Name:' + name + '   url:' + rURL
             try:
                 liz=xbmcgui.ListItem(rName, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": rName } )
                 ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=rURL,listitem=liz)
                 xbmc.Player().play(urlsolver(rURL), liz)
             except:
                 pass
#----------------------------------------------- parse_regex(reg_item) -----------------------------------------------

def parse_regex(reg_item):
        print '#################################################################################################'
        print reg_item
        print '#################################################################################################'
        try:
            regexs = {}
            for i in reg_item:
                regexs[i('name')[0].string] = {}
                #regexs[i('name')[0].string]['expre'] = i('expres')[0].string
                try:
                    regexs[i('name')[0].string]['expre'] = i('expres')[0].string
                    if not regexs[i('name')[0].string]['expre']:
                        regexs[i('name')[0].string]['expre']=''
                except:
                    addon_log("Regex: -- No Referer --")
                regexs[i('name')[0].string]['page'] = i('page')[0].string
                try:
                    regexs[i('name')[0].string]['refer'] = i('referer')[0].string
                except:
                    addon_log("Regex: -- No Referer --")
                try:
                    regexs[i('name')[0].string]['connection'] = i('connection')[0].string
                except:
                    addon_log("Regex: -- No connection --")

                try:
                    regexs[i('name')[0].string]['notplayable'] = i('notplayable')[0].string
                except:
                    addon_log("Regex: -- No notplayable --")
                    
                try:
                    regexs[i('name')[0].string]['noredirect'] = i('noredirect')[0].string
                except:
                    addon_log("Regex: -- No noredirect --")
                try:
                    regexs[i('name')[0].string]['origin'] = i('origin')[0].string
                except:
                    addon_log("Regex: -- No origin --")
                try:
                    regexs[i('name')[0].string]['includeheaders'] = i('includeheaders')[0].string
                except:
                    addon_log("Regex: -- No includeheaders --")                            
                    
                try:
                    regexs[i('name')[0].string]['x-req'] = i('x-req')[0].string
                except:
                    addon_log("Regex: -- No x-req --")
                try:
                    regexs[i('name')[0].string]['x-forward'] = i('x-forward')[0].string
                except:
                    addon_log("Regex: -- No x-forward --")

                try:
                    regexs[i('name')[0].string]['agent'] = i('agent')[0].string
                except:
                    addon_log("Regex: -- No User Agent --")
                try:
                    regexs[i('name')[0].string]['post'] = i('post')[0].string
                except:
                    addon_log("Regex: -- Not a post")
                try:
                    regexs[i('name')[0].string]['rawpost'] = i('rawpost')[0].string
                except:
                    addon_log("Regex: -- Not a rawpost")
                try:
                    regexs[i('name')[0].string]['htmlunescape'] = i('htmlunescape')[0].string
                except:
                    addon_log("Regex: -- Not a htmlunescape")


                try:
                    regexs[i('name')[0].string]['readcookieonly'] = i('readcookieonly')[0].string
                except:
                    addon_log("Regex: -- Not a readCookieOnly")
                #print i
                try:
                    regexs[i('name')[0].string]['cookiejar'] = i('cookiejar')[0].string
                    if not regexs[i('name')[0].string]['cookiejar']:
                        regexs[i('name')[0].string]['cookiejar']=''
                except:
                    addon_log("Regex: -- Not a cookieJar")                          
                try:
                    regexs[i('name')[0].string]['setcookie'] = i('setcookie')[0].string
                except:
                    addon_log("Regex: -- Not a setcookie")
                try:
                    regexs[i('name')[0].string]['appendcookie'] = i('appendcookie')[0].string
                except:
                    addon_log("Regex: -- Not a appendcookie")
                                            
                try:
                    regexs[i('name')[0].string]['ignorecache'] = i('ignorecache')[0].string
                except:
                    addon_log("Regex: -- no ignorecache")
                #try:
                #    regexs[i('name')[0].string]['ignorecache'] = i('ignorecache')[0].string
                #except:
                #    addon_log("Regex: -- no ignorecache")          

            regexs = urllib.quote(repr(regexs))
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            print regexs
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            return regexs
            
        except:
            regexs = None
            addon_log('regex Error: '+name.encode('utf-8', 'ignore'))

#----------------------------------------------- parse_m3u(data) -----------------------------------------------

def parse_m3u(data):
    content = data.rstrip()
    match = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)').findall(content)
    total = len(match)
    #print 'total m3u links',total
    for other,channel_name,stream_url in match:
        channel_name = channel_name.replace('[COLOR green][B]', '[B]').replace('[COLOR blue][B]', '[B]').replace('[COLOR white][B]', '[B]').replace('[/B][/COLOR]', '[/B]').replace('[COLOR yellow][B]', '[B]').replace('HD Footy list - only active when PL games on', 'Live Football By DKTV Lounge').replace('Next match will be available', '')
        if 'tvg-logo' in other:
            thumbnail = re_me(other,'tvg-logo=[\'"](.*?)[\'"]')
            if 'apple_itunes_like_hd_icon_by_phjellming.jpg' in thumbnail:
                thumbnail = 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png'
            if thumbnail:
                if thumbnail.startswith('http'):
                    thumbnail = thumbnail
                
                elif not addon.getSetting('logo-folderPath') == "":
                    logo_url = addon.getSetting('logo-folderPath')
                    thumbnail = logo_url + thumbnail

                else:
                    thumbnail = thumbnail
            #else:
           
        else:
            thumbnail = ''
        if 'type' in other:
            mode_type = re_me(other,'type=[\'"](.*?)[\'"]')
            if mode_type == 'yt-dl':
                stream_url = stream_url +"&mode=18"
            elif mode_type == 'regex':
                url = stream_url.split('&regexs=')
                #print url[0] getSoup(url,data=None)
                regexs = parse_regex(getSoup('',data=url[1]))
                addLink(url[0], channel_name,thumbnail,'','','','','',None,regexs,total)
                continue
        addLink(stream_url, channel_name,thumbnail,'','','','','',None,'',total)
		
    xbmc.executebuiltin("Container.SetViewMode(50)")

#----------------------------------------------- re_me(data, re_patten) -----------------------------------------------

player = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
item = xbmcgui.ListItem
resolve = xbmcplugin.setResolvedUrl
addonInfo = xbmcaddon.Addon().getAddonInfo
setting = xbmcaddon.Addon().getSetting
lang = xbmcaddon.Addon().getLocalizedString
execute = xbmc.executebuiltin

def re_me(data, re_patten):
    match = ''
    m = re.search(re_patten, data)
    if m != None:
        match = m.group(1)
    else:
        match = ''
    return match

def resolveUrl(name, url, audio, image, fanart, playable, content):
    print 'Resolving Url Name: ' + name + 'URL: ' + url
    try:
        if '.f4m'in url:
            label = cleantitle(name)
            ext = url.split('?')[0].split('&')[0].split('|')[0].rsplit('.')[-1].replace('/', '').lower()
            if not ext == 'f4m': raise Exception()
            from resources.lib.libraries.f4mproxy.F4mProxy import f4mProxyHelper
            return f4mProxyHelper().playF4mLink(url, label, None, None,'',image)
            print ' ##################   1   ################## '


        #legacy issue, will be removed later
        if 'afdah.org' in url and not '</source>' in url: url += '<source>afdah</source>'

        if '</source>' in url:
            source = re.compile('<source>(.+?)</source>').findall(url)[0]
            url = re.compile('(.+?)<source>').findall(url)[0]

            for i in ['_mv', '_tv', '_mv_tv']:
                try: call = __import__('resources.lib.sources.%s%s' % (source, i), globals(), locals(), ['object'], -1).source()
                except: pass
			
            from resources.lib import sources ; d = sources.sources()
            print ' ##################   2   ################## '

            url = call.get_sources(url, d.hosthdfullDict, d.hostsdfullDict, d.hostlocDict)

            if type(url) == list and len(url) == 1:
                url = url[0]['url']

            elif type(url) == list:
		print 'ELIF : ' + url
                url = sorted(url, key=lambda k: k['quality'])
                for i in url: i.update((k, '720p') for k, v in i.iteritems() if v == 'HD')
                for i in url: i.update((k, '480p') for k, v in i.iteritems() if v == 'SD')
                q = ['[B]%s[/B] | %s' % (i['source'].upper(), i['quality'].upper()) for i in url]
                u = [i['url'] for i in url]
                select = control.selectDialog(q)
                if select == -1: return
                url = u[select]

            url = call.resolve(url)


        from resources.lib import resolvers
        host = (urlparse.urlparse(url).netloc).rsplit('.', 1)[0].rsplit('.')[-1]
        url = resolvers.request(url)
        print ' ##################   3   ################## ' + url

        if type(url) == list and len(url) == 1:
            url = url[0]['url']

        elif type(url) == list:
            url = sorted(url, key=lambda k: k['quality'])
            for i in url: i.update((k, '720p') for k, v in i.iteritems() if v == 'HD')
            for i in url: i.update((k, '480p') for k, v in i.iteritems() if v == 'SD')
            q = ['[B]%s[/B] | %s' % (host.upper(), i['quality'].upper()) for i in url]
            u = [i['url'] for i in url]
            select = control.selectDialog(q)
            if select == -1: return
            url = u[select]

        if url == None: raise Exception()
    except:
        return infoDialog(lang(30705).encode('utf-8'))
        pass

    if playable == 'true':
        item = item(path=url)
        print ' ##################   4   ################## ' + item
        return resolve(int(sys.argv[1]), True, item)
    else:
        label = cleantitle(name)
        item = item(path=url, iconImage=image, thumbnailImage=image)
        item.setInfo( type='Video', infoLabels = {'title': label} )
        playlist.clear()
	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PLAYING RESOLVED URL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        player.play(url, item)

def addonIcon():
    appearance = setting('appearance').lower()
    if appearance in ['-', '']: return addonInfo('icon')
    else: return os.path.join(addonPath, 'resources', 'media', appearance, 'icon.png')

def infoDialog(message, heading=addonInfo('name'), icon=addonIcon(), time=3000):
    try: dialog.notification(heading, message, icon, time, sound=False)
    except: execute("Notification(%s,%s, %s, %s)" % (heading, message, time, icon))

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

Dialog = xbmcgui.Dialog()



	
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Modules **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def getRegexParsed(regexs, url,cookieJar=None,forCookieJarOnly=False,recursiveCall=False,cachedPages={}, rawPost=False, cookie_jar_file=None):#0,1,2 = URL, regexOnly, CookieJarOnly
        if not recursiveCall:
            regexs = eval(urllib.unquote(regexs))
        #cachedPages = {}
        #print 'url',url
        doRegexs = re.compile('\$doregex\[([^\]]*)\]').findall(url)
        #print 'doRegexs',doRegexs,regexs
        setresolved=True
              
 


        for k in doRegexs:
            if k in regexs:
                #print 'processing ' ,k
                m = regexs[k]
                #print m
                cookieJarParam=False


                if  'cookiejar' in m: # so either create or reuse existing jar
                    #print 'cookiejar exists',m['cookiejar']
                    cookieJarParam=m['cookiejar']
                    if  '$doregex' in cookieJarParam:
                        cookieJar=getRegexParsed(regexs, m['cookiejar'],cookieJar,True, True,cachedPages)
                        cookieJarParam=True
                    else:
                        cookieJarParam=True
                #print 'm[cookiejar]',m['cookiejar'],cookieJar
                if cookieJarParam:
                    if cookieJar==None:
                        #print 'create cookie jar'
                        cookie_jar_file=None
                        if 'open[' in m['cookiejar']:
                            cookie_jar_file=m['cookiejar'].split('open[')[1].split(']')[0]
                            
                        cookieJar=getCookieJar(cookie_jar_file)
                        if cookie_jar_file:
                            saveCookieJar(cookieJar,cookie_jar_file)
                        #import cookielib
                        #cookieJar = cookielib.LWPCookieJar()
                        #print 'cookieJar new',cookieJar
                    elif 'save[' in m['cookiejar']:
                        cookie_jar_file=m['cookiejar'].split('save[')[1].split(']')[0]
                        complete_path=os.path.join(profile,cookie_jar_file)
                        print 'complete_path',complete_path
                        saveCookieJar(cookieJar,cookie_jar_file)
                        
 
                if  m['page'] and '$doregex' in m['page']:
                    m['page']=getRegexParsed(regexs, m['page'],cookieJar,recursiveCall=True,cachedPages=cachedPages)

                if 'setcookie' in m and m['setcookie'] and '$doregex' in m['setcookie']:
                    m['setcookie']=getRegexParsed(regexs, m['setcookie'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
                if 'appendcookie' in m and m['appendcookie'] and '$doregex' in m['appendcookie']:
                    m['appendcookie']=getRegexParsed(regexs, m['appendcookie'],cookieJar,recursiveCall=True,cachedPages=cachedPages)

                 
                if  'post' in m and '$doregex' in m['post']:
                    m['post']=getRegexParsed(regexs, m['post'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
                    #print 'post is now',m['post']

                if  'rawpost' in m and '$doregex' in m['rawpost']:
                    m['rawpost']=getRegexParsed(regexs, m['rawpost'],cookieJar,recursiveCall=True,cachedPages=cachedPages,rawPost=True)
                    #print 'rawpost is now',m['rawpost']
  
                if 'rawpost' in m and '$epoctime$' in m['rawpost']:
                    m['rawpost']=m['rawpost'].replace('$epoctime$',getEpocTime())
  
                if 'rawpost' in m and '$epoctime2$' in m['rawpost']:
                    m['rawpost']=m['rawpost'].replace('$epoctime2$',getEpocTime2())

  
                link=''
                if m['page'] and m['page'] in cachedPages and not 'ignorecache' in m and forCookieJarOnly==False :
                    link = cachedPages[m['page']]
                else:
                    if m['page'] and  not m['page']=='' and  m['page'].startswith('http'):
                        if '$epoctime$' in m['page']:
                            m['page']=m['page'].replace('$epoctime$',getEpocTime())
                        if '$epoctime2$' in m['page']:
                            m['page']=m['page'].replace('$epoctime2$',getEpocTime2())

                        #print 'Ingoring Cache',m['page']
                        page_split=m['page'].split('|')
                        pageUrl=page_split[0]
                        header_in_page=None
                        if len(page_split)>1:
                            header_in_page=page_split[1]
                        req = urllib2.Request(pageUrl)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1')
                        if 'refer' in m:
                            req.add_header('Referer', m['refer'])
                        if 'agent' in m:
                            req.add_header('User-agent', m['agent'])
                        if 'x-req' in m:
                            req.add_header('X-Requested-With', m['x-req'])
                        if 'x-forward' in m:
                            req.add_header('X-Forwarded-For', m['x-forward'])
                        if 'setcookie' in m:
                            print 'adding cookie',m['setcookie']
                            req.add_header('Cookie', m['setcookie'])
                        if 'appendcookie' in m:
                            print 'appending cookie to cookiejar',m['appendcookie']
                            cookiestoApend=m['appendcookie']
                            cookiestoApend=cookiestoApend.split(';')
                            for h in cookiestoApend:
                                n,v=h.split('=')
                                w,n= n.split(':')
                                ck = cookielib.Cookie(version=0, name=n, value=v, port=None, port_specified=False, domain=w, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
                                cookieJar.set_cookie(ck)

                                

                            
                        if 'origin' in m:
                            req.add_header('Origin', m['origin'])
                        if header_in_page:
                            header_in_page=header_in_page.split('&')
                            for h in header_in_page:
                                n,v=h.split('=')
                                req.add_header(n,v)


                        if not cookieJar==None:
                            #print 'cookieJarVal',cookieJar
                            cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
                            opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
                            opener = urllib2.install_opener(opener)
                            if 'noredirect' in m:
                                opener2 = urllib2.build_opener(NoRedirection)
                                opener = urllib2.install_opener(opener2)
                                
                        if 'connection' in m:
                            print '..........................connection//////.',m['connection']
                            from keepalive import HTTPHandler
                            keepalive_handler = HTTPHandler()
                            opener = urllib2.build_opener(keepalive_handler)
                            urllib2.install_opener(opener)
                            
                        #print 'after cookie jar'
                        post=None

                        if 'post' in m:
                            postData=m['post']
                            if '$LiveStreamRecaptcha' in postData:
                                (captcha_challenge,catpcha_word)=processRecaptcha(m['page'])
                                if captcha_challenge:
                                    postData+='recaptcha_challenge_field:'+captcha_challenge+',recaptcha_response_field:'+catpcha_word
                            splitpost=postData.split(',');
                            post={}
                            for p in splitpost:
                                n=p.split(':')[0];
                                v=p.split(':')[1];
                                post[n]=v
                            post = urllib.urlencode(post)

                        if 'rawpost' in m:
                            post=m['rawpost']
                            if '$LiveStreamRecaptcha' in post:
                                (captcha_challenge,catpcha_word)=processRecaptcha(m['page'])
                                if captcha_challenge:
                                   post+='&recaptcha_challenge_field='+captcha_challenge+'&recaptcha_response_field='+catpcha_word


                            

                        if post:
                            response = urllib2.urlopen(req,post)
                        else:
                            response = urllib2.urlopen(req)

                        link = response.read()
                        link=javascriptUnEscape(link)
                        #print link This just print whole webpage in LOG
                        if 'includeheaders' in m:
                            link+=str(response.headers.get('Set-Cookie'))

                        response.close()
                        cachedPages[m['page']] = link
                        #print link
                        #print 'store link for',m['page'],forCookieJarOnly
                        
                        if forCookieJarOnly:
                            return cookieJar# do nothing
                    elif m['page'] and  not m['page'].startswith('http'):
                        if m['page'].startswith('$pyFunction:'):
                            val=doEval(m['page'].split('$pyFunction:')[1],'',cookieJar )
                            if forCookieJarOnly:
                                return cookieJar# do nothing
                            link=val
                        else:
                            link=m['page']
                if '$pyFunction:playmedia(' in m['expre'] or 'ActivateWindow'  in m['expre']   or  any(x in url for x in g_ignoreSetResolved):
                    setresolved=False
                if  '$doregex' in m['expre']:
                    m['expre']=getRegexParsed(regexs, m['expre'],cookieJar,recursiveCall=True,cachedPages=cachedPages)
                    
                
                if not m['expre']=='':
                    print 'doing it ',m['expre']
                    if '$LiveStreamCaptcha' in m['expre']:
                        val=askCaptcha(m,link,cookieJar)
                        #print 'url and val',url,val
                        url = url.replace("$doregex[" + k + "]", val)
                    elif m['expre'].startswith('$pyFunction:'):
                        #print 'expeeeeeeeeeeeeeeeeeee',m['expre']
                        val=doEval(m['expre'].split('$pyFunction:')[1],link,cookieJar )
                        if 'ActivateWindow' in m['expre']: return 
                        print 'still hre'
                        print 'url k val',url,k,val

                        url = url.replace("$doregex[" + k + "]", val)
                    else:
                        if not link=='':
                            reg = re.compile(m['expre']).search(link)
                            val=''
                            try:
                                val=reg.group(1).strip()
                            except: traceback.print_exc()
                        else:
                            val=m['expre']
                        if rawPost:
                            print 'rawpost'
                            val=urllib.quote_plus(val)
                        if 'htmlunescape' in m:
                            #val=urllib.unquote_plus(val)
                            import HTMLParser
                            val=HTMLParser.HTMLParser().unescape(val)                     
                        url = url.replace("$doregex[" + k + "]", val)
                        #return val
                else:           
                    url = url.replace("$doregex[" + k + "]",'')
        if '$epoctime$' in url:
            url=url.replace('$epoctime$',getEpocTime())
        if '$epoctime2$' in url:
            url=url.replace('$epoctime2$',getEpocTime2())

        if '$GUID$' in url:
            import uuid
            url=url.replace('$GUID$',str(uuid.uuid1()).upper())
        if '$get_cookies$' in url:
            url=url.replace('$get_cookies$',getCookiesString(cookieJar))   

        if recursiveCall: return url
        print 'final url',url
        if url=="": 
        	return
        else:
        	return url,setresolved

def javascriptUnEscape(str):
	print '\n\n*****>>> Before Unescaped JavaScript:  ' + str + '\n\n'
	js=re.findall('unescape\(\'(.*?)\'',str)
	print 'js',js
	if (not js==None) and len(js)>0:
		for j in js:
			#print urllib.unquote(j)
			str=str.replace(j ,urllib.unquote(j))
			print '\n\n*****>>> After Unescaped JavaScript:  ' + str + '\n\n'
	return str

def playsetresolved(url,name,iconimage,setresolved=True):
    if setresolved:
		print 'Resolved Url Start'
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
		liz.setInfo(type='Video', infoLabels={'Title':name})
		liz.setProperty("IsPlayable","true")
		liz.setPath(str(url))
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		print 'Resolved Url End'
    else:
	print 'Else Resolved Url'
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')    

def AllLiveTV(url):
	parser.Category('Entertainment', url)
	parser.Category('Sports', url)

def m3u_online():		
	content = make_request(online_m3u)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def m3u_onlinemovie():		
	content = make_request(online_movielist)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def m3u_PLP():		
	content = make_request(online_PLP)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def m3u_LiveTV():		
	content = make_request(online_LiveTV)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		try:
			m3u_playlist(name, url, thumb)
		except:
			pass

def m3u_playlist(name, url, thumb):	
	name = re.sub('\s+', ' ', name).strip()			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')			
			add_dir1(name, url, '', thumb, thumb)			
		else:	
			add_dir1(name, url, '', ICON, FANART)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url	
		else:			
			url = url
		if 'tvg-logo' in thumb:				
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			add_link1(name, url, 45, thumb, thumb)			
		else:				
			add_link1(name, url, 45, ICON, FANART)	

def play_video(url):
	media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def add_dir1(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok
	
def add_link1(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)  


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Portals **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def addPortal(portal):


	if portal['url'] == '':
		return;

	url = build_url({
		'mode': 'genres', 
		'portal' : json.dumps(portal)
		});
	
	cmd = 'XBMC.RunPlugin(' + base_url + '?mode=cache&stalker_url=' + portal['url'] + ')';
	ccd = 'XBMC.RunPlugin(' + base_url + '?mode=53)';
	
	li = xbmcgui.ListItem(portal['name'], iconImage=ART+'icon.png')
	li.addContextMenuItems([ ('Clear Cache', cmd), ('Clear Cached Data', ccd) ]);
	

	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
	
def build_url(query):
	return base_url + '?' + urllib.urlencode(query)


def homeLevel():
	global portal_1, go;
	
	#todo - check none portal

	if go:
		addPortal(portal_1);
	
		xbmcplugin.endOfDirectory(addon_handle);
	
	AUTO_VIEW('504')

def genreLevel():
	
	try:
		data = load_channels.getGenres(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		
		return;

	data = data['genres'];
		
	url = build_url({
		'mode': 'vod', 
		'portal' : json.dumps(portal)
	});
			
	li = xbmcgui.ListItem('VoD', iconImage='DefaultVideo.png')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
	
	
	for id, i in data.iteritems():

		title 	= i["title"];
		
		url = build_url({
			'mode': 'channels', 
			'genre_id': id, 
			'genre_name': title.title(), 
			'portal' : json.dumps(portal)
			});
			
		if id == '10':
			iconImage = 'OverlayLocked.png';
		else:
			iconImage = 'DefaultVideo.png';
			
		li = xbmcgui.ListItem(title.title(), iconImage=iconImage)
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True);
		

	xbmcplugin.endOfDirectory(addon_handle);

def vodLevel():
	
	try:
		data = load_channels.getVoD(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;
	
	
	data = data['vod'];
	
		
	for i in data:
		name 	= i["name"];
		cmd 	= i["cmd"];
		logo 	= i["logo"];
		
		
		if logo != '':
			logo_url = portal['url'] + logo;
		else:
			logo_url = 'DefaultVideo.png';
				
				
		url = build_url({
				'mode': 'play', 
				'cmd': cmd, 
				'tmp' : '0', 
				'title' : name.encode("utf-8"),
				'genre_name' : 'VoD',
				'logo_url' : logo_url, 
				'portal' : json.dumps(portal)
				});
			

		li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url)
		li.setInfo(type='Video', infoLabels={ "Title": name })

		xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_UNSORTED);
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
	xbmcplugin.endOfDirectory(addon_handle);

def channelLevel():
	stop=False;
		
	try:
		data = load_channels.getAllChannels(portal['mac'], portal['url'], portal['serial'], addondir);
		
	except Exception as e:
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;
	
	
	data = data['channels'];
	genre_name 	= args.get('genre_name', None);
	
	genre_id_main = args.get('genre_id', None);
	genre_id_main = genre_id_main[0];
	
	if genre_id_main == '10' and portal['parental'] == 'true':
		result = xbmcgui.Dialog().input('Parental', hashlib.md5(portal['password'].encode('utf-8')).hexdigest(), type=xbmcgui.INPUT_PASSWORD, option=xbmcgui.PASSWORD_VERIFY);
		if result == '':
			stop = True;

	
	if stop == False:
		for i in data.values():
			
			name 		= i["name"];
			cmd 		= i["cmd"];
			tmp 		= i["tmp"];
			number 		= i["number"];
			genre_id 	= i["genre_id"];
			logo 		= i["logo"];
		
			if genre_id_main == '*' and genre_id == '10' and portal['parental'] == 'true':
				continue;
		
		
			if genre_id_main == genre_id or genre_id_main == '*':
		
				if logo != '':
					logo_url = portal['url'] + '/stalker_portal/misc/logos/320/' + logo;
				else:
					logo_url = 'DefaultVideo.png';
				
				
				url = build_url({
					'mode': 'play', 
					'cmd': cmd, 
					'tmp' : tmp, 
					'title' : name.encode("utf-8"),
					'genre_name' : genre_name,
					'logo_url' : logo_url,  
					'portal' : json.dumps(portal)
					});
			

				li = xbmcgui.ListItem(name, iconImage=logo_url, thumbnailImage=logo_url);
				li.setInfo(type='Video', infoLabels={ 
					'title': name,
					'count' : number
					});

				xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li);
		
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_PLAYLIST_ORDER);
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
		xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_PROGRAM_COUNT);
		
		
		xbmcplugin.endOfDirectory(addon_handle);

def playLevel():
	
	dp = xbmcgui.DialogProgressBG();
	dp.create('Channel', 'Loading ...');
	
	title 	= args['title'][0];
	cmd 	= args['cmd'][0];
	tmp 	= args['tmp'][0];
	genre_name 	= args['genre_name'][0];
	logo_url 	= args['logo_url'][0];
	
	try:
		if genre_name != 'VoD':
			url = load_channels.retriveUrl(portal['mac'], portal['url'], portal['serial'], cmd, tmp);
		else:
			url = load_channels.retriveVoD(portal['mac'], portal['url'], portal['serial'], cmd);

	
	except Exception as e:
		dp.close();
		xbmcgui.Dialog().notification(addonname, str(e), xbmcgui.NOTIFICATION_ERROR );
		return;

	
	dp.update(80);
	
	title = title.decode("utf-8");
	
	title += ' (' + portal['name'] + ')';
	
#	li = xbmcgui.ListItem(title, iconImage=logo_url); <modified 9.0.19
	li = xbmcgui.ListItem(title, iconImage=logo_url, thumbnailImage=logo_url);
	li.setInfo('video', {'Title': title, 'Genre': genre_name});
	xbmc.Player().play(item=url, listitem=li);
	
	dp.update(100);
	
	dp.close();


mode = args.get('mode', None);
portal =  args.get('portal', None)


if portal is None:
	portal_1 = config.portalConfig('1');

else:
	portal = json.loads(portal[0]);

	portal = config.portalConfig('1');

if mode is None:
	Premium_TV(PASSCODE, PASSWORD);

elif mode[0] == 'cache':	
	stalker_url = args.get('stalker_url', None);
	stalker_url = stalker_url[0];	
	load_channels.clearCache(stalker_url, addondir);

elif mode[0] == 'genres':
	genreLevel();
		
elif mode[0] == 'vod':
	vodLevel();

elif mode[0] == 'channels':
	channelLevel();
	
elif mode[0] == 'play':
	playLevel();
	
elif mode[0] == 'server':
	port = addon.getSetting('server_port');
	
	action =  args.get('action', None);
	action = action[0];
	
	dp = xbmcgui.DialogProgressBG();
	dp.create('IPTV', 'Just A Second ...');
	
	if action == 'start':
	
		if server.serverOnline():
			xbmcgui.Dialog().notification(addonname, 'Server already started.\nPort: ' + str(port), xbmcgui.NOTIFICATION_INFO );
		else:
			server.startServer();
			time.sleep(5);
			if server.serverOnline():
				xbmcgui.Dialog().notification(addonname, 'Server started.\nPort: ' + str(port), xbmcgui.NOTIFICATION_INFO );
			else:
				xbmcgui.Dialog().notification(addonname, 'Server not started. Wait one moment and try again. ', xbmcgui.NOTIFICATION_ERROR );
				
	else:
		if server.serverOnline():
			server.stopServer();
			time.sleep(5);
			xbmcgui.Dialog().notification(addonname, 'Server stopped.', xbmcgui.NOTIFICATION_INFO );
		else:
			xbmcgui.Dialog().notification(addonname, 'Server is already stopped.', xbmcgui.NOTIFICATION_INFO );
			
	dp.close();

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** Test Area **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def PremiumTVMenu():
	global portal_1, go;

	if go:
		modules.AddTestDir('Clear Cached Data - Will Delete Passcode - Retype in Addon Settings', '', 50, ART+'icon.png', description="", isFolder=False, background='')
		addPortal(portal_1);
		xbmcplugin.endOfDirectory(addon_handle);

def ClearCachedData():
	print 'Clear Cache Started'
	try: os.remove(ADDON_DATA + Decode('aHR0cF9tdzFfaXB0djY2X3R2'))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9tdzFfaXB0djY2X3R2LWdlbnJlcw=='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnByaXZhdGVzZXJ2ZXJfdHY='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnByaXZhdGVzZXJ2ZXJfdHYtZ2VucmVz'))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnJvY2tldF90dg=='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('aHR0cF9wb3J0YWxfaXB0dnJvY2tldF90di1nZW5yZXM='))
	except: pass

	try: os.remove(ADDON_DATA + Decode('c2V0dGluZ3MueG1s'))
	except: pass

	print 'Clear Cache Ended'

	dialog = xbmcgui.Dialog()
	dialog.ok("Cached Data Cleared", "All Done, Cached Data Has Now Been Cleared.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** ADDON SWITCH **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

params = get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None

playlist=None
fav_mode=None
regexs=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
try:
    playlist=eval(urllib.unquote_plus(params["playlist"]).replace('||',','))
except:
		pass
try:
    fav_mode=int(params["fav_mode"])
except:
    pass
try:
    regexs=params["regexs"]
except:
    pass
try:
    playable = params['playable']
except:
    playable = '0'
try:
    content = params['content']
except:
    content = '0'
try:
    tvshow = params['tvshow']
except:
    tvshow = '0'
try:
    audio = params['audio']
except:
    audio = '0'
try:
    image = params['image']
except:
    image = '0'
try:
    fanart = params['fanart']
except:
    fanart = '0'
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
print "Playlist: "+str(playlist)
print "FavMode: "+str(fav_mode)
print "Regexs: "+str(regexs)



if mode == None		: Home_Menu(PASSCODE, PASSWORD)
elif mode == 1		: Movies(PASSCODE, PASSWORD)
elif mode == 2		: Sports_Centre(PASSCODE, PASSWORD)
elif mode == 3		: get_All_Rows(url)
elif mode == 4		: replay_Menu()
elif mode == 5		: TV_Shows(PASSCODE, PASSWORD)
elif mode == 6		: Sports_Replays(PASSCODE, PASSWORD)
elif mode == 7		: ODMenu.MOVIES_OD()

elif mode == 8 	: 
	getData(url,fanart)
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode == 9		: getChannelItems(name,url,fanart)

elif mode == 10:
    addon_log("setResolvedUrl")
    if not url.startswith("plugin://plugin") or not any(x in url for x in g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
        print 'Not setting setResolvedUrl'
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')

elif mode == 11:
    addon_log("getRegexParsed")
    url,setresolved = getRegexParsed(regexs, url)
    if url:
        playsetresolved(url,name,iconimage,setresolved)
    else:
        xbmc.executebuiltin("XBMC.Notification(E.L.,Failed to extract regex. - "+"this"+",4000,"+icon+")")
elif mode == 12		: lists.LiveTVFull(name)
elif mode == 13		: lists.List_LiveTVFull(name)
elif mode == 14		: lists.List_LiveTVCats()
elif mode == 15: 
	#print '***** PLP Resolve'
	Plp.resolveUrl(name, url, audio, image, fanart, playable, content)
elif mode == 16  	: Resolve(name, url)
elif mode == 17  	: LISTS(url)
elif mode == 18  	: LISTS2(url)
elif mode == 19  	: LISTS3(url)
elif mode == 20  	: lists.Lists()
elif mode == 21  	: lists.TESTCATS2()
elif mode == 22  	: streams.ParseURL(url)
elif mode == 23  	: lists.TESTCATS3()
elif mode == 24	 	: lists.Build_MenuMovies()
elif mode == 25  	: lists.TESTCATS4()
elif mode == 26	 	: lists.Build_MenuTrailers()
elif mode == 27		: yt.PlayVideo(url)
elif mode == 28		: modules.TestPlayUrl(name, url, iconimage)
elif mode == 29		: WWE_Home()
elif mode == 30 	: SoapsOD.Test_Regex(url)
elif mode == 31		: Wsimpsons.ParseURL(url)
elif mode == 32		:()
elif mode == 33		: modules.Resolve(name, url)
elif mode == 34		: modules.TestMenuDIR(url)
elif mode == 36		: parser.ChannelLinks(name, url)
elif mode == 37		: parser.MovieCategories(url)
elif mode == 38		: parser.Category(name, url)
elif mode == 39		: ODMenu.ALLMOVIES_OD(url)
elif mode == 40		: Live_Today(PASSCODE, PASSWORD)
elif mode == 41		: parser.Category(name, url)
elif mode == 42		: AllLiveTV(url)
elif mode == 43		: Sports_Channels(PASSCODE, PASSWORD)
elif mode == 44		: m3u_online()
elif mode == 45		: play_video(url)
elif mode == 46		: m3u_onlinemovie()
elif mode == 47		: m3u_PLP()
elif mode == 48		: m3u_LiveTV()
elif mode == 49		: PremiumTVMenu()
elif mode == 50		: ClearCachedData()
elif mode == 51		: Premium_TV(PASSCODE, PASSWORD)

elif mode == 400 	: lists.Live(url)
elif mode == 404 	: lists.TestPlayUrl(name, url, iconimage)





#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#********** ADDON FINISH **********
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
xbmcplugin.endOfDirectory(int(sys.argv[1]))
