# 📊 Customer Churn Prediction

This project helps predict whether a customer will **leave a service (churn)** based on their account details and usage behavior. It uses machine learning to help businesses take early action and improve customer retention.

---

## ✅ Objective

To build a predictive model that can identify customers who are likely to churn, so the company can take steps to retain them.

---

## 📁 Dataset

- **Source**: Telco Customer Churn dataset
- **Records**: ~7,000 customers
- **Target Variable**: `Churn` (Yes = will leave, No = will stay)

---

## 🧠 What I Did

1. **Data Preprocessing**
   - Removed unnecessary columns
   - Handled missing values
   - Converted categorical variables using one-hot encoding

2. **Imbalance Handling**
   - Used **SMOTE** to balance churn (Yes) and non-churn (No) cases

3. **Model Training**
   - Used **Decision Tree Classifier**
   - Trained on 80% of the data, tested on 20%

4. **Model Evaluation**
   - **Accuracy**: 77%
   - **F1 Score (Churn class)**: 0.60
   - **AUC Score**: 0.73
   - Evaluated with classification report and confusion matrix

5. **Model Deployment**
   - Saved the model using `joblib`
   - Built a **Streamlit app** for real-time prediction

---

## 🖥️ Streamlit App

A simple web interface where you can:
- Enter customer details manually
- Click "Predict Churn"
- Get a prediction: **Churn** or **No Churn**

---

## 🚀 How to Run the Project

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
````

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🧰 Tools & Libraries Used

* Python
* Pandas
* Scikit-learn
* imbalanced-learn (SMOTE)
* Streamlit
* Joblib

---

## 📌 Project Structure

```
customer-churn-prediction/
│
├── app.py                    # Streamlit app
├── decision_tree_model.pkl   # Saved ML model
├── model_features.pkl        # List of model features
├── churn_notebook.ipynb      # Jupyter notebook with full steps
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ✅ Conclusion

This project shows how machine learning can help businesses predict customer churn and take early action to improve customer satisfaction and reduce revenue loss.

---

## 🙋‍♀️ Author

**Pareenita Jain**
B.Tech (CSE), Data Science 




