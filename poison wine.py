"""You have 1000 bottles of wine, and exactly one bottle is poisoned. You need
to find the poisoned wine before your party starts in an hour. You have 10 rats
to test on to the find out which bottle is deadly. The poison takes effect after
an hour of consumption, so you only have one chance to run your rat poison
experiment , meaning you can't feed some rats wine and wait for an hour before
feeding them more wine. Assume each rat can drink as much wine as you feed it.
How do you find the poisoned wine?"""

# do it using bits 10 rats = 2^10 = 1024 combinations

import math

# Function to find the
# minimum number of rats
def minRats(n):

	return math.ceil(math.log2(n));


# Number of bottles
n = 1000;
print("Minimum ", end = "")
print(minRats(n), end = " ")
print("rat(s) are required")
