# algebra
## writeup

we were given a gift which is s and we know that
```
p ** (s+2) % s
```

to solve the challenge we need to use fermat little theorem

```
p ** n-1 % n == 1
p ** n % n == p
then we got 
p ** n+1 % n == p**2
p ** n+2 % n == p**3
gift == p**3
```

so we p is equal to the cube root of the gift

