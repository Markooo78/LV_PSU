import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score



# 1. UCITAVANJE PODATAKA
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

y = y.astype(int)

print("Broj uzoraka:", len(y))
print("Razdioba klasa:", np.bincount(y))



# 2. PODJELA PODATAKA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. MODEL – DECISION TREE
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# 4. PREDIKCIJA
y_pred = dt.predict(X_test)

# 5. EVALUACIJA

# matrica zabune
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.title("Matrica zabune - Decision Tree")
plt.show()

# metrike
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))

# 6. VIZUALIZACIJA STABLA
plt.figure(figsize=(12, 8))
plot_tree(dt, feature_names=feature_names, class_names=class_names, filled=True)
plt.title("Stablo odlučivanja")
plt.show()