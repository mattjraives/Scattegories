#!/usr/bin/python
import sys,os
from random import choice,sample

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','W']

class game:
	def __init__(self,timer=120,ncat=12,lst="Standard",mem=3):
		self.timer = timer
		self.ncat  = ncat
		self.mem_l = [""]*mem
		self.mem_c = [[]]*mem
		self.ms    = mem
		self.read_list(lst)
	def read_list(self,lst):
		self.list = []
		with open(lst,"r") as l:
			for line in l:
		self.list.append(line.strip())
	def start_round(self):
		loop = True
		cat = [""]*ncat
		for i in range(ncat):
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
		r = round(self.timer,l,c)
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
		while loop:
			self.begin_round()
	
class round:
	def __init__(self,timer,letter,categories):
		self.timer  = timer
		self.letter = letter
		self.categories = categories
	def play(self):
		print self.letter #TODO: in big font
		print "Press <Enter> to begin round"
		delay = raw_input()
		#TODO: timer
		for i in range(len(self.categories)):
			print str(i)+") " + self.categories[i] # TODO: Medium font?
		#TODO: Text flushing (idk what it's called)
