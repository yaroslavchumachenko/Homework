# The sys module.

#  The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within Python? 
# If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
import sys

# Default sys.path
print(sys.path)

# Modified sys.path
sys.path.append("E:\\Pythonmod")
print(sys.path)

# Is it possible to change it from within Python?
# Yes, by using setx PYTHONPATH "C:\path\to\your\directory;%PYTHONPATH%"
# You can point a definite path to the dir that you wand to add