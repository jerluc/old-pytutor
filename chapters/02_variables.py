# In the previous chapter, we learned how to represent various kinds of data using Python. In this
# chapter, let's discuss how you can store that data in your Python program so that you can reuse it
# later in the same program.

pi = 3.14159

# Above, we can see that we are associating the name `pi` with the float `3.14159`. This is called
# "variable assignment". The "variable name" is the word on the left hand side of the equal sign,
# and the value is the data on the right hand side.

# As you might expect, you can assign any kind of data to a variable:

first_name = 'Jeremy'
last_name = 'Lucas'
age = 28
can_program_in_python = True

# Note that the variable names are all lower case, and instead of using spaces in a name, it uses
# underscores. This is standard practice.

# Variable names can also contain a number, but they can't start with one:

one23 = 123

# Variable names can, however, start with an underscore:

_secret = 'Shhhh don\'t tell anyone!'

# Conventionally, Python variables that start with one or sometimes even two underscores are
# considered "private", though Python itself does not actually enforce this secrecy.

# So now we have a bunch of variables that contain data, and that's all fine and dandy. So what?

# Well, now that we have a name associated with each of these values, we can use them in our
# program!

print(pi)

# Even more, we can use our variables just as we would their underlying values:

print(first_name + last_name)  # Adds the two strings together to form one mega string!

# Wait a second, where did the space go between my first and last name?

print(first_name + ' ' + last_name)  # There we go!

# So we can even mix variables with plain data values as well. This is an important concept: we can
# store the data we need to use repeatedly or at a later time, and use them along with other data
# that we may only need once.

# Now that you've got the hang of storing data in variables, what do you think this will do:

a = 1
b = 2
c = a
a = 3

# Is `a` equal to `1` or `3`? What about `c`?

print(a + b + c)

# Surprised? Well, if you read from the first line of code down to the last line of this code, you
# shouldn't be! Let's take this step-by-step:

a = 1  # a = 1
b = 2  # a = 1, b = 2
c = a  # a = 1, b = 2, c = a = 1
a = 3  # a = 3, b = 2, c = 1

# You see when we do `c = a`, we are assigning the *value of `a`* to the variable `c`. This copies
# the value into `c`. Then in the last statement `a = 3`, we are changing the value of `a`, but this
# does not effect the value of `c`.

# This might make more sense in the context of a more complex assignment:

d = 10
e = 20
f = d * e + 1  # Assign the value of `d` times the value of `e` plus one
d = 1000
e = 2000

print(f)

# In the above example, even though we reassign the values of `d` and `e`, they have no effect on
# the value of `f`, as its value has already been decided by Python on that third line of code, just
# as we saw in the previous example.

# Think you're getting pretty fluent in Python by now? Great! Let's discuss a bit about some of the
# stuff happening behind the scenes with variables.

# So when a program says:

num = 123
print(num)

# How does Python remember the value of `num` between each statement?
#
# The short answer is: Python stores the contents of variables into your computer's memory, called
# "random access memory" or RAM, for short. Besides being the name of a decent-but-not-their-best
# Daft Punk album, your computer's RAM is where temporary information can be stored for use by the
# various pieces of software running on your computer.
#
# Typically, your "operating system" (the mega program that runs all other programs on your
# computer) manages which programs can store and read which information. This way, it's more
# difficult for malicious software to read secret variables in other running programs on your
# computer.
#
# Additionally, RAM is normally *temporary* data storage. This means that when your program stops,
# or when your computer is turned off, the RAM is reset and the information is no longer available.
# We'll discuss in a later chapter how to store data that remains even if your program stops or the
# computer is turned off.

# Well, that's about all about storing data in variables in Python!
