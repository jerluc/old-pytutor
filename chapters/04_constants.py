# In the last section, we wrote our first full program that calculates a bill with tip for a
# restaurant. In this section, we're going to look into how we might improve the organization and
# reusability of our program by using an old trick to store our data.

# Let's take a look at a bit of code we wrote in the previous section:

tax_percentage = 0.0875

# Now let's compare that to the following code:

TAX_PERCENTAGE = 0.0875  # Can you spot the difference? :P

# So why would we suddenly DECIDE TO START WRITING OUR VARIABLE NAMES IN ALL CAPS? Well, in its
# typical usage in Python, when we define a variable named with all capital letters, we are
# communicating that we wish for the variable to be considered a "constant"--that is, a named value
# whose data is not intended to change.

# Take for example a few other common constants:

PI = 3.14159  # Hopefully this never changes! (Otherwise we'd all be going in circles!)
BOILING_TEMP_C = 100
OZ_PER_TSPN = 0.1667
SHOULD_INCLUDE_TIP = True  # Also hopefully always true!

# And so on...

# Another common practice that will save you plenty of headaches as we write more complex programs
# is to try to organize your constants near or at the top of your program. This will allow us to
# very easily reconfigure our program by modifying the constants at the top, without needing to
# dive into the gory details of the program below them!

# In a lot of ways, these constants define the sort of assumptions the program is making about its
# surrounding "environment". For example, using the BOILING_TEMP_C constant above, we could see what
# other-worldly effects changing the boiling temperature of water would have on the universe, simply
# by altering the value stored in the constant at the top of a file.

# Or, as another example, we could use a boolean constant, such as SHOULD_INCLUDE_TIP, to
# potentially modify the *behavior* of our program, as we'll see in a later chapter.

# Well, that's all for this chapter! Remember:

CHANGE = 'the only constant'
