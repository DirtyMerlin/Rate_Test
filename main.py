print """
##################################
 @  The Rateogram                @
 @                               @
 @ By:                           @
 @   Dirty Dan                   @
##################################"""
def gui ():
    print """
      Who are you going to rate?
      1)Chick
      2)Dick
      """
    selection= raw_input("Please select a number ---->")
    if selection == '1':
        chicks()
    elif selection == '2':
        dudes()
    else:
        print "YEET. Try again"
        gui()
def chicks():
    print " Please rate the following parts of the subject on a scale of 1-10"
    legs= raw_input("Legs:")
    ass= raw_input("Ass:")
    boobs= raw_input("Boobs:")
    personality= raw_input("Personality:")
    face= raw_input("Face:")
    legs= int(legs)*2
    ass= int(ass)*4
    
    #giving some space
    body= int(legs)+ int(ass) + int(boobs)
    
    total= int(body) + int(face) + int(personality)
    final = float(total)/90.0 *10.0
    
    print "Your chick of choice is a", final, "."
   
def finished():
   print "Would you like to continue?"
   a= raw_input("Y/N:")
   if a.lowercase == y:
    gui()
   else:
    terminate()
 def terminate():
  i=3
  while i >1:
    print "Terminating in %s seconds" %(i)
    time.sleep(1)
  if i == 1:
    print "Terminating in 1 second"
    time.sleep(1)   
  exit 
gui()
    
