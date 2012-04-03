import random
import math

# The network, each of which has two available spaces
network=['Zeus','Athena','Hercules','Bacchus','Pluto']

# People, along with their first and second choices
prefs=[('Toby', ('Bacchus', 'Hercules')),
       ('Steve', ('Zeus', 'Pluto')),
       ('Karen', ('Athena', 'Zeus')),
       ('Sarah', ('Zeus', 'Pluto')),
       ('Dave', ('Athena', 'Bacchus')), 
       ('Jeff', ('Hercules', 'Pluto')), 
       ('Fred', ('Pluto', 'Athena')), 
       ('Suzie', ('Bacchus', 'Hercules')), 
       ('Laura', ('Bacchus', 'Hercules')), 
       ('James', ('Hercules', 'Athena'))]

 
# Each person is assigned to one open slot and the domain becomes:
# [(0,9),(0,8),(0,7),(0,6),...,(0,0)]
domain=[(0,(len(dorms)*2)-i-1) for i in range(0,len(dorms)*2)]

# Loop through the slots, and every solution.
def printsolution(vec):
  slots=[]
  # Create two slots for each network
  for i in range(len(network)): slots+=[i,i]

  # Loop over each person’s space
  for i in range(len(vec)):
    x=int(vec[i])

    # Choose the slot from the remaining ones
    network=networks[slots[x]]
    # Show the person and assigned space
    print prefs[i][0],space
    # Remove this slot
    del slots[x]

# Slots are removed as they are used up, the cost is calculated by
# comparing person's current assignment to its top choices.
# Increase cost by:
# 0 if the top choice
# 1 if second choice
# 3 if neither of the two top choices
def networkcost(vec):
  cost=0
  # Create list a of slots
  slots=[0,0,1,1,2,2,3,3,4,4]

  # Loop over each person
  for i in range(len(vec)):
    x=int(vec[i])
    network=networks[slots[x]]
    pref=prefs[i][1]
    # First choice costs 0, second choice costs 1
    if pref[0]==network: cost+=0
    elif pref[1]==network: cost+=1
    else: cost+=3
    # Not on the list costs 3

    # Remove selected slot
    del slots[x]
    
  return cost
# A module that implements optimization. From the provided data.
# This is an implementation that visualizes a Network
from PIL import Image,ImageDraw

people=['Charlie','Augustus','Veruca','Violet','Mike','Joe','Willy','Miranda']

links=[('Augustus', 'Willy'), 
       ('Mike', 'Joe'), 
       ('Miranda', 'Mike'), 
       ('Violet', 'Augustus'), 
       ('Miranda', 'Willy'), 
       ('Charlie', 'Mike'), 
       ('Veruca', 'Joe'), 
       ('Miranda', 'Augustus'), 
       ('Willy', 'Augustus'), 
       ('Joe', 'Charlie'), 
       ('Veruca', 'Augustus'), 
       ('Miranda', 'Joe')]

# Loops through all pairs of links and uses the current
# coordinates of their endpoints to determine whether they cross.
def crosscount(v):
  # Convert the number list into a dictionary of person:(x,y)
  loc=dict([(people[i],(v[i*2],v[i*2+1])) for i in range(0,len(people))])
  total=0
  
  # Loop through every pair of links
  for i in range(len(links)):
    for j in range(i+1,len(links)):

      # Get the locations 
      (x1,y1),(x2,y2)=loc[links[i][0]],loc[links[i][1]]
      (x3,y3),(x4,y4)=loc[links[j][0]],loc[links[j][1]]
      
      den=(y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)

      # den==0 if the lines are parallel
      if den==0: continue

      # Otherwise ua and ub are the fraction of the
      # line where they cross
      ua=((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/den
      ub=((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3))/den
      
      # If the fraction is between 0 and 1 for both lines
      # then they cross each other
      if ua>0 and ua<1 and ub>0 and ub<1:
        total+=1

      # A way to penalize a solution that has two nodes too close together
      # Calculate the distance and divide with desired distance.
    for i in range(len(people)):
      for j in range(i+1,len(people)):
        # Get the locations of the two nodes
        (x1,y1),(x2,y2)=loc[people[i]],loc[people[j]]

        # Find the distance between them
        dist=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        # Penalize any nodes closer than 50 pixels
        if dist<50:
          total+=(1.0-(dist/50.0))
  return total

# Draws the Network
def drawnetwork(sol):
  # Create the image
  img=Image.new('RGB',(400,400),(255,255,255))
  draw=ImageDraw.Draw(img)

  # Create the position dict
  pos=dict([(people[i],(sol[i*2],sol[i*2+1])) for i in range(0,len(people))])

  for (a,b) in links:
    draw.line((pos[a],pos[b]),fill=(255,0,0))

  for n,p in pos.items():
    draw.text(p,n,(0,0,0))

  img.show()

domain=[(10,370)]*(len(people)*2)
 import dorm
dorm.printsolution([0,0,0,0,0,0,0,0,0,0])
Toby Zeus
Steve Zeus
Karen Athena
Sarah Athena
Dave Hercules
Jeff Hercules
Fred Bacchus
Suzie Bacchus
Laura Pluto
James Pluto

reload(dorm)
<module 'dorm' from 'dorm.py'>
import optimization
s=optimization.randomoptimize(dorm.domain,dorm.dormcost)
 dorm.dormcost(s)
18
 dorm.printsolution(s)
Toby Bacchus
Steve Zeus
Karen Zeus
Sarah Athena
Dave Pluto
Jeff Athena
Fred Bacchus
Suzie Hercules
Laura Hercules
James Pluto

 s=optimization.annealingoptimize(dorm.domain,dorm.dormcost)
>>> dorm.printsolution(s)
Toby Bacchus
Steve Zeus
Karen Athena
Sarah Pluto
Dave Bacchus
Jeff Hercules
Fred Pluto
Suzie Zeus
Laura Hercules
James Athena

>>> import socialnetwork
>>> import optimization
>>> s=optimization.randomoptimize(socialnetwork.domain,socialnetwork.crosscount)
>>> socialnetwork.crosscount(s)
3
>>> s=optimization.annealingoptimize(socialnetwork.domain,
... socialnetwork.crosscount,step=50,cool=0.99)
>>> socialnetwork.crosscount(s)
2
>>> s[196.0, 214, 12.0, 361, 247, 67, 163, 10, 72, 330.0, 298, 44, 220.0, 131, 238, 274.0]

>>> reload(socialnetwork)
<module 'socialnetwork' from 'socialnetwork.py'>
>>> s=optimization.annealingoptimize(socialnetwork.domain,
... socialnetwork.crosscount,step=50,cool=0.99)
>>> socialnetwork.drawnetwork(s) // The image is saved as network1.jpg

>>> import socialnetwork
>>> import optimization
>>> s=optimization.annealingoptimize(socialnetwork.domain,
... socialnetwork.crosscount,step=50,cool=0.99)
>>> socialnetwork.crosscount(s)
5
>>> socialnetwork.drawnetwork(
