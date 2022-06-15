import sys
import string
from fuont.holes import chrf

print('Usage: python -m fuont.alpha [hex code of letter A]')

hexA = sys.argv[1]

print(''.join([chrf(int(hexA,16)+i) for i in range(26)]))
