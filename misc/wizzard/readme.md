## MISC - Wizzard

```bash
python3 -c "print('-~('*100+'()==()'+')'*100)" | nc localhost 1107
```

- `()==()` is True, empty tuple equals empty tuple
- `-~(()==())` The tilde (**`~`**) is a bitwise NOT operator, so it flips the bits of the result. In Python, **`True`** is represented as **`1`** and **`False`** as **`0`**. So, **`~True`** becomes **`-2`** (in a two's complement representation) and `-` returns 2
- each time we do `-~(x)` it translates to `(x+1)`
