#!/usr/bin/python

from sys import argv
import math

G = float(6.67 * math.pow(10, -11))

class Planet(object):

	def calculateMass(self, radius, density):
		volume = float(float(4)/3 * math.pow(radius, 3) * math.pi)
		mass = float(volume * density)
		return float(mass)


	def __init__(self, parametersList):
		self.__name = str(parametersList[0])
		self.__radius = int(parametersList[1])
		self.__mass = self.calculateMass(self.__radius, int(parametersList[2]))
		self.__force = 0

	def __str__(self):
		return "{} : {} [m], {} [kg]".format(self.__name, self.__radius, self.__mass)

	def calculateForce(self, objectMass):
		self.__force = G * ( self.__mass * objectMass) / float(math.pow(self.__radius, 2))

	def printForce(self):
		print "{}: {} [N]".format(self.__name, self.__force)	

def main():
	if len(argv) < 2:
		print "Please, pass some arguments !!!"
	else:
		objectMass = 0
		planetList = []
		filename = argv[1]
		with open(filename) as f:
			fileContent = [line.strip('\n') for line in f.readlines()]
		objectMass = int(fileContent[0])
		for line in range(2, len(fileContent)):
			planet = Planet(fileContent[line].split(', '))
			planet.calculateForce(objectMass)
			planet.printForce()
		


if __name__ == '__main__':
	main()