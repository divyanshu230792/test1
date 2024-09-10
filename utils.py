import pickle
import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')
import config
import pandas as pd

class Medical_Insurance():
    def __init__(self):
        pass

    def __load_data(self):
        with open(config.MODEL_FILE_NAME,'rb') as f:
            self.model=pickle.load(f)

        with open(config.COLUMN_DATA,'r') as f:
            self.column_data=json.load(f)

        self.column_names = self.model.feature_names_in_
        self.feature_count= self.model.n_features_in_
    
    def prediction_charges(self,age, gender, bmi, children, smoker, region):
        self.__load_data()
        gender=self.column_data['gender'][gender]
        smoker=self.column_data['smoker'][smoker]
        region='region_'+region
        region_index=np.where(self.column_names==region)[0][0]
        test_array=np.zeros((1,self.feature_count))
        test_array[0,0]=age
        test_array[0,1]=gender
        test_array[0,2]=bmi
        test_array[0,3]=children
        test_array[0,4]=smoker
        test_array[0,region_index]=1
        pc=self.model.predict(test_array)[0]
        print("Predicted Charges :",pc)
        return pc


def load_dataset():
    df=pd.read_csv(config.CSV_FILE_NAME)
    return df