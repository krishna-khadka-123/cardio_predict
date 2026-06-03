import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('Cardiovascular_Disease.csv')

df['age']=df['age']/365

df_sample = df[
    (df['ap_hi'] >= 100) & (df['ap_hi'] <= 190) &
    (df['ap_lo'] >= 50) & (df['ap_lo'] <= 99)
]


def cardio_predict():
  features = ['age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 
            'alco', 'active']
  target = 'cardio'
  X=df_sample[features]
  Y=df_sample[target]
  X_train,X_test,Y_train,Y_test=train_test_split(
    X,Y,random_state=42,test_size=0.2,stratify=Y
    )
  scaler=StandardScaler()
  X_train_scale=scaler.fit_transform(X_train)
  X_test_scale=scaler.transform(X_test)
  
  model = LogisticRegression(
    solver='lbfgs',
    class_weight='balanced',
    random_state=42,
    max_iter=1000
    )
  model.fit(X_train_scale,Y_train)
  Y_pred=model.predict(X_test_scale)
  cr=classification_report(Y_test,Y_pred)
  cm=confusion_matrix(Y_test,Y_pred)
  
  return features,target,X,Y,scaler,model,Y_pred,cr,cm



