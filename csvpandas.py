import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

csv_dataframe = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')

X = csv_dataframe.drop(['logS'], axis=1)
Y = csv_dataframe.iloc[:,-1]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, Y_train)

Y_lr_train_pred = lr.predict(X_train)
Y_lr_test_pred = lr.predict(X_test)

lr_train_mse = mean_squared_error(Y_train, Y_lr_train_pred)
lr_train_r2 = r2_score(Y_train, Y_lr_train_pred)
lr_test_mse = mean_squared_error(Y_test, Y_lr_test_pred)
lr_test_r2 = r2_score(Y_test, Y_lr_test_pred)

print("Ok mf you can run")
print(lr_train_mse)
