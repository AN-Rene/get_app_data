# import csv module 
import csv 

# open the AppleStore.csv file read the file and turn it into a list of list 
store_info = open("AppleStore.csv")
read = csv.reader(store_info)
data = list(read)

# establish an empty float variable 
x = 0.0
# get rating data from the list and calculate the average using a for loop 
for rate in data[1:]: #[1:] Excludes the header row 
	rating = float(rate[8])
	x = x + rating

avg = x / len(data)

print(round(avg,1))