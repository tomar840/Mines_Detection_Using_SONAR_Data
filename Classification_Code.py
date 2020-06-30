import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
from google.colab import files
import io

#To upload dataset from local drive to colab
#uploaded = files.upload()
raw_data = pd.read_csv(io.BytesIO(uploaded["sonar.csv"]), header = None)
x = raw_data[raw_data.columns[0:60]].values
y = list(raw_data[[60]].values)

#Converting 'R' & 'M' to 0 & 1
y = [0 if x == 'R' else 1 for x in y]

def Get_Accuracy(model, x_,y_, num_com):
  pca = PCA(n_components=num_com)
  #pca.fit(x)
  x_reduced = pca.fit_transform(x_)
  pca_var = sum(pca.explained_variance_ratio_)

  ##Splitting training and test data
  x_train, x_test, y_train, y_test = train_test_split(x_reduced, y_, test_size = 0.3, shuffle = True)

  model.fit(x_train, y_train)
  test_acc = model.score(x_test, y_test)
  #print(test_accuracy)
  return [pca_var, test_acc]

#RandomForestClassifier Model 
model = RandomForestClassifier()
pca_var_  = []
test_acc_ = []

for i in range(1,61):
  pca_var,test_acc = Get_Accuracy(model,x,y,i)
  pca_var_.append(pca_var)
  test_acc_.append(test_acc)

p = [i for i in range(1,61)]
plt.plot(p,pca_var_)
plt.xlabel("No. of features considered in PCA")
plt.ylabel("Explained Variance by PCA")
plt.show()

plt.plot(p,test_acc_)
plt.xlabel("No. of features considered in PCA")
plt.ylabel("Accuracy of reduced features in RandomForrest Model")
plt.show()

#LinearRegression Model 
model = LinearRegression()
pca_var_  = []
test_acc_ = []

for i in range(1,61):
  pca_var,test_acc = Get_Accuracy(model,x,y,i)
  pca_var_.append(pca_var)
  test_acc_.append(test_acc)

p = [i for i in range(1,61)]
plt.plot(p,pca_var_)
plt.xlabel("No. of features considered in PCA")
plt.ylabel("Explained Variance by PCA")
plt.show()

plt.plot(p,test_acc_)
plt.xlabel("No. of features considered in PCA")
plt.ylabel("Accuracy of reduced features in LinearRegression Model")
plt.show()

#LogisticRegression Model 
model = LogisticRegression()
pca_var_  = []
test_acc_ = []

for i in range(1,61):
  pca_var,test_acc = Get_Accuracy(model,x,y,i)
  pca_var_.append(pca_var)
  test_acc_.append(test_acc)

p = [i for i in range(1,61)]
plt.plot(p,pca_var_)
plt.xlabel("No. of features considered in PCA")
plt.ylabel("Explained Variance by PCA")
plt.show()

plt.plot(p,test_acc_)
plt.xlabel("No. of features considered in PCA")
plt.ylabel("Accuracy of reduced features in LogisticRegression Model")
plt.show()