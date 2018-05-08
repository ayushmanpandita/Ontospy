# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Unit test stub for ontosPy

Run like this:

:path/to/ontospyProject>python -m ontospy.tests.test_methods

"""

from __future__ import print_function
import click 

import unittest, os, sys
from .. import *
from ..core import *
from ..core.utils import *


# sanity check
print("-------------------\nOntoSpy ",  VERSION, "\n-------------------")


class TestMethods(unittest.TestCase):

	# updated 2018-05-08

	dir_path = os.path.dirname(os.path.realpath(__file__))
	DATA_FOLDER = dir_path + "/rdf/"
	f = DATA_FOLDER + "pizza.ttl"
	o = Ontospy(f, verbose=True)

	printDebug("\n*****\nTest: loading with local file... > %s\n*****" % str(f), "important")

	def test1(self):
		"""
		Instances method
		"""
		printDebug("\n=================\nTEST 1: Checking the <instances> method", "green")

		for c in self.o.classes:
			# c.describe()
			if c.instances:
				print("CLASS: " + c.uri)
				print("INSTANCES: ")
				for el in c.instances:
					print(el.uri, el.qname)
					print(el.getValuesForProperty("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"))


	def test2(self):
		"""
		getValuesForProperty
		"""
		printDebug("\n=================\nTEST 2: Checking the <getValuesForProperty> method", "green")

		for c in self.o.classes[:3]:
			print("CLASS: ")
			print(c.uri, c.qname)
			print("RDF:TYPE VALUES: ")
			print(c.getValuesForProperty("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"))


	
	def test3(self):
		"""
		extract_entity_from_uri
		"""
		printDebug("\n=================\nTEST 2: Checking the <extract_entity_from_uri> method", "green")

		e = self.o.extract_entity_from_uri("http://www.co-ode.org/ontologies/pizza/pizza.owl#Germany")
		print("URI: ", e)
		print("RDFTYPE: ", e.rdftype)
		print("BEST LABEL: ", e.bestLabel())
		print("RDF SOURCE: ")
		print(e.rdf_source())


	
	
	print("Success.\n")



if __name__ == "__main__":
	unittest.main()
