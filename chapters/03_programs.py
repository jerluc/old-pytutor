# Now that we can comfortably manipulate variables and data, let's talk briefly about how to compose
# a full program from the tools we currently have available.

# Let's say we are trying to build a bill calculator for a restaurant. We might try to start this
# program by defining some of the variables that go into the bill calculation. For example, let's
# quickly jot down the prices of each of the menu items that were ordered, and save them into
# variables for future use:

nachos = 4.50
quesadilla = 4.50
taco = 1.50
burrito = 6.00
horchata = 1.00

# Great! Now that we have the prices for each individual menu item, let's create a new variable to
# hold the subtotal for the bill:

subtotal = (2 * nachos +      # Notice how we broke this one line of code into multiple lines
            1 * quesadilla +  # surrounded by paratheses. Not only is this good practice, but it's
            3 * taco +        # also just a lot easier to read :)
            2 * burrito +
            2 * horchata)

# Okay, now we're getting somewhere! So now that we have our subtotal defined in terms of the item
# prices multiplied by the number of each item that was ordered, let's compute the sales tax:

tax_percentage = 0.0875
tax_amount = subtotal * tax_percentage

# Note that we use a variable to save the tax percentage. This may not be used more than once in the
# first version of this program, but it because we have chosen to save it into a variable, we could
# easily write a new version that makes use of it more than once (e.g. a program that can calculate
# more than one bill).

# So now we have our tax amount saved away, let's compute the receipt total:

total = subtotal + tax_amount

# Simple, right?

# But we wouldn't be very nice people if we didn't leave a tip!

tip_percentage = 0.15  # YMMV (your mileage may vary) :P
tip_amount = total * tip_percentage

# And then of course, the grand total:

grand_total = total + tip_amount

# Finally, to prove to ourselves that our program is atually useful, let's print out each of the
# relevant pieces of data:

print('Subtotal:')
print(subtotal)
print('Tax:')
print(tax_amount)
print('Total:')
print(total)
print('Tip:')
print(tip_amount)
print('Grand total:')
print(grand_total)

# Beautiful! Our program certainly could maybe use some aesthetic modifications to make it more
# user-friendly, but hey at least it gets the answer right!

# So now you have your first complete program! Congrats! If you'd like to make it your own, feel
# free to strip out all of these comments and put the code in a new file to improve upon later. In
# fact, in the next chapter, we'll go through making some minor improvements to this program that
# will make life a little easier for everyone :)
