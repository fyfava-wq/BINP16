# BINP16 — Lecture 9: Fundamentals of Artificial Intelligence
## Git Cheat Sheet

A beginner-friendly summary of the lecture slides, Python demonstration script, and `AI_exercise.ipynb`.

---

## 1. AI, machine learning, and deep learning

- **Artificial Intelligence (AI):** broad field of systems that perform tasks associated with human intelligence.
- **Machine Learning (ML):** a subset of AI where models learn patterns from data.
- **Deep Learning (DL):** a subset of ML using neural networks with multiple processing layers.

Relationship: **DL ⊂ ML ⊂ AI**

### Main types of machine learning

| Type | What the model receives | Goal | Example |
|---|---|---|---|
| Supervised learning | Features `X` and known target `y` | Predict the target for new samples | Predict disease status |
| Unsupervised learning | Features `X`, without target labels for the learning task | Discover patterns or groups | Cluster gene-expression profiles |

For supervised learning, the target determines the task:

- **Regression:** predict a numerical/continuous value, e.g. a susceptibility score.
- **Classification:** predict a category/class, e.g. `0 = no disease`, `1 = disease`.

## 2. Training data: `X` and `y`

- `X`: input features/predictors, such as gene-expression measurements.
- `y`: known target/response, such as a numerical score or disease class.
- Rows represent samples/individuals; columns in `X` represent features.
- Keep the rows in `X` and `y` in the same order.

```python
# Example: 4 samples, 2 features per sample
X = [
    [2.0, 3.0],
    [4.0, 5.0],
    [6.0, 7.0],
    [8.0, 9.0]
]

# One known numerical target per sample
y = [25, 40, 60, 75]
```

General supervised-learning workflow:

1. Prepare the feature matrix `X` and target `y`.
2. Split data into training and test sets when evaluating predictive performance.
3. Fit the model using training data.
4. Predict targets for unseen samples.
5. Evaluate predictions using suitable metrics.

## 3. Correlation is not causation

Correlation describes the **strength and direction** of a relationship between two variables.

- `r > 0`: positive correlation; variables tend to increase together.
- `r < 0`: negative correlation; one tends to decrease as the other increases.
- `r ≈ 0`: no clear *linear* relationship.
- **Correlation does not necessarily imply causation.** Two variables changing together does not prove that one causes the other.

## 4. Regression

Regression predicts a numerical target.

### Simple linear regression

One feature is used to predict one numerical outcome:

\[
\hat{y} = w_1 x_1 + b
\]

- `x₁`: input feature/predictor.
- `w₁`: weight, coefficient, or slope.
- `b`: intercept or bias.
- `ŷ`: predicted outcome.

The fitted line minimises the sum of squared vertical prediction errors (residuals) in ordinary least-squares linear regression.

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([12, 19, 32, 38, 51, 57, 72, 79])

model = LinearRegression()
model.fit(X, y)

print(model.coef_)       # learned weight(s)
print(model.intercept_)  # bias/intercept
y_pred = model.predict(X)

# Predict for one new sample: one row, one feature
print(model.predict(np.array([[5.5]])))
```

**Important:** scikit-learn expects `X` to be a 2D table, even when there is only one feature. Use `.reshape(-1, 1)` for a one-dimensional list/array of feature values.

### Multiple linear regression

Use several features to predict one numerical outcome:

\[
\hat{y} = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b
\]

```python
X = np.array([
    [1, 4],
    [2, 2],
    [3, 5],
    [4, 3]
])
y = np.array([12, 19, 32, 38])

model = LinearRegression()
model.fit(X, y)

# New sample has two features, in the same column order as training X
new_sample = np.array([[5.5, 6]])
print(model.predict(new_sample))
```

`model.coef_` contains one coefficient per feature; `model.intercept_` is the fitted intercept.

## 5. Classification

Classification predicts a category/class rather than a continuous number.

### Logistic regression

Despite its name, logistic regression is used for classification. It estimates class probabilities and predicts a class.

```python
import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([
    [1, 4],
    [2, 2],
    [3, 5],
    [4, 3],
    [5, 7],
    [6, 4],
    [7, 8],
    [8, 6]
])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

