from functools import reduce 

domain = [1, 2, 3, 4, 5]

#f(x)=x*2
our_range = map(lambda num: num * 2,domain)
#our_range is a map object
print( list(our_range))

evens = filter(lambda num: num % 2==0, domain)
print(list(evens))

the_sum = reduce( lambda accumularor, num: accumularor+num, domain,0)
print(the_sum)

words= ["Boss", "a", "Alfred", "fig", "Deamon", "dig"]
print("Sorting by default")
print(sorted(words)) #Create a new list

print("Sorting with a lambda key")
print(sorted(words,key=lambda s:s.lower())) # create a new list with sorted

print("Sorting with  a method")
words.sort(key=str.lower,reverse=True)
print(words) #change the list itself




