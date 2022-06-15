import sys
from fuont.holes import chrf

print('Usage: python -m fuont [hex code of letter A] [string to convert]')


if __name__ == '__main__':
    hexA = sys.argv[1].lower()

    for inputString in sys.argv[2:]:
        print(''.join([chrf(ord(c) + int(hexA,16)-97) for c in inputString]))
