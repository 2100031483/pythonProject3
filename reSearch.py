import re
txt = "Use of Python in Machine Learning"
x = re.search("^Python.*Anaconda$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")