from yaml import load, Loader
from pprint import pprint
import sys
print sys.argv
if "v" in sys.argv:
        print "verbose"
	for x in sys.argv[2:]:
    		pprint(load(open(x), Loader=Loader))
else:
	for x in sys.argv[1:]:
    		print "valid: {} {}".format(x, bool(load(open(x), Loader=Loader)))
