# wizard
## writeup

the challenge generate output like this 

c = (m ** (2**i)) % p
we can transform it like this 
c = ((m ** i) ** 2) % p
we keep calculatin quadratic residues until we reach the flag

this is quadratic residue read more about it here :
https://en.wikipedia.org/wiki/Quadratic_residue

Solve script [here](./solve.py)                                                                                                                                                                                                                                             
