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






# ==================================================
# Practice 7 — Week 7
# Variant 9
# ==================================================


# ==============================
# Task 1 — Base Class
# ==============================

class DataAnalyser:

    def __init__(self, students):

        self.students = students
        self.result = {}

    def analyse(self):

        print("Not implemented — use a child class")

    def print_results(self):

        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):

        return f"DataAnalyser: base class, {len(self.students)} students"


# ==============================
# Task 2 — Child Class
# ==============================

class TopStudentsAnalyser(DataAnalyser):

    def __init__(self, students):

        super().__init__(students)

    def analyse(self):

        top_students = []

        for student in self.students:

            gpa = float(student['GPA'])

            if gpa >= 3.5:
                top_students.append(student['student_id'])

        self.result = {
            'total_students': len(self.students),
            'top_students_count': len(top_students),
            'top_students': top_students
            
        }

    def print_results(self):

        print("==============================")
        print("TOP STUDENTS ANALYSIS REPORT")
        print("==============================")

        super().print_results()

        print("==============================")

    def __str__(self):

        return f"TopStudentsAnalyser: Top Students Analysis, {len(self.students)} students"


# ==============================
# Extra analyser for polymorphism
# ==============================

class CountryAnalyser(DataAnalyser):

    def __init__(self, students):

        super().__init__(students)

    def analyse(self):

        countries = {}

        for student in self.students:

            country = student['country']

            if country in countries:
                countries[country] += 1
            else:
                countries[country] = 1

        top_3 = sorted(
            countries.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        self.result = {
            'total_students': len(self.students),
            'total_countries': len(countries),
            'top_3': top_3
        }

    def print_results(self):

        print("==============================")
        print("COUNTRY ANALYSIS REPORT")
        print("==============================")

        super().print_results()

        print("==============================")

    def __str__(self):

        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"


# ==============================
# Task 4 — Association
# ==============================

class Report:

    def __init__(self, analyser, saver):

        self.analyser = analyser
        self.saver = saver

    def generate(self):

        print("Generating report...")

        self.analyser.analyse()

        self.analyser.print_results()

        self.saver.data = self.analyser.result

        self.saver.save_json()

        print("Report complete.")


# ==============================
# Main
# ==============================

fm = FileManager('students.csv')

fm.check_file()

fm.create_output_folder()

dl = DataLoader('students.csv')

dl.load()




# ==============================
# Task 5 — Polymorphism
# ==============================

analysers = [
    TopStudentsAnalyser(dl.students),
    CountryAnalyser(dl.students)
]

print('------------------------------')
print('Running all analysers:')
print('------------------------------')

for a in analysers:

    print(a)

    a.analyse()

    a.print_results()


# ==============================
# Task 4 — Report
# ==============================

saver = ResultSaver(
    analysers[0].result,
    'output/result.json'
)

report = Report(
    analysers[0],
    saver
)

report.generate()






