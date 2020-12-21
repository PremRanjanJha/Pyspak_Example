import sys
from pyspark import SparkContext
from platform import python_version


sc = SparkContext(master="local", appName="Version")

print(f"Spark Version =  {sc.version }") #Check Spark Version

print(f"Python Version = {sys.version}") # Check version inside your Python program

print(f" Pycharm Python Version = {python_version()}") # Check version runing on Pycharm IDE
