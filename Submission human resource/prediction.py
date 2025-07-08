import pandas as pd 
import joblib

# Muat model terbaik (pipeline) yang telah disimpan
MODEL_PATH = 'attrition_rf_model_bundle.pkl'
model_bundle = joblib.load(MODEL_PATH)
preprocessor = model_bundle['preprocessor']
model = model_bundle['model']
# === Hardcoded input values ===
# Ganti nilai di bawah sesuai skenario yang diinginkan
# Pastikan mencakup kolom yang dipakai pipeline: EmployeeId, EmployeeCount, StandardHours, Over18

data = pd.DataFrame({
    'Age': [35],
    'BusinessTravel': ['Travel_Rarely'],
    'DailyRate': [800],
    'Department': ['Sales'],
    'DistanceFromHome': [5],
    'Education': [3],
    'EducationField': ['Life Sciences'],
    'EmployeeCount': [1],            # default 1
    'EnvironmentSatisfaction': [2],
    'Gender': ['Male'],
    'HourlyRate': [100],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobRole': ['Sales Executive'],
    'JobSatisfaction': [3],
    'MaritalStatus': ['Married'],
    'MonthlyIncome': [5000],
    'MonthlyRate': [15000],
    'NumCompaniesWorked': [2],
    'Over18': ['Y'],                # default Y
    'OverTime': ['Yes'],
    'PercentSalaryHike': [15],
    'PerformanceRating': [3],
    'RelationshipSatisfaction': [3],
    'StandardHours': [80],           # constant 80
    'StockOptionLevel': [1],
    'TotalWorkingYears': [10],
    'TrainingTimesLastYear': [3],
    'WorkLifeBalance': [4],
    'YearsAtCompany': [5],
    'YearsInCurrentRole': [3],
    'YearsSinceLastPromotion': [1],
    'YearsWithCurrManager': [3]
})

X_input = preprocessor.transform(data)


pred = model.predict(X_input)

prediction = "Yes" if pred[0] == 1 else "No"
print(f"Will this employee attrit? ➜ {prediction}")
