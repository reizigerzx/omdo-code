# Python Best Practices

## Swapping Variables
```python
a, b, c, d, e = 10, 20, 30, 40, 50
a, b, c, e, d = a, d, a, b, e
```

## Chain Comparison
```python
a = 25
#if ((a >= 20) and (a <= 30))
if(20 <= a <= 30)
```

## Value Packing
```python
a, b, c = 10, 20, 540
d = a, b, c  # tuple
d = [a,b,c] # list
```

## Value Unpacking
```python
d = [10, 41, 56]
a, b, c = d
```

## For
```python
#for i in range(len(d)):
#	print(d[i])
for i in d :
	print i
```

## ZIP
```python
nim : ['001','002','003']
nama : ['Asep','Tejo','Wakanda']
for n_nim, n_nama in zip(nim,nama):
	print({n_nim}, {n_nama})
```