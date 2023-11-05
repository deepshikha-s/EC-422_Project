# -*- coding: utf-8 -*-
"""Heart Disease Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VTzBS3SIfZqsK_hPglH75rTPNHmmC-QO
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')
df.head()

df.describe()

df.info()

df.shape

"""# Data visualization
### Sex (Gender)
"""

labels=['Female', 'Male']
order=df['sex'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Sex (Gender) Distribution')

# subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['sex'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))

# subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax=sns.countplot(x='sex',data=df,order=order)
plt.xlabel('Gender')
plt.ylabel('Total')
countplt

"""### CP (Chest Pain Types)"""

labels=['Type 0', 'Type 2', 'Type 1', 'Type 3']
order=df['cp'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Chest Pain Type Distribution')

# subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['cp'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))

# subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='cp',data=df,order=order)
plt.xlabel('Pain Type')
plt.ylabel('Total')
countplt

"""fbs (Fasting Blood Sugar)"""

labels=['< 120 mg/dl', '> 120 mg/dl']
order=df['fbs'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Fasting Blood Sugar Distribution')

# subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['fbs'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))


# subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='fbs',data=df,order=order)
plt.xlabel('Fasting Blood Sugar')
plt.ylabel('Total')
countplt

"""restecg (Resting Electrocardiographic Results)"""

labels=['1', '0', '2']
order=df['restecg'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Resting Electrocardiographic Distribution')

#subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['restecg'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))

#subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='restecg',data=df,order=order)
plt.xlabel('Resting  Electrocardiographic')
plt.ylabel('Total')
countplt

"""### exang (Exercise Induced Angina)"""

labels=['False', 'True']
order=df['exang'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Exercise Induced Angina Distribution')

#subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['exang'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))

#Subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='exang',data=df,order=order)
plt.xlabel('Exercise Induced Angina')
plt.ylabel('Total')
countplt

"""### slope (Slope of the Peak Exercise)"""

labels=['2', '1', '0']
order=df['slope'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Slope of the Peak Exercise Distribution')

# Subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['slope'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))


#Subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='slope',data=df,order=order)
plt.xlabel('Slope')
plt.ylabel('Total')
countplt

"""### ca (Number of Major Vessels)"""

labels=['0', '1', '2', '3', '4']
order=df['ca'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Number of Major Vessels Distribution')

# Subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['ca'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))

#Subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='ca',data=df,order=order)
plt.xlabel('Number of Major Vessels')
plt.ylabel('Total')
countplt

"""### thal"""

labels=['2', '3', '1', '0']
order=df['thal'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('"thal" Distribution')

# Subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['thal'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))

#Subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='thal',data=df,order=order)
plt.xlabel('Number of "thal"')
plt.ylabel('Total')
countplt

"""### target (Heart Disease Status)"""

labels=['True', 'False']
order=df['target'].value_counts().index

plt.figure(figsize= (16,8))
plt.suptitle('Heart Diseases Distribution')

# Subplot 1
plt.subplot(1,2,1)
plt.title('Pie Chart')
plt.pie(df['target'].value_counts(),labels=labels, autopct='%.2f%%', wedgeprops=dict(alpha=0.8))

#Subplot 2
countplt = plt.subplot(1,2,2)
plt.title('Histogram')
ax= sns.countplot(x='target',data=df,order=order)
plt.xlabel('Heart Disease Status')
plt.ylabel('Total')
countplt

"""## Heart Disease Distribution based on Gender"""

labels = ['False', 'True']
label_gender = np.array([0, 1])
label_gender2 = ['Male', 'Female']

# Bar Chart
ax = pd.crosstab(df.sex, df.target).plot(kind='bar', figsize=(8, 5))

for rect in ax.patches:
    width, height = rect.get_width(), rect.get_height()
    x, y = rect.get_xy()
    ax.text (x+width/2, y+height/2,'{:.0f}'.format(height), horizontalalignment='center',verticalalignment='center', fontsize=10)

plt.suptitle('Heart Disease Distribution based on Gender', fontsize='16')
plt.xlabel('Gender (Sex)')
plt.ylabel('Total')

plt.xticks(label_gender, label_gender2, rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.legend(labels=labels, title='Target', fontsize='8', title_fontsize='9', loc='upper left', frameon=True);

"""Females tend to have heart diseases more frequently compared to males. In males, the distribution is more imbalanced compared to females.

## Heart Disease Distribution Based on Major Vessels Total
"""

labels = ['False', 'True']

# --- Creating Horizontal Bar Chart ---
ax = pd.crosstab(df.ca, df.target).plot(kind='barh', figsize=(8, 5))

for rect in ax.patches:
    width, height = rect.get_width(), rect.get_height()
    x, y = rect.get_xy()
    ax.text (x+width/2, y+height/2, '{:.0f}'.format(width), horizontalalignment='center', verticalalignment='center')
plt.suptitle('Heart Disease Distribution based on Major Vessels Total',fontsize='16')

plt.xlabel('Total')
plt.ylabel('Number of Major Vessels')

plt.yticks(rotation=0)
plt.grid(axis='x', alpha=0.2)
plt.grid(axis='y', alpha=0)
plt.legend(labels=labels, title='Target', fontsize='8', frameon=True,title_fontsize='9', loc='upper right');

"""## Heart Disease Scatter Plot Based on Age"""

plt.figure(figsize=(10, 8))
plt.suptitle('Heart Disease Scatter Plot based on Age',fontsize='16')
plt.scatter(x=df.age[df.target==0], y=df.thalach[(df.target==0)])
plt.scatter(x=df.age[df.target==1], y=df.thalach[(df.target==1)])

plt.legend(['False', 'True'], title='Target', fontsize='7', title_fontsize='8', loc='upper right', frameon=True)

plt.xlabel('Age')
plt.ylabel('Max. Heart Rate')
plt.ticklabel_format(style='plain', axis='both')
plt.grid(axis='both', alpha=0.5)
plt.show();

"""## Heart Disease Distribution Based on Fasting Blood Sugar"""

labels = ['False', 'True']
label_gender = np.array([0, 1])
label_gender2 = ['< 120 mg/dl', '> 120 mg/dl']

# --- Creating Bar Chart ---
ax = pd.crosstab(df.fbs, df.target).plot(kind='bar', figsize=(8, 5))

# --- Bar Chart Settings ---
for rect in ax.patches:
    width, height = rect.get_width(), rect.get_height()
    x, y = rect.get_xy()
    ax.text (x+width/2, y+height/2, '{:.0f}'.format(height),horizontalalignment='center', verticalalignment='center')

plt.suptitle('Heart Disease Distribution based on Fasting Blood Sugar',fontsize='16')

plt.xlabel('Fasting Blood Sugar')
plt.ylabel('Total')
plt.xticks(label_gender, label_gender2, rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.legend(labels=labels, title='Target', fontsize='8', title_fontsize='9', loc='upper left', frameon=True);

"""The number of patients with low fasting blood sugar is higher compared to patients with high fasting blood sugar. In low fasting blood sugar, patients tend to have heart diseases. Also, the distribution of heart diseases patients with high fasting blood sugar is equally distributed."""

df.head()

"""# Data Preprocessing

## One-Hot Encoding
"""

# categorical columns
cp = pd.get_dummies(df['cp'],prefix= 'cp')
thal = pd.get_dummies(df['thal'],prefix = 'thal')
slope = pd.get_dummies(df['slope'],prefix = 'slope')

frames = [df,cp,thal,slope]
df = pd.concat(frames,axis=1)

df['cp_1'] = df['cp_1'].astype(int)
df['cp_2'] = df['cp_2'].astype(int)
df['cp_3'] = df['cp_3'].astype(int)
df['thal_0'] = df['thal_0'].astype(int)
df['thal_1'] = df['thal_1'].astype(int)
df['thal_2'] = df['thal_2'].astype(int)
df['thal_3'] = df['thal_3'].astype(int)
df['slope_0'] = df['slope_0'].astype(int)
df['slope_1'] = df['slope_1'].astype(int)
df['slope_2'] = df['slope_2'].astype(int)


#Dropping the unnecessory variables
df=df.drop(columns = ['cp','thal','slope'])
df.head()

#missing values
df.isnull().sum()

df.isna()

df1 = df.dropna()
df1.head()

df1.describe()

df1.corr()

plt.figure(figsize= (16,8))
ax = sns.heatmap(df1.corr(), annot=True)

df1.drop(df1['fbs'], inplace=True)

"""# Distribution Plots"""

sns.kdeplot(df['age'])

sns.kdeplot(df['trestbps'])

sns.kdeplot(df['chol'])

sns.kdeplot(df['thalach'])

sns.kdeplot(df['sex'])

"""# Box Plots"""

from sklearn.preprocessing import MinMaxScaler
X = df.drop(['target'],axis=1)
X = MinMaxScaler().fit_transform(X)

sns.boxplot(y='age', data=df1)

sns.boxplot(y='trestbps', data=df1)

sns.boxplot(y='chol', data=df1)

sns.boxplot(y='thalach', data=df1)

sns.boxplot(y='oldpeak', data=df1)

# Removing outliers

"""# Logistic Regression"""

df_log = df1

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix,mean_squared_error,roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = df_log.drop('target', axis=1)
y = df_log['target']
print(df.shape, X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# building roc curve
y_true = y_test  # True labels (actual target values)
y_prob = model.predict_proba(X_test)[:, 1]  # Predicted probabilities for the positive class


# Calculate the AUC (Area Under the Curve)
roc_auc = roc_auc_score(y_true, y_prob)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

print(f"Accuracy percentage: {accuracy * 100:.2f}%")
print(f"Accuracy: {accuracy}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"roc_auc: {roc_auc}")

# Display a classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Display a confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

"""# Naive Bayes Classifier"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, auc

df_naive = df1

X = df_naive.drop('target', axis=1)
y = df_naive['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

nb_classifier = GaussianNB()

nb_classifier.fit(X_train, y_train)

y_pred = nb_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
confusion_matrix_result = confusion_matrix(y_test, y_pred)
classification_report_result = classification_report(y_test, y_pred)

fpr, tpr, thresholds = roc_curve(y_test, nb_classifier.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)

precision, recall, _ = precision_recall_curve(y_test, nb_classifier.predict_proba(X_test)[:, 1])
pr_auc = auc(recall, precision)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:\n', confusion_matrix_result)
print('Classification Report:\n', classification_report_result)
print('ROC AUC:', roc_auc)
print('Sensitivity (True Positive Rate):', sensitivity)
print('Specificity (True Negative Rate):', specificity)
print('Precision-Recall AUC:', pr_auc)

"""# K Nearest Neighbors"""

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, auc

df_knn = df1

X = df_knn.drop('target', axis=1)
y = df_knn['target']

# Define a list of k values to test
k_values = [3, 5, 7]

# Create a dictionary to store the results for each k
results = {}

# Perform cross-validation and evaluation for each value of k
for k in k_values:
    # Create a KNN classifier
    knn_classifier = KNeighborsClassifier(n_neighbors=k)

    # Perform cross-validation with 5 folds
    cross_val_scores = cross_val_score(knn_classifier, X, y, cv=5)
    mean_score = cross_val_scores.mean()

    # Split the dataset for final evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    knn_classifier.fit(X_train, y_train)  # Corrected line
    y_pred = knn_classifier.predict(X_test)

    # Calculate additional metrics
    accuracy = accuracy_score(y_test, y_pred)
    confusion_matrix_result = confusion_matrix(y_test, y_pred)
    classification_report_result = classification_report(y_test, y_pred)

    # Calculate ROC curve and AUC
    fpr, tpr, thresholds = roc_curve(y_test, knn_classifier.predict_proba(X_test)[:, 1])
    roc_auc = auc(fpr, tpr)

    # Store the results in the dictionary
    results[k] = {
        "Cross-Validation Mean Score": mean_score,
        "Accuracy": accuracy,
        "Confusion Matrix": confusion_matrix_result,
        "Classification Report": classification_report_result,
        "ROC AUC": roc_auc,
    }

# Find the best k based on mean cross-validation score
best_k = max(results, key=lambda k: results[k]["Cross-Validation Mean Score"])

# Print the results for all values of k
for k in k_values:
    print(f'KNN (k={k})')
    print(f'Cross-Validation Mean Score: {results[k]["Cross-Validation Mean Score"]}')
    print(f'Test Set Accuracy: {results[k]["Accuracy"]}')
    print('Confusion Matrix:\n', results[k]['Confusion Matrix'])
    print('Classification Report:\n', results[k]['Classification Report'])
    print('ROC AUC:', results[k]['ROC AUC'])
    print('\n')

# Print the best k and its results
print(f'Best k: {best_k}')
print('Performance Metrics for the Best k:')
best_results = results[best_k]
print(f'Cross-Validation Mean Score: {best_results["Cross-Validation Mean Score"]}')
print(f'Test Set Accuracy: {best_results["Accuracy"]}')
print('Confusion Matrix:\n', best_results['Confusion Matrix'])
print('Classification Report:\n', best_results['Classification Report'])
print('ROC AUC:', best_results['ROC AUC'])

"""# Decision Trees and Random Forests"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df_dt = df1

y = df_dt['target'].iloc[2:]
X = df_dt.drop(df['target'])
print(df.shape, X.shape, y.shape)

X = df_dt.drop(['target'], axis=1)  # Exclude 'target'
y = df_dt['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")

from sklearn.ensemble import RandomForestClassifier

# Create a Random Forest classifier
rf_clf = RandomForestClassifier(n_estimators=1000, random_state=42)  # You can adjust the number of estimators as needed

# Fit the Random Forest classifier to the training data
rf_clf.fit(X_train, y_train)

# Make predictions on the test set
y_rf_pred = rf_clf.predict(X_test)

# Evaluate the Random Forest model
rf_accuracy = accuracy_score(y_test, y_rf_pred)
rf_report = classification_report(y_test, y_rf_pred)

print("Random Forest Classifier Results:")
print(f"Accuracy: {rf_accuracy}")
print(f"Classification Report:\n{rf_report}")

"""# Support Vector Machines"""

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df_svm = df1

X = df_svm.drop('target', axis=1)
y = df_svm['target']

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=42)

X_train.shape, X_test.shape

SVMmodel = SVC()

# Training SVM
SVMmodel.fit(X_train, y_train)

#Predicting y for test dataset
y_pred = SVMmodel.predict(X_test)

#Accuracy score
accuracy= accuracy_score(y_test, y_pred)

print("Support Vector Machine Model Accuracy:", accuracy)

"""# Artificial Neural Networks"""

from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

df_nn = df1

y = df_nn['target']
X = df_nn.drop('target', axis = 1)
print(df_nn.shape, X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

model = keras.Sequential([layers.Dense(units=4, activation='relu'), layers.Dense(units=3, activation='relu'), layers.Dense(units=1, activation='sigmoid')])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    batch_size=256,
    epochs=100
)

history_df = pd.DataFrame(history.history)
# Start the plot at epoch 5
history_df.loc[5:, ['loss', 'val_loss']].plot()
history_df.loc[5:, ['binary_accuracy', 'val_binary_accuracy']].plot()

print(("Best Validation Loss: {:0.4f}" +\
      "\nBest Validation Accuracy: {:0.4f}")\
      .format(history_df['val_loss'].min(),
              history_df['val_binary_accuracy'].max()))

#Predicting y for test dataset
preds = model.predict(X_test)
y_pred = [int(round(x[0])) for x in preds]
#Accuracy score
accuracy= accuracy_score(y_test, y_pred)

print("Neural Networks Accuracy:", accuracy)
roc_auc = roc_auc_score(y_test, y_pred)
print("ROC AUC: ", roc_auc)
mse = mean_squared_error(y_test, y_pred)
print(mse)

# Display a classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Display a confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))