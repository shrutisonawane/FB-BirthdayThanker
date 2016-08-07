#!/usr/bin/env python

#This piece of code should relieve people the tedious task of thanking people on Facebook for wishing them on their birthdays!!

import os
import sys
import urllib
import facebook


def main(argv, req=None):
	print 'Staring the birthday thanker. . .\n\n'
	msg=''
	accessToken = ''
	while (msg=='' and accessToken==''):
		msg = raw_input("Enter your thanking message:")
		accessToken= raw_input("Enter your Facebook access token:")

	try:
		graph = facebook.GraphAPI(access_token=accessToken,version='2.5')
		posts = graph.get_connections(id='me',connection_name='posts')
		
	except:
		print '\nSomething went wrong.. Please check your access token and try again'
		sys.exit(0)

	#Loops through your feed data to determine if anybody has wished you happy birthday!
	for i in range(1,3):
		for p in posts['data']:
			if p.has_key("message"):
				str = p['message']
				if ("Happy Bday" in str) or ("Happy Birthday" in str) or ("Many Many Happy" in str) or ("Happeee bday" in str) or ("happy bday" in str) or ("Happy bday" in str) or ("happy birthday" in str) or ("HAPPY BIRTHDAY" in str) or ("HAPPY BDAY" in str):
					graph.put_like(object_id=p['id'])
					graph.put_comment(object_id=p['id'],message=msg)
				#print p['id'] +": "+p['message']

		#Move to the next page in your FB feed
		nextStr = posts['paging']['next']
		nextIndex = nextStr.find('posts?')
		nextPtr = nextStr[nextIndex:]
		posts = graph.get_connections(id='me',connection_name=nextPtr)
	print '\nThanked everyone for their lovely Birthday wishes on FB! :)\n'
		

if __name__ == '__main__':
    main(sys.argv)

