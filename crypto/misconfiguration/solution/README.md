# misconfiguration
## Write up

we were given this:
```
c = 44845677627141622140887574178478387679526777674999624331264892460077814962297242819909194161872930746713559645889363194616437071651930433092457662361088439653487817323635497574995531930513553552694329113579575082922379636661420288544554517897647109626175162432548437091295139804230190014085193956510067231114
e = 32
N = 175172386972134042106714875854909861637321963986240854241688167823368303617176297981603845920281917001838565391273684550635003526191377686367411965977790168189072030265148988509223956322164360184076912270270641108529921752195916612944263345992742002591054202758545082304676227431235658202316127843107785760383

```

first thing i noticed is that n is prime so we can easily calculate the phi
the phi should not be prime in rsa

```
phi = n-1
```

but the problem is that gcd(phi, e) != 1

so we cant calculate the d so we cant decrypt the encrypted text

but how we can solve the challenge

we need to know a bit of math 
so here is the way i used to solve 

in normal rsa 

```
d*e = 1 % phi
d*e = (k * phi) + 1
so we got 
d * e - k * phi = 1
```

but since gcd(phi, e) = 2 the formula will be

```
d * e - k * phi = 2

```

so we can calculate the d easily using the extended euclidian algorithm 

after calculating the d we cant decrypt normally as we said before because gcd(phi, e) != 1

so how we will do it

we got this 

```
c = m ** e % n
c**d %n = m ** (e*d) % n ---eq1
```

and from the previous formula we got this 

```
d * e - k * phi = 2

d * e = k * phi + 2
```

so we will get this 
```
m ** (e*d) % n = m ** k * phi + 2 % n
```

now we will use fermat little theorem

read more abot it here 
https://en.wikipedia.org/wiki/Fermat's_little_theorem

```
m ** (k * phi) % n ≡ 1 % n 
m ** (k * phi) + 2 % n ≡ m**2 % n  --- eq2
```

by using eq1 and eq2

we can find m

```
m**2 % n = c**d % n
```

now lets get the flag 

> flag : shellmates{so_modular_square_root_is_a_thing}

the solve [script](./solve.py)

