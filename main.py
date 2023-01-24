import time
import numpy as np
import pandas as pd



def read(selection):
    input_dict=dict(a = 'Google_hashcode2021/input /a_example.in', 
                    b = 'Google_hashcode2021/input /b_little_bit_of_everything.in', 
                    c = 'Google_hashcode2021/input /c_many_ingredients.in', 
                    d = 'Google_hashcode2021/input /d_many_pizzas.in', 
                    e = 'Google_hashcode2021/input /e_many_teams.in')
    
    with open(input_dict[selection], 'r') as input_file:                    # read input
        items = input_file.read()
    items = np.array(items.split('\n'))                                     # extract read and split each row
    items = items[:-1]#pop last item
    items = np.char.split(items)

    return items

def build_dataframe(pizza_array):
    pizza_df = pd.DataFrame(pizza_array)

    # rename columns     
    new_column_names = {i: "ingredient_{}".format(i) if i > 0 else 'amount' for i in range(0, len(pizza_df.columns))} # create a dictionary of new column names
    pizza_df.rename(columns = new_column_names, inplace = True)
    return pizza_df

def split_df(pizza_df):

    # better readable names
    df_size = pizza_df.size
    if df_size < 10000 : return pizza_df # skip df splitting if dataframe is small
    target_sub_dfs = 20
    df_size = pizza_df.size
    max_col = pizza_df.shape[1]

    target_size = (max_col * pizza_df.shape[0]) // target_sub_dfs
    dataframes = []
    n_steps = target_size // max_col # n_steps are also the target number of rows
    iloc_start = 0
    iloc_end = n_steps
    
    for i in range(target_sub_dfs):  # slice dataframes in subdataframes
        df = pizza_df.iloc[iloc_start : iloc_end]
        iloc_start += n_steps
        iloc_end += n_steps
        dataframes.append(df)

    return dataframes

def pizza_selecter(pizza_df):
    # create sub delivery




    return

def get_runtime(text):
    end_time = time.perf_counter()
    print(f'Runtime {text}: {end_time - start_time:.2f}s')
    return 

start_time = time.perf_counter() # start measuring runtime

# get input 
input = 'b'
items = read(input) 
team_array, *pizza_array = items 
team_array = np.array(team_array, dtype=np.int32) # transform an array of strings intro an array of integers, easier to handle in following code
pizza_df = build_dataframe(pizza_array) 

# creat an array with an ingredient array
ingre_arr = np.unique(pizza_df.dropna().values) #  get all uniques (ingredients) in the pizza_df except 'nonetypes'
ingre_arr = ingre_arr[1:] 

# split dataframe in a smaller sub dataframes for better performance, but decrease accuracy. Pass dataframes < 10000 items
pizza_df = split_df(pizza_df)
get_runtime('pizza_df')


# create delivery 
delivery = pizza_selecter(pizza_df)
    # interupt if no ingredients left
     
    # deliver team of four - selection by determine intersection 
    # while-loop till no team left?

    # delivor team of three and two - sort pizza by amount of ingredients and select top and bottom pizza
    # while-loop till no team left
    # merge dfs together?

    
    





