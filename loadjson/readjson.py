import pandas as pd
from JSONLoader import JSONLoader

# enter your file location here
fileLocation = 'C:/DataSets/YelpDataSet/yelp_dataset/'
datefilename = 'yelp_academic_dataset_tip.json'

# use the JSONLoader class to load the data
jl = JSONLoader(fileLocation)
dataframes = jl.getDataframe(datefilename)

# print the shape and info of the dataframe
print('DataFrame Shape', dataframes.shape)
print('DataFrame Info', dataframes.info())
