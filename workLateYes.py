print "'Great, I'm heading out early. See you Monday'"
time.sleep(1)
print "You jerk around for another hour and pretend to be busy."
time.sleep(2)
print "It's now 6:00pm. Do you go 'home' or go to a 'bar'?"
destination = raw_input("> ")
if destination == "home":
    print "Bic."
elif destination == "bar":
    print "Do you head to Dooley's Irish 'Pub' or The Envoy 'Hotel'?"
    bar = raw_input("> ")
    if bar == "Pub":
        print "It's 6:14p and you've just arrived. You can tell that the crowd has been here a while."
    elif bar == "Hotel":
        print "You arrive at 6:23p and glance around, silently judging all the pricks in their tailored suits."