new_sample = np.array([[5.5, 6]])
print(model.predict(new_sample))             # predicted class
print(model.predict_proba(new_sample))       # probability for each class
print(model.predict_proba(new_sample)[0, 1]) # probability of class 1
```

### Other algorithms mentioned in the lecture

| Algorithm | Basic idea / use |
|---|---|
| Decision tree | Learns feature-based splitting rules and leaf predictions |
| Random forest | Combines predictions from many decision trees |
| Gradient boosting | Builds a sequence of models that progressively improve predictions |
| Support Vector Machine (SVM) | A supervised algorithm used for classification (and some regression tasks) |
| Naive Bayes | Probabilistic classification method |
| Artificial neural network (ANN) | Learns weights and biases across connected neurons |
| Deep neural network | Neural network with multiple processing layers |
| K-means | Unsupervised clustering into a chosen number of groups |
| PCA | Unsupervised dimensionality reduction; creates principal-component coordinates |

### Common Python ML packages

- **scikit-learn:** regression, classification, clustering, preprocessing, and evaluation.
- **PyTorch:** building, training, and evaluating neural networks.
- **TensorFlow:** developing deep-learning models.
- **XGBoost:** gradient-boosted decision trees for regression and classification.

## 6. Preparing and scaling data

Features can have very different numeric scales. A high-variance feature may dominate methods such as PCA if the data is not scaled.

### StandardScaler

Standardisation transforms each feature to approximately mean `0` and standard deviation `1`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

**For predictive modelling:** split the data first, fit the scaler on training features only, and use that fitted scaler to transform validation/test features. This helps prevent data leakage.

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # do not fit again on test data
```

- `test_size=0.2`: 20% test set, 80% training set.
- `random_state=42`: makes the random split reproducible.
- `stratify=y`: helps preserve class proportions in the splits; use for classification when appropriate.

## 7. Unsupervised clustering: K-means

K-means groups samples into a chosen number of clusters based on feature similarity. It does **not** use known target labels to form the clusters.

Example workflow from `AI_exercise.ipynb`:

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("gene_expression_data.csv")

# Ensure X contains numeric features only, not labels or metadata
X = df.select_dtypes(include="number").to_numpy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init="auto")
cluster_labels = kmeans.fit_predict(X_scaled)
```

- `n_clusters=3`: request three clusters.
- `fit_predict(...)`: fits K-means and returns a cluster assignment for each sample.
- Cluster numbers are arbitrary identifiers; cluster `0` is not automatically a biological class.
- Compare clusters with known labels only after clustering, to help interpret the results.

## 8. Dimensionality reduction: PCA

**Principal Component Analysis (PCA)** creates new coordinates (principal components) that capture directions of high variance. It is unsupervised: target labels are not used to fit PCA.

PCA is useful for visualising many measurements in two dimensions, but it does not itself predict a diagnosis.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(pca.explained_variance_ratio_)
```

- `n_components=2`: retain two components, often called PC1 and PC2.
- `X_pca`: each sample's coordinates along those two components.
- `explained_variance_ratio_`: fraction of variance explained by each retained component. The two values need not add up to `1`, because other components were omitted.
- PCA maximises captured variance; it does **not** guarantee that classes will separate clearly.

### Visualise PCA coordinates

```python
import matplotlib.pyplot as plt

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA")
plt.show()
```

To colour the plot by known labels, use the labels only for plotting—not as PCA input.

### Why scaling matters for PCA

The lecture's synthetic example compares PCA with and without `StandardScaler`. One irrelevant feature has a much larger variance than the other eight features. Without scaling, this feature can dominate the principal components. Scaling places features on comparable variance scales, so the other features can contribute meaningfully.

## 9. Evaluate classification

Always compare predicted labels against known labels from data not used to fit the model when measuring test performance.

### Confusion matrix

For binary classification with labels ordered `[0, 1]`, scikit-learn's confusion matrix is:

\[
\begin{bmatrix}
TN & FP \\
FN & TP
\end{bmatrix}
\]

- **TP (true positive):** positive case correctly predicted positive.
- **TN (true negative):** negative case correctly predicted negative.
- **FP (false positive):** negative case incorrectly predicted positive.
- **FN (false negative):** positive case incorrectly predicted negative.

Check which class is defined as “positive” in the dataset. The lecture's breast-cancer example uses `0 = malignant`, `1 = benign`, while another exercise uses `1 = disease`.

### Main metrics

