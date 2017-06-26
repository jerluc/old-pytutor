# Before we talk about representing data in Python, we'll need a way to actually show what's going
# on with our program. There's an age-old saying:
#
#     "A program that has no output is not a very useful program."
#
#                                                      - Anonymous
#
# So to make sure we create useful programs, we'll need to first introduce a way to print something
# to your screen in your terminal:

print(123)

# This is the print function, and as you might have guessed, it prints to your terminal whatever you
# put inside of the paratheses. We'll go more in-depth into what functions are and even how to
# create your own functions in a later chapter.
#
# So now that we know how to print things to the screen, let's talk about what was printed in this
# first example.
#
# What kind of information is 123? In Python, we would call this an "integer" (or "int" for short).
# An integer is basically a whole number and is written just the same as you would in any math class
# in the world.
#
# What kind of information could you represent with an integer?
#
# Maybe the number of floors in a building? For example, my apartment has this many floors:

print(4)

# How about one's age? For example, I am this many years old:

print(28)

# What about a phone number? For example, my totally real phone number:

print(555-555-5555)

# Wait a second, that's not right...My phone number is 555-555-5555, not -5555. So why did it print
# out -5555?
#
# Well, as it turns out, Python integers can do lots of integery things. For example, you can add
# them:

print(1 + 2)

# Or subtract them

print(2 - 1)

# Or multiply them (with the `*`)

print(4 * 2)

# Or divide them (with the `/`)

print(49 / 7)

# So then why didn't the phone number print out properly? It's because Python saw the phone number
# 555-555-5555 and evaluated this as an integery math equation:
#
#     555 - 555 - 5555 =
#     0         - 5555 =
#                      = -5555
#
# Makes sense now, right? As a rule of thumb, use an integer to represent numeric information only
# when it would be appropriate to do some kind of math with that information. So just as you
# wouldn't add two phone numbers together, nor would you subtract zip codes, nor multiply street
# numbers, etc.
#
# But this leaves the question: how do we represent these kinds of information in Python?

print('555-555-5555')

# Aha! There we go! Now we're talking! So to represent a phone number literally as 555-555-5555, we
# need to put quotes around it. But what kind of data is this? In Python, this is called a "string",
# and is generally used to represent any kind of textual information. Note that similar to Python
# comments, Python doesn't try to evaluate the information in the string at all:

print('1 + 2')

# In fact, the triple quotes we saw in the previous chapter is really just a way to write out a
# multi-line string:

print('''Look ma
I
can
fly!''')

# So what kinds of information would you want to represent using a string?
#
# How about a name? For example, my name is:

print('Jeremy Lucas')

# Maybe a street address? For example, my totally real street address:

print('1234 Place St, Apt. #3')

# This is all fine dandy, but what if my data has a single quote in it? For example, if you wanted
# to say "I am 6'0" tall".
#
# Well, in order to use that single quote in the middle of the string, we need to "escape" it by
# putting a `\` just before the single quote:

print('I am 6\'0" tall')

# The `\` tells Python "Hey it's fine, that quote is with me" so that it won't touch your quotes.
#
# So now that we have strings, what else can we do with them?
#
# Well, you can add them together! For example:

print('Hey' + 'There!')

# As you can see, when you add two strings together, Python just cobbles them together into one
# bigger string!
#
# That's not all you can do with a string (we'll discuss more things you can do with strings later).
#
# So what other kinds of information can we represent in Python? Well, in most programs it is
# important to be able to represent various kinds of yes or no decisions called "branches", like the
# branches of a tree. These yes or no decisions are encoded as:

print(True)

# For yes, and:

print(False)

# For no.
#
# Note that both `True` and `False` are capitalized, as this is mandatory for Python to understand
# what you mean.
#
# In a later chapter, we'll discuss how these true or false values, called "boolean" values, can be
# used for our programs.
#
# The last kind of data we'll introduce here is a way to represent non-whole numbers:

print(3.14159)

# These non-whole numbers, called "floats" in Python, allow us to represent decimals with variable
# precision. Using these floats, we can do all the usual mathematical operations:

print(0.5 * 0.5)

print(10.0 / 2.0)

print(1.5 - 4.5)

print(0.25 + 0.75)

print(0.5 * 10)

# Notice what happened in that last example? We actually multiplied the float `0.5` with the integer
# `10`, which produced the float `5.0`. Python decided that since we are doing arithmetic between a
# float and an integer, it should "coerce" the integer into a float. This is an incredibly
# convenient thing, as otherwise these two kinds of data wouldn't be able to interact.
#
# Throughout the remaining chapters, we'll encounter other points of coercion or even times when
# Python needs some help coercing.
#
# Well that's it for this chapter! Congrats on learning how to represent data in Python!
