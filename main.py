import parsejson,mysql_databse,getData

data = parsejson.get_data("json/hospital.json")
patients_sql = "INSERT INTO Patients (patient_id, name, age, sex) VALUES (%s, %s, %s, %s)"
physician_sql = "INSERT INTO physician (id, name, specialist) VALUES (%s, %s, %s)"

data_patients = getData.patients(data)
data_physician = getData.physicians(data)
print(data_physician)
mysql_databse.insert(patients_sql,data_patients)
mysql_databse.insert(physician_sql,data_physician)

