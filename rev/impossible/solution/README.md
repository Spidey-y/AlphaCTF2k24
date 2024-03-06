# impossible
## writeup

we decompile the code in ghidra we see so many conditions the chall description says dont do it manualy so we need to write a solver to do solve the challenge
so the idea is to use symbolic execution i used a python library called angr https://angr.io/


the script can be found [here](./solve.py)