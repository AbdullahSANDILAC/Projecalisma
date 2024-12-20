import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

df= pd.read_csv("/kaggle/input/banana/banana_quality.csv",
 encoding='ISO-8859-1')

print("First 5 Rows of Data Set:")
print(df.head())

print("\nData Set Information:")
print(df.info())

print("\nNumber of Missing Values ​​in Dataset:")
print(df.isnull().sum())

print("\nNumber of Duplicate Rows in Dataset:")
print( df.duplicated().sum())

print("\nStatistical Properties of Data Set:")
print(df.describe())

print("\nTarget Variable Distribution:")
print(df['Quality'].value_counts( ))

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

model_list = [RandomForestClassifier(), LogisticRegression(), KNeighborsClassifier(), DecisionTreeClassifier()]

model_name_list=[]
model_acc=[]

plt.figure(figsize=(10,4))
cols= ["c", "brown", "green", "blue"]
cols2= ["c", "brown"]

plt.subplot(1, 2, 1)
x = df["Quality"].value_counts().index
y = df["Quality"].value_counts()
sns.barplot(x=x, y=y, palette=cols2)
plt.title("Target Variable Distribution (Column Graph)")
plt.xlabel("Quality")
plt.ylabel("Number")
plt.show()

plt.subplot(1,2,2)
plt.pie(x=df["Quality"].value_counts(),labels=df["Quality"].value_counts().index,
 shadow=True , explode=[0.02,0.02],startangle=30,autopct='%0.2f%%',colors=cols)
plt.legend(labels=["good","bad"],loc=(1,0.8 ),fontsize="small")
print(df.Quality.value_counts())
plt.title("Target Variable Distribution (Pie Chart)")
plt.tight_layout()
plt.show()



if df["Quality"].dtype == "object":
 le= LabelEncoder()
 df["Quality"] = le.fit_transform(df["Quality"])

scaler =StandardScaler()
df.iloc[:,:-1]=scaler.fit_transform(df.iloc[:,:-1])
print("iloc StandardScaler\n",df.iloc[::-1])

scalerminmax = MinMaxScaler()
df.iloc[:,:-1]=scalerminmax.fit_transform(df.iloc[:,:-1])
print("iloc MinMaxScaler\n",df.iloc[::-1])

X=df.drop(["Quality"],axis=1)
y=df["Quality"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)


for i in model_list:
 model=i.fit(X_train,y_train)
 model_name=model.__class__.__name__
 y_pred=model.predict(X_test)
 accuracy=accuracy_score(y_test,y_pred)
 model_name_list.append(model_name)
 model_acc.append(accuracy)
 print(f"{model_name},accuracy: {accuracy:.3f}\n")

model_data = pd.DataFrame({
 'Model': model_name_list,
 'Accuracy': model_acc
})

plt.figure(figsize=(8, 5))
sns.barplot(data=model_data, x='Model', y='Accuracy', palette=cols)
plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.title("Model Accuracy Comparison")
plt.show()

model_prediction = pd.DataFrame()

for model in model_list:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    model_prediction[model.__class__.__name__] = y_pred

prediction_data = model_prediction.melt(var_name="Model", value_name="Prediction")

plt.figure (figsize=(12, 6))
sns.countplot(data=prediction_data, x="Prediction", hue="Model", palette=cols)
plt.title("Differential Differences Between Models Comparison")
plt.xlabel("Predicted Classes")
plt.ylabel("Frequency")
plt.xticks(ticks=[0, 1], labels=["Bad", "Good"])
plt.legend(title ="Model")
plt.show()