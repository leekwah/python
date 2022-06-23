import pandas
house = pandas.read_csv('house.csv')
print(house)
print(house.head(2))
print(house.describe()) #각각 column의 성격을 파악하고 싶을 때 사용하면 된다.