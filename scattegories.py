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
		self.mem_l = [""]*mem
		self.mem_c = [[]]*mem
		self.ms    = mem
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
		loop = True
		cat = [""]*self.ncat
		for i in range(self.ncat):
			if self.debug:
				print i,
			j = 0
			loop = True
			while loop:
				c = choice(self.list)
				if c not in cat and c not in [[]+m for m in self.mem_c]:
					cat[i] = c
					loop = False
				else:
					if self.debug:
						print "!"
					j = j+1
				if j > 100:
					break
		if self.debug:
			print j,
		loop = True
		while loop:
			l = choice(letters)
			if l not in self.mem_l:
				loop = False
		if self.debug:
			print l
			t = "{}\n"*12
			print t.format(*cat)
		else:	
			r = round(self.timer,l,cat,rn)
			r.play()
			self.mem_l = [l] + self.mem_l
			self.mem_l = self.mem_l[:-1]
			self.mem_c = cat + self.mem_c
			self.mem_c = self.mem_c[:-1]
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
			print ttext.format(int(self.timer + T_0 - time.time())),
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
