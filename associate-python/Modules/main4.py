print("importing  helpers from main")
from helpers import *

print("Importing extras from main")
import extras

print(f"Lower: {extract_lower(extras.name)}")
print(f"Upper: {extract_upper(extras.name)}")
