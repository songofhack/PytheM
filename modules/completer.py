import sys
from subprocess import *
import time
import readline

class Completer:

        def __init__(self,console):
		tab = readline.parse_and_bind("tab: complete")
		if console == "pythem":
			completer = readline.set_completer(self.pythem)

	def suboption(self, text, state):
		#print text
		#print state
		results = [x for x in self.suboptions if x.startswith(text)] + [None]
		return results[state]

        def pythem(self, text, state):
		#print text
		#print state
		if "set" in text and state == 1:
			self.suboptions = ['interface','arpmode','target','gateway','file','domain','port','script','redirect']
			completer = readline.set_completer(self.suboption)

		elif "jarvis" in text and state == 1:
			self.suboptions = ['help','log','say','read']
			completer = readline.set_completer(self.suboption)

		elif "print" in text and state == 1:
			self.suboptions = ['interface', 'arpmode', 'target', 'gateway','file']
			completer = readline.set_completer(self.suboption)

		elif "scan" in text and state == 1:
			self.suboptions = ['tcp','arp','manual']
			completer = readline.set_completer(self.suboption)

		elif "arpspoof" in text and state == 1:
			self.suboptions = ['start', 'stop']
			completer = readline.set_completer(self.suboption)

		elif "dnsspoof" in text and state == 1:
			self.suboptions = ['start','stop']
			completer = readline.set_completer(self.suboption)

		elif "inject" in text and state == 1:
			self.suboptions = ['start','stop']
			completer = readline.set_completer(self.suboption)

		elif "xploit" in text and state == 1:
			self.suboptions = ['stdin', 'tcp']
			completer = readline.set_completer(self.suboption)

		elif "brute-force" in text and state == 1:
			self.suboptions = ['ssh','url','form']
			completer = readline.set_completer(self.suboption)
		else:
	        	self.words = ['clear','help','exit','quit','set','print','scan','arpspoof','dnsspoof','inject','sniff','pforensic','xploit','brute','geoip','decode','encode','cookiedecode','jarvis']
			results = [x for x in self.words if x.startswith(text)] + [None]
			return results[state]



