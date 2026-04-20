import os
import csv
import json

# ---------- TASK D1 ----------
print("Checking file...")
if not os.path.exists("students.csv"):
    print("Error: students.csv not found. Please download the file from LMS.")
    exit()
else:
    print("File found: students.csv")

print("Checking output folder...")
if not os.path.exists("output"):
    os.makedirs("output")
    print("Output folder created: output/")
else:
    print("Output folder already exists: output/")

# ---------- TASK D2 ----------
students = []

with open("students.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

print(f"Total students: {len(students)}")

print("First 5 rows:")
print("--------------------------------")
for i in range(5):
    s = students[i]
    print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
print("--------------------------------")


# ---------- TASK D3 ----------
# сортировка как в Excel: сначала по score, потом по GPA
sorted_students = sorted(
    students,
    key=lambda x: (x['final_exam_score'], x['GPA']),
    reverse=True
)

top10 = sorted_students[:10]

print("--------------------------------")
print("Top 10 Students by Exam Score")
print("--------------------------------")

for i, s in enumerate(top10, start=1):
    print(f"{i}. {s['student_id']} | {s['country']} | {s['major']} | "
          f"Score: {s['final_exam_score']} | GPA: {s['GPA']}")

print("--------------------------------")


# ---------- TASK D4 ----------
result = {
    "analysis": "Top 10 Students by Exam Score",
    "total_students": len(students),
    "top_10": []
}

for i, s in enumerate(top10, start=1):
    result["top_10"].append({
        "rank": i,
        "student_id": s["student_id"],
        "country": s["country"],
        "major": s["major"],
        "final_exam_score": s["final_exam_score"],
        "GPA": s["GPA"]
    })

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("==============================")
print("ANALYSIS RESULT")
print("==============================")
print("Analysis :", result["analysis"])
print("Total students :", result["total_students"])
print("Top 10 saved to output/result.json")
print("==============================")
print("Result saved to output/result.json")
