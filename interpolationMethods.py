# interpolationMethods.py
# 
# Contains methods for interpolation, specifically Newton's Forward Divided Differences and the Natural Cubic Spline
# REQUIREMENTS: colorama
#
# Note: When a "y-value" array is fed into the natural cubic splines function (and possibly the others), the array is modified and comes back
#       without it's last element. I'm not sure why exactly, though I suspect it's because I don't clone the arrays, and yet use the equivalent
#       of y_array.pop() to remove an extra element from the end.

import platform
import os
import sys
import math


def forwardDivDiff(xVals, yVals):
	xVals = xVals.copy()
	yVals = yVals.copy()
	n = len(xVals) - 1
	F = []
	for i in range(n + 1):
		F.append([yVals[i]])
		for j in range(i):
			F[i].append(0)
	for i in range(1, n + 1):
		for j in range(1, i+1):
			F[i][j] = (F[i][j-1] - F[i - 1][j - 1])/(xVals[i]-xVals[i-j])
	coeff = []
	for x in F:
		coeff.append(x[-1])
	return coeff, xVals

def natCubicSpline(xVals, a):
	xVals = [i for i in xVals]
	a = [i for i in a]
	n = len(xVals) - 1
	h = []
	alpha = [0] * n
	l = []
	mu = []
	z = []
	b = [0] * n
	c = [0] * (n+1)
	d = [0] * n
	# initializes h array
	for i in range(n):
		h.append(xVals[i+1] - xVals[i])
	
	for i in range(1, n):
		alpha[i] = (3/h[i]) * (a[i+1] - a[i]) - (3/h[i-1]) * (a[i] - a[i-1])
	l.append(1)
	mu.append(0)
	z.append(0)
	
	for i in range(1, n):
		l.append(2 * (xVals[i+1] - xVals[i-1]) - h[i-1] * mu[i-1])
		mu.append(h[i]/l[i])
		z.append((alpha[i] - h[i-1] * z[i-1])/l[i])
	
	l.append(1)
	z.append(0)
	c[n] = 0
	for j in range(n-1, -1, -1):
		c[j] = z[j] - mu[j] * c[j+1]
		b[j] = (a[j+1] - a[j])/h[j] - (h[j]/3)*(c[j+1] + 2*c[j])
		d[j] = (c[j+1] - c[j])/(3 * h[j])
	# had a and c returning too many values, though I think the extra values are necessary to compute everything else
	a.pop()
	c.pop()
	return [a, b, c, d], xVals
	
def clampCubicSpline(xVals, a, fPrimeX0, fPrimeXn):
	n = len(xVals) - 1
	h = []
	alpha = [0] * (n + 1)
	l = []
	mu = []
	z = []
	b = [0] * n
	c = [0] * (n+1)
	d = [0] * n
	# initializes h array
	for i in range(n):
		h.append(xVals[i+1] - xVals[i])
	#print(f"len(alpha): {len(alpha)}")
	#print(f"len(h): {len(h)}")
	#print(f"n: {n}")
	alpha[0] = 3 * (a[1] - a[0])/h[0] - 3 * fPrimeX0
	alpha[n] = 3 * fPrimeXn - 3 * (a[n] - a[n-1])/h[n-1]
	for i in range(1, n):
		alpha[i] = (3/h[i]) * (a[i+1] - a[i]) - (3/h[i-1]) * (a[i] - a[i-1])
	l.append(2*h[0])
	mu.append(0.5)
	z.append(alpha[0]/l[0])

	for i in range(1, n):
		l.append(2 * (xVals[i+1] - xVals[i-1]) - h[i-1] * mu[i-1])
		mu.append(h[i]/l[i])
		z.append((alpha[i] - h[i-1] * z[i-1])/l[i])
	
	l.append(h[n-1]*(2 - mu[n-1]))
	z.append((alpha[n] - h[n-1] * z[n-1])/l[n])
	c[n] = z[n]
	for j in range(n-1, -1, -1):
		c[j] = z[j] - mu[j] * c[j+1]
		b[j] = (a[j+1] - a[j])/h[j] - (h[j]/3)*(c[j+1] + 2*c[j])
		d[j] = (c[j+1] - c[j])/(3 * h[j])
	# had a and c returning too many values, though I think the extra values are necessary to compute everything else
	a.pop()
	c.pop()
	return [a, b, c, d], xVals
	
def divDiffPoly(coeffAndXVals, x):
	coeff, xVals = coeffAndXVals
	sum = 0
	for i in range(len(coeff)):
		term = coeff[i]
		for j in range(i):
			term *= x - xVals[j]
		sum += term
	return sum
	
def printDivDiffPoly(coeffAndXVals):
	coeff, xVals = coeffAndXVals
	for i in range(len(coeff)):
		term = f"{coeff[i]}"
		for j in range(i):
			term += f"  + (x - {xVals[j]})"
		print(f"{term}", end="")
	print("")

def cubicSplinePoly(abcdArrayAndXVals, x):
	abcdArray, xVals = abcdArrayAndXVals
	a, b, c, d = abcdArray
	i = -1
	for iter in range(len(xVals)-1):
		if xVals[iter] <= x <= xVals[iter + 1]:
			i = iter
			break
	if i == -1:
		return "The value given is out of the splines' range."
	x -= xVals[iter]
	return a[iter] + b[iter] * x + c[iter] * x**2 + d[iter] * x**3

