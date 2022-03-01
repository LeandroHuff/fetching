#!/usr/bin/python

'''
A Python program implementing a URL fetching, a simple URL list fetching.

Works transparently on Posix (Linux, Mac OS X).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''

#######################################
# import libs
#######################################
import os
import requests
import sys
import termios
import atexit
from select import select

#######################################
# websites list
#######################################
website = [ 'http://www.google.com/',
            'http://www.facebook.com/',
            'http://www.yahoo.com/',
            'http://www.mail.com/',
            'http://www.microsoft.com/',
            'http://www.intel.com/',
            'http://www.replit.com/',
            'http://www.github.com/',
            'http://www.atlassian.com/',
            'http://www.bitbucket.com/',
            'http://www.sqlite.org/',
            'http://www.ffmpeg.org/',
            'http://www.cplusplus.com/',
            'http://www.youtube.com/',
            'http://www.tutorialspoint.com/',
            'http://ler.amazon.com.br/',
            'http://cloudconvert.com/',
            'http://www.tiktok.com/',
            'http://web.whatsapp.com/',
            'http://www.nixos.org/',
            'http://www.linkedin.com/',
            'http://www.udemy.com/',
            'http://www.geeksforgeeks.org/',
            'http://www.apinfo.com/',
            'http://www.learncpp.com/',
            'http://www.freecodecamp.org/',
            'http://www.coursera.org/',
            'http://www.microchip.com/',
            'http://www.st.com/',
            'http://www.nxp.com/',
            'http://www.boost.org/',
            'http://www.openssl.org/',
            'http://www.learn-c.org/',
            'http://www.w3schools.com/',
            'http://www.bogotobogo.com/',
            'http://developer-life.webnode.com/'
          ]

#######################################
# class KBHit
'''
A Python class implementing KBHIT, the standard keyboard-interrupt poller.
Works transparently on Posix (Linux, Mac OS X).  Doesn't work with IDLE.
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''
#######################################
class KBHit:

	def __init__(self):
		'''Creates a KBHit object that you can call to do various keyboard things.
		'''
		# Save the terminal settings
		self.fd = sys.stdin.fileno()
		self.new_term = termios.tcgetattr(self.fd)
		self.old_term = termios.tcgetattr(self.fd)

		# New terminal setting unbuffered
		self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
		termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

		# Support normal-terminal reset at exit
		atexit.register(self.set_normal_term)

	def set_normal_term(self):
		''' Resets to normal terminal.  On Windows this is a no-op.
		'''
		termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

	def getch(self):
		''' Returns a keyboard character after kbhit() has been called.
		Should not be called in the same program as getarrow().
		'''
		return sys.stdin.read(1)

	def getarrow(self):
		''' Returns an arrow-key code after kbhit() has been called. Codes are
		0 : up
		1 : right
		2 : down
		3 : left
		Should not be called in the same program as getch().
		'''
		c = sys.stdin.read(3)[2]
		vals = [65, 67, 66, 68]
		return vals.index(ord(c.decode('utf-8')))

	def kbhit(self):
		''' Returns True if keyboard character was hit, False otherwise.
		'''
		dr,dw,de = select([sys.stdin], [], [], 0)
		return dr != []


#######################################
# main()
#######################################
if __name__ == "__main__" :
	kb = KBHit()											#kb is an object from class KBHit
	stop = False											#stop is a running control
	line = 0													#line number to print on console
	print('Program to fetch ' + str(len(website)) + ' URLs from a web site list.')
	print('Starting...')
	while not stop :										#as nike brand, just do it ...
		print('\t\t[Esc] to exit from program')	#message about exit key stroke
		for site in website :							#loop for each line in website list
			if kb.kbhit() :								#check a keyboard hit
				stop = (kb.getch() == chr(27))		#true for Esc key
			if stop :										#if program will stop...
				break											#then stop now!
			line = line + 1								#inc line number to be printed on console
			print('\t' + str(line) + '.\t' + site)	#print site in a formated shape
			try :												#try...
				resp = requests.get(site)				#fetch a URL site from server
			except :											#exception...
				print('Error')								#for any error, print an error message.
	kb.set_normal_term()									#restore terminal console parameters
	print('...Finished!')								#end of program


#######################################

