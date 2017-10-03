#!/usr/bin/python
import sys,os,time
from glob import glob
from random import choice,sample

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','W']
rtext = \
'''Round {}: {}
===========================
1. {}
2. {}
3. {}
4. {}
5. {}
6. {}
7. {}
8. {}
9. {}
10. {}
11. {}
12. {}'''
ttext = "Time Remaining: {}\r"
ht = "******************************************"


class game:
	def __init__(self,timer=120,ncat=12,mem=3):
		self.timer = timer
		self.ncat  = ncat
		self.mem_l = []
		self.mem_c = []
		self.mem    = mem
		self.read_list()
		self.debug = 0
		self.quit_commands = ["q","quit","exit","end"]
	def read_list(self):
		self.list = []
		categs = glob("Categories/*.txt")
		for lst in categs:
			with open(lst,"r") as l:
				for line in l:
					if "#" not in line and line.strip():
						self.list.append(line.strip())
	def start_round(self,rn):
		if self.debug:
			print len(self.mem_l),len(self.mem_c)
		if not self.mem_l:
			self.mem_l = sample(letters,self.mem)
			self.mem_c = sample(self.list,self.mem*self.ncat)
		letter = self.mem_l.pop()
		categories = [self.mem_c.pop() for i in range(self.ncat)]
		if self.debug:
			print letter
			t = "{}\n"*12
			print t.format(*categories)
		else:	
			r = round(self.timer,letter,categories,rn)
			r.play()
	def play_game(self):
		os.system("clear")
		print "openScat v 0.1.0"
		print "Press <Enter> to begin game.  Press <p> to pause.  Press <q> to quit. Type 'debug' to",
		print " enter debug mode"
		#TODO: keypress signals
		delay = raw_input()
		if delay.lower()=="debug":
			self.debug = 1
		loop = True
		i = 0
		while loop:
			i = i+1
			self.start_round(i)
			delay = raw_input()
			if delay.lower() in self.quit_commands:
				sys.exit()
	
class round:
	def __init__(self,timer,letter,categories,i):
		self.timer  = timer
		self.letter = letter
		self.categories = categories
		self.n = i
	def play(self):
		os.system("clear")
		print rtext.format(self.n,self.letter,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht)
		delay = raw_input()
		os.system("clear")
		print rtext.format(self.n,self.letter,*self.categories)
		print " "
		print ttext.format(self.timer),
		T_0 = time.time()
		while time.time() - T_0 < self.timer:
			print ttext.format(str(int(self.timer + T_0 - time.time()))+"    "),
		print " "
		os.system("clear")
		print rtext.format(self.n,self.letter,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht)
		print "Time Up!  Press <Enter> to Continue"
		delay = raw_input()
		os.system("clear")
		print rtext.format(self.n,self.letter,*self.categories)
		print "Press <Enter> to continue to next round"
		#print self.letter #TODO: in big font
		#print "Press <Enter> to begin round"
		#delay = raw_input()
		##TODO: timer
		#for i in range(len(self.categories)):
		#	print str(i)+") " + self.categories[i] # TODO: Medium font?
		##TODO: Text flushing (idk what it's called)

if __name__=="__main__":
	Game = game()
	Game.play_game()
