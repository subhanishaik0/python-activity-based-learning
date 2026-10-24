from datetime import datetime

# Student Data
students = [
    {
        "id": 101,
        "name": "Alice",
        "aggregate": 92,
        "subjects": [70, 75, 80, 85],
        "attendance": 90,
        "income": 200000,
        "application_date": "2024-05-10"
    },
    {
        "id": 102,
        "name": "Bob",
        "aggregate": 92,
        "subjects": [65, 70, 75, 80],
        "attendance": 88,
        "income": 150000,
        "application_date": "2024-05-08"
    },
    {
        "id": 103,
        "name": "Charlie",
        "aggregate": 88,
        "subjects": [62, 68, 72, 74],
        "attendance": 95,
        "income": 120000,
        "application_date": "2024-05-12"
    },
    {
        "id": 104,
        "name": "David",
        "aggregate": 74,
        "subjects": [68, 70, 72, 75],
        "attendance": 90,
        "income": 100000,
        "application_date": "2024-05-09"
    }
]

# Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_SCORE = 60
MIN_ATTENDANCE = 80
MAX_INCOME = 300000

# Step 1: Filter Eligible Students
eligible_students = []

for student in students:
    if (
        student["aggregate"] >= MIN_AGGREGATE and
        min(student["subjects"]) >= MIN_SUBJECT_SCORE and
        student["attendance"] >= MIN_ATTENDANCE and
        student["income"] <= MAX_INCOME
    ):
        eligible_students.append(student)

# Step 2: Sort According to Ranking Rules
eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],      # Higher aggregate first
        -x["attendance"],     # Higher attendance first
        x["income"],          # Lower income first
        datetime.strptime(x["application_date"], "%Y-%m-%d"),
        x["id"]               # Lower ID first
    )
)

# Step 3: Display Results
print("Scholarship Ranking List")
print("-" * 60)

for rank, student in enumerate(eligible_students, start=1):
    print(f"Rank {rank}")
    print(f"ID         : {student['id']}")
    print(f"Name       : {student['name']}")
    print(f"Aggregate  : {student['aggregate']}%")
    print(f"Attendance : {student['attendance']}%")
    print(f"Income     : ₹{student['income']}")
    print("-" * 60)