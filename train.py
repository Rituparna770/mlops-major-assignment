from sklearn.datasets import fetch_olivetti_faces
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = fetch_olivetti_faces()
X, y = data.data, data.target

# Split 70% train, 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'savedmodel.pth')
print("Model trained and saved as savedmodel.pth")
