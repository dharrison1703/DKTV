# -*- coding: utf-8 -*-


import re,urlparse,json,urllib
from liveresolver.modules import client,decryptionUtils



def resolve(url):
    try:
        try: referer = urlparse.parse_qs(urlparse.urlparse(url).query)['referer'][0]
        except: referer = url
        try: id = urlparse.parse_qs(urlparse.urlparse(url).query)['id'][0]
    	except: id = re.findall('streamup.com/(.+?)/embed',url)[0]
        url = 'https://streamup.com/%s/embeds/video?startMuted=true'%id
        page = url
        result = client.request(url,referer=referer)
        result = decryptionUtils.doDemystify(result)
        roomSlug = re.findall('"roomSlug":\s*"(.+?)"',result)[0]
        url = re.findall('\$.ajax\(\{\s*url:\s*"(.+?),',result)[0].replace('"','').replace(' ','').replace('window.Room.roomSlug',roomSlug).replace('+','')
        item = re.findall('HlsManifestUrl:\s*response\[\'(.+?)\'\]',result)[0]
        resp = json.loads(client.request(url,referer=referer))[item]
        url = resp + '|%s' % urllib.urlencode({'User-Agent': client.agent(), 'Referer': page,'X-Requested-With':'ShockwaveFlash/20.0.0.286'})
        return url
    except:
        return


