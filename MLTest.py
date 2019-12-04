import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

filePath = "C:/Users/psion/Documents/psionEyeRecordings/mldata.csv"
eyeData = pd.read_csv(filePath)

features = ['Average peak velocity of saccades','Average peak velocity of saccades',
       'Minimum peak velocity of saccades',
       'Maximum peak velocity of saccades',
       'Standard deviation of peak velocity of saccades',
       'Average amplitude of saccades', 'Minimum amplitude of saccades',
       'Maximum amplitude of saccades']

y = eyeData['TEST']

X = eyeData[features]

trainX, testX, trainy, testy = train_test_split(X, y, random_state = 0)

eyeModel = DecisionTreeRegressor(random_state=1)
eyeModel.fit(trainX, trainy)
