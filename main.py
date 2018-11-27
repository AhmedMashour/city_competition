# Add python code in this file
import csv

#Defining End and Beginning of each csv row 
delimiter=','
quotechar='"'

# Defining cities and points holder initially
cities = []
points = []

# This for defining the header of output csv
heading = ['ID','X','Y','City']


# To determine if coordinate in range of an axis or not.. 
# because city is without rotation
# we determinie a side on which value of axis is bigger in value and which is smaller to determine the operation
# Then return after comparsion is the point in range of that axis or not
def is_point_in_range(coordinate,botom,top):
        side = (int(top) - int(botom)) > 0
        if not side:
            return int(botom) >= int(coordinate) >= int(top)
        else:
            return int(botom) <= int(coordinate) <= int(top)

#fetching cities and storing them
with open('./cities.csv', 'r') as citiesfile:
    # Converting read file into a dictionary and pointing rows into cities list
    dect_reader = csv.DictReader(citiesfile, delimiter= delimiter, quotechar = quotechar)
    cities = [row_dect for row_dect in dect_reader]
    
#fetching points and working them, Nested loop also to iterate over cities for each point
with open('./points.csv', 'r') as pointsfile, open('output.csv', 'w') as output:
    # points = load_csv(pointsfile)
    output_writer = csv.writer(output, dialect='excel')
    output_writer.writerow(heading)

    #The same in converting csv file into dectionary then iterating over rows
    dect_reader = csv.DictReader(pointsfile, delimiter= delimiter, quotechar = quotechar)
    for point in dect_reader:
        values = []
        for city in cities:
            # Determine range for x axis
            range_x = is_point_in_range(point['X'],city['BottomRight_X'], city['TopLeft_X'])

            # if not in x range no need to continue for that point
            if not range_x:
                continue

            # Determine range for y axis
            range_y = is_point_in_range(point['Y'],city['BottomRight_Y'], city['TopLeft_Y'])
            
            # Giving the city column to the point
            if range_x and range_y:
                point['City'] = city['Name']
            else:
                point['City'] = 'None'

            # prepare point for the writer (it take an array)
            for key in heading:
                print('for key', key, 'value', point[key])
                values.append(point[key])
            # saving the point  
            output_writer.writerow(values)

