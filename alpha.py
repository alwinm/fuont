import sys
import string
print('Usage: python -m fuont.alpha [hex code of letter A]')

hexA = sys.argv[1]

print(''.join([chr(int(hexA,16)+i) for i in range(26)]))
