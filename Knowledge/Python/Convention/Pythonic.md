# Pythonic

https://www.youtube.com/watch?v=yOkUgGrmR2c

## Looping
non-pythonic
```python
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)
```

```python
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)
```

pythonic
```python
best_list = [name for name in names if len(name) >= 6]
```