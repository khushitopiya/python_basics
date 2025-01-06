#using replace 
a = "we are python developer"
b = a.replace(' ', '*')
print(b)




tuple = ("apple", "banana", "cherry")
for x in tuple:
  print(x)





thisdict = {
  "brand": "bmw",
  "model": "i3",
  "year": 2014
}
thisdict["color"] = "Black"
print(thisdict)





#half 
rows = 5
for i in range(1, rows + 1):
    print('*' *i)




#full
rows = 10
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))



#numbers
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()




sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)



numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[1:11:2])



for x in range(1,4):
    sea_creatures += ['fish']
    print(sea_creatures)



sea_creatures =['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone', 'yeti crab']

del sea_creatures[1:4]
print(sea_creatures)
