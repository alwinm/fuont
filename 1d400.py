from fuont.holes import chrf

hexA = '0x1d400'
intA = int(hexA,16)

for i in range(40):
    base = intA + i*26
    print(hex(base),''.join([chrf(base+i) for i in range(26)]),'\n')

    
