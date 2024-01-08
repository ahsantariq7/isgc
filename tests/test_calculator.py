from isgc.gpa_calculator.calculator import IUB

semesters = {
    # Your semester data here...
}

# Instantiate the IUB class
iub_instance = IUB()

# Call the method on the instance
cgpa = iub_instance.calculate_semester_gpa(semesters)

print(f"CGPA: {cgpa}")
