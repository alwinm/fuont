# A dict to help deal with holes, since Unicode did not want to duplicate definitions

hole_dict = {}

pairs = [('1d455','210e'), # ℎ Mathematical Italic Small
         
         # Mathematical Script Capital          
         ('1d49d','212c'), # ℬ 
         ('1d4a0','2130'), # E
         ('1d4a1','2131'), # F
         ('1d4a3','210b'), # H
         ('1d4a4','2110'), # I
         ('1d4a7','2112'), # L
         ('1d4a8','2133'), # M
         ('1d4ad','211b'), # R

         # Mathematical Script Small
         ('1d4ba','212f'), # e 
         ('1d4bc','210a'), # g
         ('1d4c4','2134'), # o

         # Mathematical Fraktur Capital (using Black Letter Capital)
         ('1d506','212d'), # C
         ('1d50b','210c'), # H
         ('1d50c','2111'), # I
         ('1d515','211c'), # R
         ('1d51d','2128'), # Z

         # Mathematical Double-struck Capital
         ('1d53a','2102'), # C
         ('1d53f','210d'), # H
         ('1d545','2115'), # N
         ('1d547','2119'), # P
         ('1d548','211a'), # Q
         ('1d549','211d'), # R
         ('1d551','2124'), # Z                  
]


for x,y in pairs:
    if y:
        hole_dict[int(x,16)] = int(y,16)


def chrf(x):
    if x in hole_dict:
        return chr(hole_dict[x])
    return chr(x)
