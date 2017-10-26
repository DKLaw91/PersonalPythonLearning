https://www.learnpython.org/en/Pandas_Basics
______________________________________________________
pop={"Country": ["Brazil", "Russia", "India", "China", "South Africa"], 
  "Capital" : ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"], 
  "Area" : [8.516, 17.10, 3.286, 9.597, 1.221], 
  "Population" : [200.4, 143.5, 1252, 1357, 52.98]}

import pandas as pd

brics=pd.DataFrame(pop) # Converts dictionary to Data Frame
print(brics) # Prints Data Frame
print()
brics.index=['1','2','3','4','5'] # Changes index - can be anything
print(brics)
print()
print(brics['Capital']) # Prints out individual column as Data Frame
print()
print(brics[['Country', 'Capital', 'Area']]) # Prints out selected columns
print()
print(brics[0:2]) # Prints first 2 observations (rows)
print()
print(brics[2:4]) # Prints 3 & 4th observations (rows)
print()
print(brics.iloc[1]) #  Prints out row in reversed format
print()
print(brics.loc[['1', '2']]) # Prints 1st & 2nd observations (rows)
