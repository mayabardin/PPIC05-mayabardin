#!/usr/bin/env python3
#
# pp. 163, 165, 166
#
#float is how we compare decimals
"""
5.1 Write a program to read the 'rainfall.txt' file and the write out a 
new file called 'rainfallfmt.txt'. The new file should format each 
line so that the city is right-justifiled in a field that is 25 
characters wide, and the rainfall data should be printed in a a field 
that is 5 characters wide with 1 digit to the right of the decimal 
point.
"""
data_file = open('rainfall', 'r') #'r' means "read"
data_filefmt = open('rainfallfmt', 'w') #'r' means "read"
for aline in data_file:
	row = aline.strip().split()
	line_str = '%25s %5.1f' % (row[0], float(row[1]))
	data_filefmt.write(line_str)
	data_filefmt.write('/n')

data_file.close()
data_filefmt.close()

	
	#print('%-25s %5.1f' % (row[0], float(row[1])) )

"""
5.2 Write a function that writes a temperature coversion table called 
'tempcov.txt'. The table should include temperatures from -300 to 212 
degrees Fahrenheit and their Celcius equivalents, presented in two 
columns with appropriate headings. Each collumn should be 10 
characters wide, and each temperature should have 3 digits to the 
right of the decimal point.
"""
def func():
	maya = open('degreestocelcius', 'w')
	f = -301
	for x in range(513):
	    f = f + 1 
	    c = (f - 32)*(5/9)
	    temps = '%s %10.3f' % (f, c)
	    maya.write(temps)
	    maya.write('\n')

func()
#myfile.close()

"""
5.3 Open a file during a Python session. Call the 'readline' method twice 
on that file, then call the 'readlines' method. What lines does the 
list reurned by 'readlines' include?
"""

#at first it printed -300   -184.444 but the second time it returns an empty list

"""
5.4 Open the file in Exercise 5.3 again, but call 'readlines' 
immediately. Compare the lines returned in this excercise with the 
previous one.
"""

#it printed another empty list like it did the second time i entered maya.readline()

"""
5.5 Write a program that reads in the contents of a file and writes a new 
file where all the characters are in uppercase.
"""
data_newfile = open('loudcupcakes.txt', 'w')
data_file = open('CupcakeIpsum', 'r')
for aline in data_file:
	row = aline.upper()

	print(row)
#myfile.close()

"""
5.6 Write a program that reads in a file and then prints out the number 
of lines, words, and characters in the file.
"""
myfile = open('CupcakeIpsum', 'r')
num_lines = 0 
num_words = 0
num_letters = 0
for line in myfile:
	lines = 1



	
	print(line.split())



myfile.close()

"""
5.7 Write a program that creates a file with a concordance - an index 
that tells you the line of the file wach word appears on. If a word 
is on more tha one line, the concordance will show you all of the 
lines containing that word. Hint: Use a dictionary keyed by each word 
to solve this problem.
"""








