import io
import pandas as pd

# read the text as a string
ttext = '5 1 2 1 \n3 onion pepper olive\n3 mushroom tomato basil\n3 chicken mushroom pepper\n3 tomato mushroom basil\n2 chicken basil\n'

# read the string as a DataFrame using '\n' as the delimiter
df = pd.read_csv(io.StringIO(text), header=None, sep='\n')

# convert the DataFrame to a list of ASCII values
df = df.applymap(ord)
