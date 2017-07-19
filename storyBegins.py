import time

#story begins, scene is set
print "It's Friday at 4:48pm, the office is almost empty."
time.sleep(2)
print "You've been checking your watch every minute for the past hour."
time.sleep(2)
print "5 o'clock can't come fast enough."
time.sleep(2)
print "You see your new boss waddling down the hall."
time.sleep(2)
print "Shit. You make eye contact."
time.sleep(2)
print "He calls out, 'What the hell's your name again?'"

#user establishes his/her name
userName = raw_input("> ")
time.sleep(1)
print "'Ah right... %s'" % userName
time.sleep(1)
print "'I'm gonna need you to stay until six tonight.'"
time.sleep(1)

#decision making begins
print "Do you say 'yes' or 'no'?"
workLate = raw_input("> ")

if workLate == "yes":
    execfile('workLateYes.py')
elif workLate == "no":
    execfile('workLateNo.py')
