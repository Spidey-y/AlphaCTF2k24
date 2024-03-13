# writeup
## prison

we can find the whitelist after bruteforcing

```py
whitelist = 'l">)ai./1r<nhepx\'(+dcg'
```

not the goal is to pass
```py
"print(open('flag.txt').read())"
```
since we cant use all charecters we will try to bypass that using 
```py
chr
```

then we find a length constraint
our input must be less that 138
so we will try to make the payload shorter using bitwise shift operators

```
<< shift left
>> shift right
```

the final payload

```py
"prin"+chr((11>>1)+111)+"("+chr((111<1)+111)+"pen"+"('"+chr((111<<11>>1)//1111)+"lag."+chr((11>>1)+111)+"x"+chr((11>>1)+111)+"').read())"
```