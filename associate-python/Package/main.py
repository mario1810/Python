from helpers.strings import extract_lower, extract_upper
from helpers import variables
import helpers #Import entire packaage
print(f"Lowercase: {extract_lower(variables.name)}")
print(f"Uppercase: {extract_upper(variables.name)}")
print(f"From helpers: {helpers.strings.extract_lower(variables.name)}")