import time
import numpy as np
import pandas as pd

def read(selection):
    input_dict=dict(a = 'kompetitives_programmieren/uebung6/Zusatzmaterial/a_example.in', 
                    b = 'kompetitives_programmieren/uebung6/Zusatzmaterial/b_little_bit_of_everything.in', 
                    c = 'kompetitives_programmieren/uebung6/Zusatzmaterial/c_many_ingredients.in', 
                    d = 'kompetitives_programmieren/uebung6/Zusatzmaterial/d_many_pizzas.in', 
                    e = 'kompetitives_programmieren/uebung6/Zusatzmaterial/e_many_teams.in')
    
    with open(input_dict[selection], 'r') as input_file:                    # read input
        items = input_file.read()
    items = np.array(items.split('\n'))                                     # extract read and split each row
    items = items[:-1]#pop last item
    items = np.char.split(items)

    return items

def get_ingre(pizza_df):
    # create an array with all ingredients 
    ingre_arr = pizza_df.melt()
    ingre_arr = np.array(ingre_arr['value'].unique()) # extract unique ingredients
    ingre_arr = ingre_arr[len(pizza_df[0].unique()):] # remove the amount of ingredients
    return ingre_arr

def object2int(pizza_df, ingre_arr):

    # transform pizza_df to a pizza_df with int as data type
    ingre_dict = {ingre_arr[i]: int(i)+1 for i in range(0, len(ingre_arr))} # create a dictionary of ingredients and their index

    # change ingredient to their index 
    pizza_df = pizza_df.replace(ingre_dict) 
    pizza_df = pizza_df.fillna(0) # fill nan with 0, its nessesary for the next step
    pizza_df = pizza_df.astype(np.int16) 

    return pizza_df

def get_runtime(text):
    end_time = time.perf_counter()
    print(f'Runtime {text}: {end_time - start_time:.2f}s')
    return 

start_time = time.perf_counter() # start measuring runtime

# get input 
input = 'c'
items = read(input) 
team_array, *pizza_array = items 
team_array = np.array(team_array, dtype=np.int32) # transform team_array all strings elements intro integers
pizza_df = pd.DataFrame(pizza_array)

# get all ingredients
inrgredients = get_ingre(pizza_df) 

# transform pizza_df of objects into a dataframe of integers
pizza_df = object2int(pizza_df, inrgredients)  
print(pizza_df)

get_runtime('pizza_df')



