import time
import numpy as np
import pandas as pd

def read(selection):
    input_dict=dict(a = 'Google_hashcode2021/input/a_example.in', 
                    b = 'Google_hashcode2021/input/b_little_bit_of_everything.in', 
                    c = 'Google_hashcode2021/input/c_many_ingredients.in', 
                    d = 'Google_hashcode2021/input/d_many_pizzas.in', 
                    e = 'Google_hashcode2021/input/e_many_teams.in')
    
    with open(input_dict[selection], 'r') as input_file:                    # read input
        items = input_file.read()
    items = np.array(items.split('\n'))                                     # extract read and split each row
    items = items[:-1]#pop last item
    items = np.char.split(items)

    return items

def size_check(pizza_df, team_array):
    max_pizza = team_array[3]*4 + team_array[2]*3 + team_array[1]*2         # get the maximum amount of pizza that can be handled

    if max_pizza > team_array[0]:
        return pizza_df
    print('pizza overload!')

    
    pizza_df = pizza_df.sort_values(0, ascending=False)                      # sort the pizza by the amount of ingredients
    pizza_df = pizza_df.iloc[:team_array[0] - max_pizza]                     # remove the pizza with the lowest amount of ingredients
    pizza_df = pizza_df.sort_index()                                         # sort the pizza by the index
    return pizza_df

def get_ingre(pizza_df):
    # create an array with all ingredients 
    ingre_arr = pizza_df.melt()
    ingre_arr = np.array(ingre_arr['value'].unique())                       # extract unique ingredients
    ingre_arr = ingre_arr[len(pizza_df[0].unique()):]                       # remove the amount of ingredients
    return ingre_arr

def object2int(pizza_df, ingre_arr):

    # transform pizza_df to a pizza_df with int as data type
    ingre_dict = {ingre_arr[i]: int(i)+1 for i in range(0, len(ingre_arr))} # create a dictionary of ingredients and their index

    # change ingredient to their index 
    arr = np.array(pizza_df)                                    # get the amount of ingredients
    print(pizza_df)
    
    pizza_df.replace(to_replace=ingre_dict, inplace=True)
    #pizza_df = pizza_df.replace(ingre_dict, inplace=True) 

    pizza_df = pizza_df.fillna(0)                                           # fill nan with 0, its nessesary for the next step
    pizza_df = pizza_df.astype(np.int16) 
    print(pizza_df)
    return pizza_df

def get_runtime(text):
    end_time = time.perf_counter()
    print(f'Runtime {text}: {end_time - start_time:.2f}s')
    return 

# get input
start_time = time.perf_counter() # start measuring runtime 
input = 'e'
items = read(input) 
team_array, *pizza_array = items 
team_array = np.array(team_array, dtype=np.int32)                           # transform team_array all strings elements intro integers
pizza_df = pd.DataFrame(pizza_array)

# remove ingredients, if there are too many 
pizza_df = size_check(pizza_df, team_array)
get_runtime('size_check')


# get all ingredients
inrgredients = get_ingre(pizza_df) 

# transform pizza_df of objects into a dataframe of integers
pizza_df = object2int(pizza_df, inrgredients)  

get_runtime('object2int')

print(pizza_df)



