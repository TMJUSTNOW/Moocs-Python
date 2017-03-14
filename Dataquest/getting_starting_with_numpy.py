import csv
f = open("world_alcohol.csv")
reader = csv.reader(f)
world_alcohol = list(reader)

years = []
for row in world_alcohol:
    years.append(row[0])

years = years[1:]

total = 0
for year in years:
    total = total + float(year)

avg_year = total / len(years)


#NumPy is a Python module that is used to create and manipulate multidimensional arrays.

#An array is a collection of values. Arrays have one or more dimensions. An array dimension is the number of indices it takes to extract
#a value. 
#Each value in a NumPy array has to have the same data type
#In a list, we specify a single index, so it is one-dimensional:
#A list is similar to a NumPy one-dimensional array, or vector, because we only need a single index to get a value.
first_row =  [1986, "Western Pacific", "Viet Nam", "Wine", 0]
print(first_row[0])


#The code would read in the nfl.csv file into a NumPy array. 
#NumPy arrays are represented using the numpy.ndarray class. We'll refer to ndarray objects as NumPy arrays in our material.
import numpy
nfl = numpy.genfromtxt("nfl.csv", delimiter=",")

#Create Array
vector = numpy.array([10, 20, 30])
matrix= numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
#visualiser le shape
matrix_shape = matrix.shape
#visualiser le type d'un array
world_alcohol_dtype = world_alcohol.dtype


#Reading In The Data Properly
    #u75 =  This specifies that we want to read in each value as a 75 byte unicode data type
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)
print(world_alcohol)



#Assign the whole third column from world_alcohol to the variable countries.
#Assign the whole fifth column from world_alcohol to the variable alcohol_consumption.

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]



#Assign all the rows and the first 2 columns of world_alcohol to first_two_columns.
# attention, non inclusive
first_two_columns= world_alcohol[:,0:2]


#Selecting Elements
#Compare the third column of world_alcohol to the string Algeria.
#Assign the result to country_is_algeria.
#Select only the rows in world_alcohol where country_is_algeria is True.
#Assign the result to country_algeria.

country_is_algeria = world_alcohol[:,2] == "Algeria" #renvoie true ou false pour chaque élément
country_algeria=world_alcohol[country_is_algeria]


#replacing

world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'
world_alcohol[:,3][world_alcohol[:,3] == 'Wine'] = 'Grog'

#converting data type 
#We can convert the data type of an array with the astype() method.
vector = numpy.array(["1", "2", "3"])
vector = vector.astype(float)
