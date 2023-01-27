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
    pizza_df = pizza_df.sort_index()                                         # sort the pizza by index
    return pizza_df

def get_ingre(pizza_df):
    # create an array with all ingredients 
    ingre_arr = pizza_df.melt()
    ingre_arr = np.array(ingre_arr['value'].unique())                       # extract unique ingredients
    ingre_arr = ingre_arr[len(pizza_df[0].unique()):]                       # remove the amount of ingredients
    ingre_arr = ingre_arr[:-1]                                              # and last item
    return ingre_arr

def create_delivery2(pizza_df, team_array,input):
    def determine_team_size(team_array):
        team = 4
        if team_array[3] == 0:
            team = 3
            if team_array[2] == 0:
                team = 2
        return team
    
    def gen_rand_df(df):
      
        df = df.reset_index()
        data = df.values
        np.random.shuffle(data)
        df = pd.DataFrame(data, columns=df.columns)

        return df

    def rating(rand_df,team_size):
        score_data = []
        loops = len(rand_df.index) // team_size
            
        for _ in range(loops):
            combination = np.array(rand_df.iloc[:team_size, 0]).astype(np.int64)
            ingredient = np.array(rand_df.iloc[:team_size,2:]).astype(object)
            ingredient = np.concatenate(ingredient[0:team_size-1], axis=0) # convert all rows as one row
            ingredient, counts = np.unique(ingredient, return_counts=True) # extract the values for the rating
            counts = np.count_nonzero(counts == 1)  # define score by the amount of ones
            combination = np.concatenate((combination, [counts]))
            score_data.append(combination)
            rand_df = rand_df.iloc[team_size:]
            


        score_data = pd.DataFrame(score_data)


        score_data = score_data.sort_values(team_size, ascending=False)
        return score_data
    
    pizza_df = pizza_df.fillna('0')
    delivery = []
    output_file = pd.DataFrame()
    output_file.astype(np.int64)
    
    
    # 1. generate a shuffled copy of the pizza dataframe and genarate delivery combination
    # 2. rate the combinations
    # 3. pick the best combination and go back to step 1

    sub_diliverys = team_array[3] // 3
    for _ in range(8):
    
        # determine wich team is choosen and how many diliverys this loop generate
        team = determine_team_size(team_array)
        
        # generates a random df by shuffling the rows
        rand_df = gen_rand_df(pizza_df) 
        
        # creat a scoring df the last element is the score lvl and tranfer the best 1/3 of the score to outputfile
        delivery = rating(rand_df, team)
        if team_array[team-1] < sub_diliverys + 3: sub_diliverys = team_array[team-1]
        delivery = delivery.iloc[:sub_diliverys,:team]

        used_pizza = delivery.values
        
        # add team size collumn
        delivery.insert(0, "size", team, True)
        
        # combine dfs
        output_file = pd.concat([output_file,delivery])                
        
        
        # create an array with all used pizzas 
        used_pizza = np.concatenate(used_pizza[:len(used_pizza)], axis=0)
        pizza_df = pizza_df.drop(used_pizza) # drop all pizzas by used_pizza(used pizzas)        
        team_array[team-1] -= sub_diliverys # remove all deliverd teams

        if len(pizza_df) < 2: break # Termination criterion: if less than 2 rows left
        

    # transform to an one dimensional string and add the amount of subdelivery
    output_file = output_file.fillna(-1)
    number_subdeli = str(len(output_file)) + ('\n')
    output_file = output_file.astype(np.int32)
    output_file = output_file.to_string(index=False,header=False)
    output_file = output_file.replace('-1', '') 
    output_file = number_subdeli + output_file
    
    with open('Google_hashcode2021/output/c.out', "w") as save_file:
        save_file.write(str(output_file))
    get_runtime('object2int')
            
    return

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

# get all ingredients
#inrgredients = get_ingre(pizza_df) 

#output_file = create_delivery1(pizza_df, team_array)
output_file = create_delivery2(pizza_df, team_array,input)





get_runtime('object2int')

print(pizza_df)



