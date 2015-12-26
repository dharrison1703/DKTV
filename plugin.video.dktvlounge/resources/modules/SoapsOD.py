import re, urllib2, sys, urllib

url = ''

def Test_Regex(url):
	Html = OPEN_URL(url)
	Im_A_Celebrity = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(Html)
	for url, name in Im_A_Celebrity:
		if 'hugefiles' in url:
			addDir((name).replace('_720p','').replace('.HDTV.x264','').replace('-SS.mp4',''),'','','','','','','',showcontext=False)
		else:
			pass

		
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

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


#xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

# this line below is only here to initiate testregex method when the script is done and passes the url to it same as mode would do in kodi script
# ah right oki if i get tht far as to putting somethin in addon ill come back to you hahah
# lol sound mate
#Test_Regex(url)

# that should work actually mate bit simpler
# see that import and urllib2 i wouldnt have put in lol
# lol ive missed the open url any way hahah
# like that lol
# ur to quick but i got the gist hahahaha
# the open url open the url gets the html then returns it to test regex then the emmerdale = re.findall finds all links that have emmerdale init
# then you get the url and episode for each one and then you make the emmerdale title urself
# yeah sound, last question mate where it says html = open url so i need put the URL in their?
# yeah mate will do one last thing

