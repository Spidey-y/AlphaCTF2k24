
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot, gcdext, gcd

c = 44845677627141622140887574178478387679526777674999624331264892460077814962297242819909194161872930746713559645889363194616437071651930433092457662361088439653487817323635497574995531930513553552694329113579575082922379636661420288544554517897647109626175162432548437091295139804230190014085193956510067231114
e = 32
N = 175172386972134042106714875854909861637321963986240854241688167823368303617176297981603845920281917001838565391273684550635003526191377686367411965977790168189072030265148988509223956322164360184076912270270641108529921752195916612944263345992742002591054202758545082304676227431235658202316127843107785760383

phi = N-1

d = gcdext(e, phi)

flag_2 = pow(c, d[1], N)

flag, is_root = iroot(flag_2, gcd(phi, e))

print(long_to_bytes(flag))