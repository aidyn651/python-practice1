import os
import csv

# -------------------------------
# D1 — FUNCTIONS
# -------------------------------

def check_files():
    print("Checking file...")
    
    if os.path.exists("students.csv"):
        print("File found: students.csv")
        file_exists = True
    else:
        print("File not found!")
        file_exists = False

    print("Checking output folder...")
    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    return file_exists


def load_data(filename):
    print("Loading data...")
    students = []
    
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        print(f"Data loaded successfully: {len(students)} students")
        return students

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return []

    except Exception as e:
        print("Error:", e)
        return []


def preview_data(students, n=5):
    print(f"First {n} rows:")
    print("-----------------------------")
    
    for s in students[:n]:
        print(f"{s.get('student_id','N/A')} | {s.get('age','N/A')} | "
              f"{s.get('gender','N/A')} | {s.get('country','N/A')} | "
              f"GPA: {s.get('GPA','N/A')}")
    
    print("-----------------------------")


# -------------------------------
# D2 — ANALYSIS FUNCTION
# -------------------------------

def get_top_students(students, n=10):
    valid_students = []

    for s in students:
        try:
            s['final_exam_score'] = float(s.get('final_exam_score', 0))
            s['GPA'] = float(s.get('GPA', 0))
            valid_students.append(s)
        except ValueError:
            print(f"Warning: could not convert value for student {s.get('student_id','Unknown')} — skipping row.")
            continue

    sorted_students = sorted(valid_students, key=lambda x: x['final_exam_score'], reverse=True)
    return sorted_students[:n]


def print_top_students(students, title):
    print(title)
    print("-----------------------------")
    
    for i, s in enumerate(students, 1):
        print(f"{i}. {s.get('student_id','N/A')} | {s.get('country','N/A')} | "
              f"Score: {s.get('final_exam_score','N/A')} | GPA: {s.get('GPA','N/A')}")
    
    print("-----------------------------")


# -------------------------------
# D3 — LAMBDA / MAP / FILTER
# -------------------------------

def lambda_map_filter(students):
    print("Lambda / Map / Filter")
    print("-----------------------------")

    try:
        top_scorers = list(filter(lambda s: float(s.get('final_exam_score', 0)) > 95, students))
        print("final_exam_score > 95 :", len(top_scorers))

        gpa_values = list(map(lambda s: float(s.get('GPA', 0)), students))
        print("GPA values (first 5) :", gpa_values[:5])

        good_assignments = list(filter(lambda s: float(s.get('assignment_score', 0)) > 90, students))
        print("assignment_score > 90 :", len(good_assignments))

    except ValueError:
        print("Error in data conversion")

    print("-----------------------------")


# -------------------------------
# MAIN PROGRAM
# -------------------------------

if check_files():
    students = load_data("students.csv")

    if students:
        preview_data(students)

        print("-----------------------------")
        top10 = get_top_students(students)
        print_top_students(top10, "Top 10 Students by Exam Score")


        lambda_map_filter(students)

# проверка ошибки
load_data("wrong_file.csv")