| Metric | Formula | Meaning |
|---|---|---|
| Accuracy | `(TP + TN) / (TP + TN + FP + FN)` | Fraction of all predictions that are correct |
| Precision | `TP / (TP + FP)` | Of predicted positives, how many are truly positive? |
| Recall / sensitivity | `TP / (TP + FN)` | Of actual positives, how many were found? |
| Specificity | `TN / (TN + FP)` | Of actual negatives, how many were correctly identified? |

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, confusion_matrix
)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

tn, fp, fn, tp = confusion_matrix(
    y_true, y_pred, labels=[0, 1]
).ravel()
specificity = tn / (tn + fp)
```

**ROC curve and AUC**
- ROC plots true-positive rate against false-positive rate over classification thresholds.
- AUC summarises ranking discrimination; `0.5` corresponds to random ranking, and `1.0` to perfect ranking.
- Use probabilities for the class you intend to treat as positive, and make `pos_label` consistent with that choice.

## 10. Neural networks and activation functions

A neural network learns weights and biases between connected neurons. An activation function transforms a neuron's weighted input `z`.

| Function | General behaviour |
|---|---|
| Sigmoid | Maps values to the interval `(0, 1)` |
| Tanh | Maps values to `(-1, 1)` |
| ReLU | Returns `0` for negative input and `z` for positive input |
| Leaky ReLU | Uses a small negative slope instead of zero for negative input |
| ELU | Smoothly maps negative values toward `-1` (with `alpha=1`) and returns `z` for positive input |
| Linear / identity | Returns the input unchanged; useful for continuous regression outputs |

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh(z):
    return np.tanh(z)

def relu(z):
    return np.maximum(0, z)

def leaky_relu(z):
    return np.where(z > 0, z, 0.01 * z)

def elu(z):
    return np.where(z > 0, z, np.exp(z) - 1)

def linear(z):
    return z
```

### PyTorch workflow in the exercise notebook

The notebook demonstrates a neural-network classification workflow:

1. Read expression data and metadata.
2. Add/encode the group labels (e.g. with `LabelEncoder`).
3. Split into training, validation, and test sets.
4. Create a custom `torch.utils.data.Dataset`.
5. Create `DataLoader` objects for batches and shuffling.
6. Define a model by subclassing `torch.nn.Module`.
7. Choose a loss function and optimiser.
8. Train over epochs; monitor validation loss and use early stopping.
9. Plot training and validation loss.
10. Evaluate the selected model on the test set.

- **Training set:** used to update model parameters.
- **Validation set:** used to monitor performance and make model-selection decisions.
- **Test set:** held back for final evaluation.
- **Epoch:** one pass through the training dataset.
- **Batch:** a subset of training samples processed together.
- **Early stopping:** stop training when validation performance no longer improves, helping limit overfitting.

## 11. Common mistakes to avoid

- **Wrong task:** regression predicts a number; classification predicts a class.
- **Wrong shape:** `scikit-learn` expects `X` shaped `(n_samples, n_features)`. For one feature, use `reshape(-1, 1)`.
- **Target leakage:** do not include the target column in `X`.
- **Data leakage:** do not fit preprocessing steps on test data.
- **Using labels in unsupervised learning:** K-means and PCA should fit on features only; labels may be used later for comparison or plot colouring.
- **Unscaled features:** large numeric scales can dominate PCA and distance-based clustering.
- **Misreading class labels:** confirm what `0` and `1` mean before interpreting confusion matrices or ROC/AUC.
- **Overinterpreting tiny examples:** the lecture's small or synthetic demonstrations are for learning syntax and concepts, not for clinical conclusions.

## 12. Quick algorithm chooser

| Question | Suitable starting point |
|---|---|
| Predict a continuous score from labelled examples | Linear regression |
| Predict a category from labelled examples | Logistic regression, random forest, SVM, Naive Bayes |
| Find groups without known labels | K-means |
| Visualise high-dimensional measurements in 2D | PCA |
| Build a neural-network model | PyTorch or TensorFlow |

---

## Source materials

This cheat sheet is based on the uploaded **Fundamentals of Artificial Intelligence** lecture PDF, the Python demonstration script, and `AI_exercise.ipynb`. The examples are educational; synthetic susceptibility scores are not diagnostic evidence, and the notebook's breast-cancer dataset contains cell measurements rather than gene-expression measurements.
