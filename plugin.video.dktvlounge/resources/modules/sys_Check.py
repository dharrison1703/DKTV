import os.path, binascii, base64, re, urllib2, xbmc, modules, xbmcgui, shutil
path_Addon = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.entertainmentlounge'))
path_Repo = xbmc.translatePath(os.path.join('special://home/addons/repository.ChameleonEntertainment'))
file_Check = os.path
Decode = base64.decodestring

def system_Check(sys_Password, sys_Passcode):
	auth_URL = Decode('aHR0cDovL2RldmlsNjY2d2l6YXJkLngxMGhvc3QuY29tL2FkZG9uL1NlY3VyaXR5L3NlY3VyaXR5LnBocD8=')+'passcode='+sys_Passcode+'&password='+sys_Password
	print auth_URL
	finalise_Sum = open_URL(auth_URL)
	auth_Result = re.compile(Decode('PGgxPiguKz8pPC9oMT48aDI+KC4rPyk8L2gyPjxoMz4oLis/KTwvaDM+PGg0PiguKz8pPC9oND4='),re.DOTALL).findall(finalise_Sum)
	print str(auth_Result)
	for msg, sum, follow, status in auth_Result: 
		print 'SUM: ' + str(sum)
		if follow == 'True':
			test_Sum = int(sum) / 6
			if str(test_Sum) == Decode('MTQ0NTM='):
				if status == 'online':
					return True
				elif status == 'offline':
					return False
				else: pass
			else: clean_UP()
		else: clean_UP()
	
def failed_Verification():
	dialog = xbmcgui.Dialog()
	dialog.ok("Failed Verification", "We couldnt verify your system please check back later!")

def clean_UP():
	dialog = xbmcgui.Dialog()
	dialog.ok("Authorisation Failed", "This Add-On is for private use only sorry!")
	#shutil.rmtree(path_Addon, ignore_errors=True)
	#shutil.rmtree(path_Repo, ignore_errors=True)
	
def down_Maintenance(sys_Password):
	auth_URL = 'urlhere'+'password='+sys_Password
	status = open_URL(auth_URL)
	Decode = base64.decodestring
	status_Result = eval(Decode("cmUuY29tcGlsZShEZWNvZGUoJ1BHZzBQaWd1S3o4cFBDOW9ORDQ9JykscmUuRE9UQUxMKS5maW5kYWxsKHN0YXR1cyk="))
	for status in status_Result: 
		if status == 'online':
			return True
		elif status == 'offline':
			return False
		else: pass

def maintenance_Popup():
	dialog = xbmcgui.Dialog()
	dialog.ok("Routine Maintenance", "Currently Down For Routine Maintenance.\nCheck Back Soon.")

def no_Sys_Password():
	dialog = xbmcgui.Dialog()
	dialog.ok("System Password Not Found", "Sorry We Couldnt Detect A Password\nPassword Can Be Found In The Group")

def no_Sys_Passcode():
	dialog = xbmcgui.Dialog()
	dialog.ok("System Passcode Not Found", "Sorry We Couldnt Detect A Passcode\nPasscode Can Be Found In The Group")

def incorrect_System():
	dialog = xbmcgui.Dialog()
	dialog.ok("Incorrect Build", "Looks Like This May Not Be The Devils Build!")

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def open_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link