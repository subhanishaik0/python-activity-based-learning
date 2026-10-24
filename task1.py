# University Scholarship Allocation System

print("=" * 70)
print("          UNIVERSITY SCHOLARSHIP ALLOCATION")
print("=" * 70)

students = []

# Scholarship Criteria
MIN_SUBJECT_MARKS = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

num_students = int(input("Enter Number of Applicants: "))

for i in range(num_students):
    print(f"\nApplicant {i+1}")

    name = input("Enter Student Name: ")

    subject1 = float(input("Subject 1 Marks: "))
    subject2 = float(input("Subject 2 Marks: "))
    subject3 = float(input("Subject 3 Marks: "))

    attendance = float(input("Attendance Percentage: "))
    income = float(input("Annual Family Income (₹): "))

    aggregate = (subject1 + subject2 + subject3) / 3

    eligible = (
        subject1 >= MIN_SUBJECT_MARKS and
        subject2 >= MIN_SUBJECT_MARKS and
        subject3 >= MIN_SUBJECT_MARKS and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME
    )

    students.append({
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "eligible": eligible
    })

# Filter Eligible Students
eligible_students = [s for s in students if s["eligible"]]

# Ranking Rules:
# 1. Higher Aggregate
# 2. Higher Attendance
# 3. Lower Income

eligible_students.sort(
    key=lambda x: (-x["aggregate"],
                   -x["attendance"],
                   x["income"])
)

print("\n" + "=" * 70)
print("                 SCHOLARSHIP RESULTS")
print("=" * 70)

if len(eligible_students) == 0:
    print("No students are eligible for the scholarship.")
else:

    print(f"{'Rank':<8}{'Name':<20}{'Aggregate':<15}"
          f"{'Attendance':<15}{'Income'}")
    print("-" * 70)

    rank = 1

    for student in eligible_students:
        print(
            f"{rank:<8}"
            f"{student['name']:<20}"
            f"{student['aggregate']:<15.2f}"
            f"{student['attendance']:<15.2f}"
            f"₹{student['income']:.0f}"
        )
        rank += 1

print("\n" + "=" * 70)
print("ELIGIBILITY CRITERIA")
print("=" * 70)
print(f"Minimum Subject Marks : {MIN_SUBJECT_MARKS}")
print(f"Minimum Attendance    : {MIN_ATTENDANCE}%")
print(f"Maximum Family Income : ₹{MAX_INCOME}")
print("=" * 70)