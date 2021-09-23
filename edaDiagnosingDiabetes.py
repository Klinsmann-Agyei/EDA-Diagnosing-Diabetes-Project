import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv("diabetes.csv")

print(diabetes_data.head())
print(diabetes_data.shape)
print(diabetes_data.isnull().sum())
print(diabetes_data.describe())
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
print(diabetes_data.info())