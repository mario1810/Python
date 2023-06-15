#To gain access to the identifiers that are on our sub-modules when somebody imports from this package
#Make the package import specific things
__all__=["extract_upper"]

#Make the package import specific things (all functions from the module string)
from .strings import *