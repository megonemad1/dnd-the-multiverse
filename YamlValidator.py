from yaml import load, Loader
from pprint import pprint
import sys
if "v" in sys.argv:
    pprint(load(open(sys.argv[1:][-1]), Loader=Loader))
else:
    print "valid: ", bool(load(open(sys.argv[1:][-1]), Loader=Loader))
