# sort out free apps and paid apps
# import csv module 
import csv

# open the AppleStore.csv file read the file and turn it into a list of list 
store_info = open("AppleStore.csv")
read = csv.reader(store_info)
data = list(read)
free = []
cost = []
rate = []
poor_rate =[] 
for money in data[1:]:
	price = float(money[5]) 
	name  = money[2]
	rating = float(money[8])

# goes throught the price list and gets the names of the applications are free
	if price == 0 and rating >= 4.0: 
		free.append(name)
		rate.append(name)
		# print(f"Free: {name}")
# appends any of the apps that price doesn't equal 0 
	elif price != 0 and rating >= 4.0: 
		cost.append(name)
		rate.append(name)	
		print(f"Cost: {name} {price}")
	else: 
		poor_rate.append(name)
		print(f"Rating below 4.0: {name}")
cost_data = [cost, rating]
free_data = [free,rating]
print(f"""Number of paid apps: {len(cost_data[0])} 
Number of free apps: {len(free_data[0])}
Apps that don't rate 4.0 and above: {(len(data)) - (len(free_data[0]) + len(cost_data[0])) }
Number of total apps in the list: {len(data)}		
		""")

