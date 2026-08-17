import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from train_utils import DATA_FILE_PATH, MODEL_DIR, MODEL_PATH
import os
df = pd.read_csv(DATA_FILE_PATH)

df = df.drop_duplicates()
df = df.drop(['name', 'torque', 'mileage', 'engine', 'max_power'], axis = 1)

X = df.drop(['selling_price'], axis = 1)
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

num_cols = X_train.select_dtypes(include=['number']).columns.tolist()
cat_cols = [col for col in X_train.columns if col not in num_cols]


num_pipe = Pipeline(
    steps = [
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ]
)

cat_pipe = Pipeline(
    steps = [
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))  
    ]

)

preprocessor = ColumnTransformer(
    transformers = [
        ('num', num_pipe, num_cols),
        ('cat', cat_pipe, cat_cols)
    ]
)

preprocessor.fit_transform(X_train)
preprocessor.transform(X_test)


regressor = RandomForestRegressor(n_estimators = 100, random_state = 42, max_depth = 5)


rf_model = Pipeline(
    steps = [
        ('pre', preprocessor),
        ('reg', regressor)
    ]
)
# pipeline could be treated as last step in the pipeline
rf_model.fit(X_train, y_train)

os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(rf_model, MODEL_PATH)
