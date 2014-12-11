my_name = 'Jon Doe'
my_age = 150
my_height = 72
my_weight = 185
my_eyes = 'Blue'
my_teeth = 'yellow and falling out'
my_hair = 'brown, but has fallen out'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d poinds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s, depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right.
print "If i add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, (my_age + my_height + my_weight))
