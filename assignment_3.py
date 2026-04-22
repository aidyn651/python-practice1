import os
import csv
import json

# -------------------------------
# Task 1 — FileManager
# -------------------------------
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print("File not found!")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


# -------------------------------
# Task 2 — DataLoader
# -------------------------------
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.students.append(row)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print("File not found!")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-----------------------------")

        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | "
                  f"{s['country']} | GPA: {s['GPA']}")

        print("-----------------------------")


# -------------------------------
# Task 3 — DataAnalyser
# -------------------------------
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = []

    def analyse(self):
        # сортировка по exam score
        sorted_students = sorted(
            self.students,
            key=lambda s: float(s['final_exam_score']),
            reverse=True
        )

        self.result = sorted_students[:10]

    def print_results(self):
        print("Top 10 Students by Exam Score")
        print("-----------------------------")

        for i, s in enumerate(self.result, 1):
            print(f"{i}. {s['student_id']} | {s['country']} | "
                  f"Score: {s['final_exam_score']} | GPA: {s['GPA']}")

        print("-----------------------------")


# -------------------------------
# Task 4 — ResultSaver
# -------------------------------
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as e:
            print("Error saving file:", e)


# -------------------------------
# Task 5 — MAIN
# -------------------------------
fm = FileManager("students.csv")

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()
