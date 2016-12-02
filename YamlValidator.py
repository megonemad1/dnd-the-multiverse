from yaml import load, Loader
from pprint import pprint
import sys
if "v" in sys.argv:
	for x in sys.argv[2:]:
    		pprint(load(open(x), Loader=Loader))
else:
	for x in sys.argv[1:]:
    		print "valid: {} {}".format(x, bool(load(open(x), Loader=Loader)))
