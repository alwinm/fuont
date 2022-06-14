import sys

print('Usage: python -m fuont [hex code of letter A] [string to convert]')

hexA = sys.argv[1].lower()

for inputString in sys.argv[2:]:
    print(''.join([chr(ord(c) + int(hexA,16)-97) for c in inputString]))
