# -*- coding: utf-8 -*-

import re,sys,urllib,urlparse,base64,urllib2
import client
from resources.modules import cloudflare


def resolvezero(url):
    try:
        try: referer = urlparse.parse_qs(urlparse.urlparse(url).query)['referer'][0]
        except: referer = url

        page = urlparse.parse_qs(urlparse.urlparse(url).query)['a'][0]
        page = 'http://zerocast.tv/embed.php?a=%s&id=&width=640&height=480&autostart=true&strech=exactfit' % page
        result = client.request(page, referer=referer)
        result = client.request(page, referer=referer, close=False)
        result = re.compile("file: unescape\('(.+?)'\)").findall(result)[0]
        result= urllib.unquote(result).decode('utf8')
        if result.startswith('rtmp'):
            return '%s pageUrl=%s live=1 timeout=20' % (result, page)
        elif '.m3u8' in result:
            chunk = client.request(result)
            chunk = re.compile('(chunklist_.+)').findall(chunk)[0]
            return result.split('.m3u8')[0].rsplit('/', 1)[0] + '/' + chunk

    except:
        return

def resolvemi(url):
    try:
        try:
            referer = urlparse.parse_qs(urlparse.urlparse(url).query)['referer'][0]
        except:
            referer=url
            
        id = urlparse.parse_qs(urlparse.urlparse(url).query)['id'][0]
        url = 'http://miplayer.net/embedplayer.php?width=640&height=480&id=%s'%id
        result = client.request(url, referer=referer)
        curl = re.compile("curl\s*=\s*\"(.+?)\"").findall(result)[0]
        curl = base64.b64decode(curl)
        
        url = curl + ' swfUrl=http://otronivel.me/jw7/jwplayer.flash.swf flashver=WIN/2019,0,0,226 timeout=15 live=true swfVfy=1 pageUrl=http://miplayer.net/embedplayer.php?width=640&height=480&id=%s&autoplay=true&strech=exactfit'%id
        return url
    except:
      return

def resolves43(url):

    try:
        result = cloudflare.request(url)
        items = client.parseDOM(result, 'video', attrs={'id': 'live_player'})
        url = client.parseDOM(items, 'source', ret='src')[0]
        if ('http') in url: return url+'|User-Agent=Mozilla/5.0'
    except:
        return None