def printCubicSplinePoly(abcdArrayAndXVals):
	abcd, xVals = abcdArrayAndXVals
	for splineNum in range(len(abcd[0])):
		spline = [abcd[i][splineNum] for i in range(4)]
		print(f"Spline {splineNum + 1}: ", end="")
		for i in range(len(spline)):
				print(f"{spline[i]}", end="")
				for j in range(i):
					print(f"(x-{xVals[splineNum]})", end="")
				if i + 1 == len(spline ):
					print("")
				else:
					print(" + ", end="")

def cubicSplinePolyDeriv(abcdArrayAndXVals, x):
	abcdArray, xVals = abcdArrayAndXVals
	a, b, c, d = abcdArray
	i = -1
	for iter in range(len(xVals)-1):
		if xVals[iter] <= x <= xVals[iter + 1]:
			i = iter
			break
	if i == -1:
		return "The value given is out of the splines' derivatives' range."
	x -= xVals[iter]
	return b[iter] + 2 * c[iter] * x + 3 * d[iter] * x**2

def printCubicSplinePolyDeriv(abcdArrayAndXVals):
	abcd, xVals = abcdArrayAndXVals
	for splineNum in range(len(abcd[0])):
		spline = [abcd[i][splineNum] for i in range(4)]
		print(f"Spline {splineNum + 1}: ", end="")
		for i in range(len(spline) - 1):
				print(f"{(i + 1)*spline[i+1]}", end="")
				for j in range(i):
					print(f"(x-{xVals[splineNum]})", end="")
				if i + 1 == len(spline) - 1:
					print("")
				else:
					print(" + ", end="")

#clears the console for Linux, MacOS, or Windows; exits program otherwise
def clearConsole():
	# Clears scrollback buffer and screen for Mac: printf '\33c\e[3J'
	# Maybe does same for Linux? print this to console: "\033[H\033[2J"
	system = platform.system()
	if system == "Linux" or system == "Darwin":  
		command = "clear"
	elif system == "Windows":
		command = "cls"
	else:
		sys.exit("The system platform could not be determined.")
	os.system(command)

#only runs this code if the file itself is being run, not if it's being imported
if __name__ == '__main__':
	import colorama
	from colorama import Fore, Style, init

	#attempts to launch colorama by newer method; if it fails, defaults to older method
	try:
		colorama.just_fix_windows_console()
	except:
		init()

	besselXs = [1, 1.3, 1.6, 1.9, 2.2]
	besselYs = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]
	expXs = [0, 1, 2, 3]
	expYs = [math.exp(i) for i in range(4)]

	# running test 1
	for testLetter in ["a", "b"]:
		if testLetter == "a":
			xs = expXs
			ys = expYs
		else:
			xs = besselXs
			ys = besselYs	
		clearConsole()
		print(Fore.WHITE + Style.BRIGHT + f"Test 1{testLetter}:\n")
		print(f"Running Newton's Forward Divided Difference alogorithm on the points ", end="")
		print([(xs[i], ys[i]) for i in range(len(xs))].__str__()[1:-1] , ":\n", sep="")
		divDiffOutput = forwardDivDiff(xs, ys)
		print(Fore.GREEN + f"Coefficients: {divDiffOutput[0]}\n")
		print(Fore.YELLOW + f"The function evaluated at 1.5 is {divDiffPoly(divDiffOutput, 1.5)}.\n" + Style.RESET_ALL)
		junk = input("Press enter to continue...")

	# running test 2
	for testLetter in ["a", "b"]:
		expXs = [0, 1, 2, 3]
		expYs = [math.exp(i) for i in range(4)]
		if testLetter == "a":
			functionType = "Natural"
			output = natCubicSpline(expXs, expYs)
		else:
			functionType = "Clamped"
			output = clampCubicSpline(expXs, expYs, expYs[0], expYs[3])
		clearConsole()
		print(Fore.WHITE + Style.BRIGHT + f"Test 2{testLetter}:\n")
		print(f"Running the {functionType} Cubic Spline alogorithm on the points ", end="")
		expYs = [math.exp(i) for i in range(4)]
		#print([(expXs[i], expYs[i]) for i in range(len(expXs))].__str__()[1:-1] , ":\n", sep="")
		for i in range(len(expXs)):
			endChar = ", "
			if i == len(expXs) - 1:
				endChar = ":\n\n"
			print(f"{(expXs[i], expYs[i])}{endChar}", end="")
		print(Fore.GREEN + f"Coefficients:")
		letters = ['a', 'b', 'c', 'd']
		for i in range(len(output[0])):
			print(f"{letters[i]}: {output[0][i]}")
		print(Fore.YELLOW)
		for x in [0.5, 1.5, 2.5]:
			fOfX = cubicSplinePoly(output, x)
			print(f"Evaluating the {functionType[0].lower()}{functionType[1:]} cubic splines at {x}: {fOfX}")
		print(Style.RESET_ALL)
		junk = input("Press enter to continue...")
