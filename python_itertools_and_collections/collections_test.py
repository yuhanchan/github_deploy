import collections

### namedtuple
Point = collections.namedtuple('Point', ['x', 'y', 'z']) # kinda like a simple way to create a class
p = Point(1, 2, 3)
print(p.x)
print(p.y)
print(p.z)
print(p)

### deque
d = collections.deque('abc')
print(d)
for i in d:
    print(i)
# methods:
d.append(4) # append to right (end)
d.appendleft(1) # append to left (begin)
d.clear() # clear all items
d_copy = d.copy()
d_copy.append(1) # will not affect d
d = collections.deque([1,2,3,4,1])
print(d.count(1)) # count number of 1
d.extend(['a', 'b']) # similar to append, but input is a iterable item, like a list
d.extendleft(['a', 'b']) # will append 'b', 'a' to the left (append 'a', then 'b', so the left most will be 'b')
print(d.index('a')) # return the first match, 
d.insert(2, 'x') # insert 'x' to index 2
d.pop() # pop from right
d.popleft() # pop from left
d.remove('a') # remove the first occurance of 'a'
d.reverse() # reverse queue in place
d.rotate(2) # rotate 2 to the right, use negative number if want to rotate left
print(d)

### ChainMap, you can access multiple maps as if there is only one map
dic1 = {'a': 1, 'b': 2}
dic2 = {'a': 3, 'c': 4}
dic3 = {'d': 5}
chain = collections.ChainMap(dic1, dic2)
chain = chain.new_child(dic3)
print(chain)
print(list(chain.keys()))
print(list(chain.values()))
print(chain['a']) # access
print(chain.get('b')) # access

### Counter, this can be very useful
c = collections.Counter(['a','b','c','b'])      # Multiple ways to initialize
c = collections.Counter({'red': 4, 'blue': 2})  # Multiple ways to initialize
c = collections.Counter(cats=4, dogs=8)         # Multiple ways to initialize
c = collections.Counter('abfddss')              # Multiple ways to initialize
c2 = collections.Counter('fhfask')              # Multiple ways to initialize
print(c['s']) # access counter
print(c.most_common(2)) # The most common 2, return [('d', 2), ('s', 2)]
print(c)
c.subtract(c2) # substract another counter
print(c)
