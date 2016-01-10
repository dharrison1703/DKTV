import sys
import os
import json
import urllib
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import load_channels
import hashlib
import re
import random

import server

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
addondir    = xbmc.translatePath( addon.getAddonInfo('profile') )


def getPass_Set():
	randomSets = [1,2,3]
	randomSet = 1 #random.choice(randomSets) # this decides which set below it will use making it like this randomSet = 2 #random.choice(randomSets) so you hash the last bit out and put the number of set you want to try
	if randomSet == 1:
		passSet1 = ['MDA6MUE6Nzg6MDA6MDA6MjU=','MDA6MUE6Nzg6MDA6MDA6NDA=','MDA6MUE6Nzg6MDA6MDA6MDU=','MDA6MUE6Nzg6MTU6MTU6MTU=','MDA6MUE6Nzg6NTU6NTU6MDA=','MDA6MUE6Nzg6MDY6MDY6MDY=','MDA6MUE6Nzg6MTU6MTU6MTU=','MDA6MUE6Nzg6NTU6NTU6MDA=','MDA6MUE6Nzg6MDY6MDY6MDY='] # these macs only work with the url below. aaa i get you now mate
		port_Url = 'aHR0cDovL3BvcnRhbC5pcHR2cHJpdmF0ZXNlcnZlci50dg==' # this in each one is a diff url
		rand_Mac = random.choice(passSet1) # chooses random mac
		setDet = [port_Url,rand_Mac] # puts portal url and choosen mac in list
		print 'mac details 1: '+str(setDet)
		return setDet #returns the list back down to
	
	elif randomSet == 2:
		passSet2 = ['MDA6MUE6Nzg6MTA6MDA6MDY=','MDA6MUE6Nzg6MTA6MDA6NTg=']
		port_Url = 'aHR0cDovL213MS5pcHR2NjYudHY='
		rand_Mac = random.choice(passSet2)
		setDet = [port_Url,rand_Mac]
		print 'mac details 1: '+str(setDet)
		return setDet
	
	elif randomSet == 3:
		passSet3 = ['MDA6MUE6Nzg6MDA6MDA6MDA=','MDA6MUE6Nzg6MDA6MDA6ODU=']
		port_Url = 'aHR0cDovL3BvcnRhbC5pcHR2cm9ja2V0LnR2'
		rand_Mac = random.choice(passSet3)
		setDet = [port_Url,rand_Mac]
		print 'mac details 1: '+str(setDet)
		return setDet
	
	else:pass

def portalConfig(number):
	setDet = getPass_Set() # list returns here
	print str(setDet[0]).decode('base64')
	print str(setDet[1]).decode('base64')
	portal = {};
	
	portal['parental'] = addon.getSetting("parental");
	portal['password'] = addon.getSetting("password");
	
	portal['name'] = 'Premium Portal - [COLORred]If Fail First Click Again[/COLOR]';
	portal['url'] = str(setDet[0]).decode('base64')
	portal['mac'] = str(setDet[1]).decode('base64')
	portal['serial'] = configSerialNumber(number);
	print 'portal info: '+str(portal)
	return portal;


def configMac(number):
	global go;

	custom_mac = ('custom_mac_1');
	portal_mac = ('portal_mac_1');
	
	if custom_mac != 'true':
		portal_mac = (macChoice);
		
	elif not (custom_mac == 'true' and re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", portal_mac.lower()) != None):
		xbmcgui.Dialog().notification(addonname, 'Custom Mac ' + number + ' is Invalid.', xbmcgui.NOTIFICATION_ERROR );
		portal_mac = '';
		go=False;
		
	return portal_mac;

	
	
def configSerialNumber(number):
	global go;
	
	send_serial = addon.getSetting('send_serial_' + number);
	custom_serial = addon.getSetting('custom_serial_' + number);
	serial_number = addon.getSetting('serial_number_' + number);
	device_id = addon.getSetting('device_id_' + number);
	device_id2 = addon.getSetting('device_id2_' + number);
	signature = addon.getSetting('signature_' + number);

	
	if send_serial != 'true':
		return None;
	
	elif send_serial == 'true' and custom_serial == 'false':
		return {'custom' : False};
		
	elif send_serial == 'true' and custom_serial == 'true':
	
		if serial_number == '' or device_id == '' or device_id2 == '' or signature == '':
			xbmcgui.Dialog().notification(addonname, 'Serial information is invalid.', xbmcgui.NOTIFICATION_ERROR );
			go=False;
			return None;
	
		return {'custom' : True, 'sn' : serial_number, 'device_id' : device_id, 'device_id2' : device_id2, 'signature' : signature};
		
	return None;