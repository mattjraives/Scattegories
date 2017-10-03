#!/usr/bin/python
import sys,os,time
from glob import glob
from random import choice,sample

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','W']
rtext = \
'''Round {0}: {1}
===========================
Time Remaining: {2}
===========================
1. {3}
2. {4}
3. {5}
4. {6}
5. {7}
6. {8}
7. {9}
8. {10}
9. {11}
10. {12}
11. {13}
12. {14}'''
ht = "******************************************"


class game:
	def __init__(self,timer=120,ncat=12,mem=3):
		self.timer = timer
		self.ncat  = ncat
		self.mem_l = [""]*mem
		self.mem_c = [[]]*mem
		self.ms    = mem
		self.read_list()
	def read_list(self):
		self.list = []
		categs = glob("Categories/*.txt")
		for lst in categs:
			with open(lst,"r") as l:
				for line in l:
					if line[0] is not "\#" and line.strip():
						self.list.append(line.strip())
	def start_round(self,i):
		loop = True
		cat = [""]*self.ncat
		for i in range(self.ncat):
			j = 0
			loop = True
			while loop:
				c = choice(self.list)
				if c not in cat and c not in sum(self.mem_c):
					cat[i] = c
					loop = False
				else:
					j = j+1
				if j > 100:
					break
		r = round(self.timer,l,c,i)
		r.play()
		self.mem_l = [l] + self.mem_l
		self.mem_l = self.mem_l[:-1]
		self.mem_c = [c] + self.mem_c
		self.mem_c = self.mem_c[:-1]
	def play_game(self):
		print "openScat v 0.1.0"
		print "Press <Enter> to begin game.  Press <p> to pause.  Press <q> to quit."
		#TODO: keypress signals
		delay = raw_input()
		loop = True
		i = 0
		while loop:
			i = i+1
			self.start_round(i)
	
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
		T_0 = time.time
		while time.time - T_0 < timer:
			pass
		print rtext.format(self.n,self.letter,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht,ht)
		print "Time Up!  Press <Enter> to Continue"
		delay = raw_input()
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
