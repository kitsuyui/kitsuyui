# 変更できない dict が欲しいとき

```python
def sample(x={}):
    if 'a' not in x:
        x['a'] = 0
    x['a'] += 1
    return x['a']


sample()  # => 1
sample()  # => 2
```


```python
from types import MappingProxyType
def sample2(x=MappingProxyType({})):
    if 'a' not in x:
        x['a'] = 0
    x['a'] += 1
    return x['a']


sample2()
sample2()
```

```
TypeError: 'mappingproxy' object does not support item assignment
```
