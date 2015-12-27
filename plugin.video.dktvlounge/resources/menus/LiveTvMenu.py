'''
import re, sys, os, xbmc, xbmcaddon, xbmcplugin, xbmcgui, urllib, urllib2
from resources.modules import modules, yt
from resources.modules.parsers import parser

ADDON_ID = 'plugin.video.dktvlounge'
ADDON = xbmcaddon.Addon(id=ADDON_ID)
BaseURL = 'http://chameleon.x10host.com/test/links/'
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID + '/resources/icons/'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'fanart.jpg'))

#********** Test Text Files YouTube**********
LEntertainment = 'LiVE/LIVETV.m3u'
LMovies = 'LiVE/LIVEMOVIES.m3u'
LKids = 'LiVE/LIVEKIDS.m3u'
LSports = 'LiVE/LIVESPORTS.m3u'

def AllLiveTV(url):
	parser.Category('Entertainment', url)

'''