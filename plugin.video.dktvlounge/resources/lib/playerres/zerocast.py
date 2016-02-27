# -*- coding: utf-8 -*-
import re,urlparse,base64,urllib
import client


domains = ['zerocast.tv']


def resolve(url):
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


