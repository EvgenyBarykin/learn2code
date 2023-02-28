import pandas as pd

# first type of data in pandas - Series
s1 = pd.Series([1,2,3])
s2 = pd.Series(['okok','mama','tutu'])

print(s1)

# second type of data in pandas - DataFrame: collection of series objects
s3 = pd.DataFrame({'number': s1, 'nonsense':s2})
 
print(s3)