import itertools
import operator

### infinite iterators
itertools.count(10, 2) # count(start, step)
itertools.cycle('ABCD') # will repeat ABCD ABCD ...
itertools.repeat(10, 4) # repeat(obj, times) repeat obj times time

### Useful tools
l1 = [1,2,3,4,5]
gen = itertools.accumulate(l1, operator.mul) # apply operator to l1, which gives runing product, returns a generator
print(next(gen)) # get next elm of generator
print(next(gen))

gen = itertools.chain('a', 'c', '123') # chains all input
print(next(gen))
print(next(gen))

gen = itertools.chain(['ABC', 'DEF']) # will get 'ABC' -> 'DEF'
print(next(gen))

gen = itertools.chain.from_iterable(['ABC', 'DEF']) # will get 'A' -> 'B' -> 'C' -'D' -> ...
print(next(gen))

gen = itertools.compress([1,2,3,4,5], [0,0,1,0,1]) # compress(data, selector), only selector where selector is not 0
print(next(gen))
print(next(gen))

gen = itertools.dropwhile(lambda x: x<5, [1,2,3,4,5,7,1]) # dropwhile(cond, seq), will get [5, 7, 1], stop droping once cond fail
print(list(gen))

gen = itertools.takewhile(lambda x: x<5, [1,2,3,4,5,7,1]) # takewhile(cond, seq), will get [1,2,3,4], stop taking once cond fail, opposite of dropwhile
print(list(gen))

gen = itertools.filterfalse(lambda x: x%2, [1,2,3,4,5]) # filterfalse(cond, seq), will get [2, 4], where cond is false
print(list(gen))

res = [[k, list(g)] for k, g in itertools.groupby('AABBCABB')] # will return (k, g) pairs, where k is key, and g is a generator
res = [[k, len(list(g))] for k, g in itertools.groupby('AABBCABB')] # usually used this way to get (key, repeat_num) pair
print(res)

gen = itertools.islice('ABCDE', 2) # islice(seq, [start], end, [step])
print(list(gen))

gen = itertools.starmap(pow, [(2,3), (3,5)]) # starmap(func, input), apply func to inputs 2^3, 3^5
gen = itertools.starmap(pow, [[2,3], [3,5]]) # both tuple and list work
print(list(gen))

gen = itertools.zip_longest('ABCD', 'ab') # zip two inputs, fill with None in default
gen = itertools.zip_longest('ABCD', 'ab', fillvalue='*') # zip two inputs, fill with * for shorter one
print(list(gen))

### Combinatoric iterators:
gen = itertools.product('ABC', 'xy') # Ax Ay Bx By Cx Cy
gen = itertools.product(range(2), repeat=3) # 000 001 010 011 100 101 110 111
print(list(gen))

gen = itertools.permutations([1,2,3,4,5], 3) # permutation(inputs, length), return all permutations with length
gen = itertools.permutations(range(5), 2)
print(list(gen))

gen = itertools.combinations([1,2,3,4,5], 3) # combinations(inputs, length), return all combinations with length
gen = itertools.combinations(range(5), 2)
print(list(gen))

gen = itertools.combinations_with_replacement([1,2,3,4,5], 3) # similar to combinations, but with replacement
gen = itertools.combinations_with_replacement(range(5), 2)
print(list(gen))
