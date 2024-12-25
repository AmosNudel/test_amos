import pandas as pd
import math

df = pd.read_csv('data.csv')


# Highest Price:
highest_price = df['price'].max()


#Price Avrage:
sum = 0
for price in df['price']:
    sum += price
avg = sum / (len(df['price']) - 1)


#Number of ideals:
ideal_counter = 0

for cut in df['cut']:
    if cut == 'Ideal':
        ideal_counter += 1


#colors:
color_counter = 0
color_array = []
def color_count():
    global color_counter
    for color in df['color']:
        if color not in color_array:
            color_counter += 1
            print(f"Color: {color}")
            color_array.append(color)
    print(f"There are {color_counter} colors")

#The carat of the half index of premium cuts:
premium_array_half = []

for index, cut in enumerate(df['cut']):
    if cut == "Premium":
        premium_array_half.append(index)

mid_index = math.floor(len(premium_array_half) / 2)

def get_middle_carat():
    global mid_index
    for index, carat in enumerate(df['carat']):
        if index == mid_index:
            print(f"The carat of the premium cut in the middle is: {carat}")

# avrage carat for each cut:
ideal_carat_array = []
good_carat_array = []
very_good_carat_array = []
premium_carat_array = []

for index, row in df.iterrows():
    if row['cut'] == "Ideal":
        ideal_carat_array.append(row['carat'])
    elif row['cut'] == "Good":
        good_carat_array.append(row['carat'])
    elif row['cut'] == "Very Good":
        very_good_carat_array.append(row['carat'])
    elif row['cut'] == "Premium":
        premium_carat_array.append(row['carat'])

total_ideal = 0
for carat in ideal_carat_array:
    total_ideal += carat

avrage_ideal = total_ideal / len(ideal_carat_array)


total_good = 0
for carat in good_carat_array:
    total_good += carat

avrage_good = total_good / len(good_carat_array)


total_very_good = 0
for carat in very_good_carat_array:
    total_very_good += carat

avrage_very_good = total_very_good / len(very_good_carat_array)


total_premium = 0
for carat in premium_carat_array:
    total_premium += carat

avrage_premium = total_premium / len(premium_carat_array)


#avrage price per color

e_array = []
i_array = []
j_array = []
h_array = []
f_array = []
g_array = []
d_array = []

for index, row in df.iterrows():
    if row['color'] == "E":
        e_array.append(row['price'])
    elif row['color'] == "I":
        i_array.append(row['price'])
    elif row['color'] == "J":
        j_array.append(row['price'])
    elif row['color'] == "H":
        h_array.append(row['price'])
    elif row['color'] == "F":
        f_array.append(row['price'])
    elif row['color'] == "G":
        g_array.append(row['price'])
    elif row['color'] == "D":
        d_array.append(row['price'])
    

total_e = 0
for price in e_array:
    total_e += price

avrage_e = total_e / len(e_array)


total_i = 0
for price in i_array:
    total_i += price

avrage_i = total_i / len(i_array)


total_j = 0
for price in j_array:
    total_j += price

avrage_j = total_j / len(j_array)


total_h = 0
for price in h_array:
    total_h += price

avrage_h = total_h / len(h_array)


total_f = 0
for price in f_array:
    total_f += price

avrage_f = total_f / len(f_array)


total_g = 0
for price in g_array:
    total_g += price

avrage_g = total_g / len(g_array)


total_d = 0
for price in d_array:
    total_d += price

avrage_d = total_d / len(d_array)


if __name__=="__main__":
    # Highest Price:
    print(f"The highest price is: {highest_price}")
    #Price Avrage:
    print(f"The avrage price is {math.floor(avg)}, rounded down.")
    #Number of ideals:
    print(f"There are {ideal_counter} ideal cuts.")
    #colors:
    color_count()
    #The carat of the half index of premium cuts:
    get_middle_carat()
    # avrage carat for each cut:
    print(f"The avrage carat of an ideal cut is: {avrage_ideal}")
    print(f"The avrage carat of a good cut is: {avrage_good}")
    print(f"The avrage carat of a very good cut is: {avrage_very_good}")
    print(f"The avrage carat of a premium cut is: {avrage_premium}")
    #avrage price per color
    print(f"The avrage price of an E color is: {avrage_e}")
    print(f"The avrage price of an I color is: {avrage_i}")
    print(f"The avrage price of an J color is: {avrage_j}")
    print(f"The avrage price of an H color is: {avrage_h}")
    print(f"The avrage price of an F color is: {avrage_f}")
    print(f"The avrage price of an G color is: {avrage_g}")
    print(f"The avrage price of an D color is: {avrage_d}")
