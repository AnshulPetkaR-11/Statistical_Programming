# **Diabetes Prediction System**

### **Basic Information**
- **Practical Name:** SPL Lab 7  
- **Name:** Anshul Petkar  
- **Roll No:** 05  
- **Section/Batch:** B4 / B1  

---

### **Project Description**
This project is a machine learning–based system designed to predict whether a patient has diabetes.  
It analyzes health factors like **Glucose levels, Blood Pressure, BMI, and Age** to provide a result: **“Diabetic”** or **“Non-Diabetic.”**

---

### **Workflow & Steps**
- **Data Analysis:** Used **Pandas** to load the dataset and **Seaborn/Matplotlib** for visualizations (heatmaps, boxplots).  
- **Data Cleaning:** Removed outliers using the **Interquartile Range (IQR)** method to improve data quality.  
- **Data Preprocessing:** Handled imbalanced data with **SMOTE** and normalized features using **StandardScaler**.  
- **Model Building:** Tested five algorithms:  
  - Logistic Regression  
  - Decision Tree  
  - Random Forest  
  - Support Vector Machine (SVM)  
  - K-Nearest Neighbors (KNN)  
- **Best Model:** **Support Vector Machine (SVM)** gave the best performance.  
- **Deployment:** Built a user-friendly web interface using **Gradio** where users can input data and get instant predictions.  

---

### **Technology Stack**
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, Gradio  
- **Platform:** Google Colab
