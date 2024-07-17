bicycles = ['trek', 'cannondale']
print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

#Inserting
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(2, 'ducati')
print(motorcycles)          

#Removing
del motorcycles[0]
print(motorcycles)
print(motorcycles.pop())

motorcycles.remove('ducati')
print(motorcycles)

#organizing a list
cars = ["bmw", "audi", "toyota","tesla"]
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

    #Temporary Sort sorted(cars)
print("sorted(carts, reverse=True):",sorted(cars, reverse=True))

#Reverse Order
cars.reverse()
print("cars.reverse():",cars)

