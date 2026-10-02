import pandas as pd 

#load attendance data
file_path= "data/Attendance_July_September_2026_Final.xlsx"

df = pd.read_excel(file_path,sheet_name="Attendance_Data")

df["Date"]=pd.to_datetime(df["Date"])

print("\n=====BASIC INFORMATION=====")

print("Total records:",len(df))
print("Total students:",df["Roll_No"].nunique())
print("Date range:",df["Date"].min().date(),"to",df["Date"].max().date())

print("\n=====ATTENDANCE SUMMARY=====")

present_count = (df["Status"] == "P").sum()
absent_count = (df["Status"] == "A").sum()

total_records = len(df)

attendance_percentage = (present_count / total_records) * 100

print("Present: ",present_count)
print("Absent: ",absent_count)
print("Attendance percentage: ",round(attendance_percentage,2),"%")

print("\n=====STUDENT-WISE ATTENDANCE======")

student_summary = df.groupby("Roll_No")["Status"].value_counts().unstack(fill_value=0)

student_summary["Total"] = (student_summary.get("P",0) + student_summary.get("A",0))

student_summary["Attendance Percentage"] = (student_summary.get("P",0) / student_summary["Total"] * 100)

print(student_summary.head())
