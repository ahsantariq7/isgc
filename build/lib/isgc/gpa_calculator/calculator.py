import math
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate


def custom_round(number, decimal_places):
    factor = 10 ** decimal_places
    rounded_number = int(number * factor + 0.5) / factor
    return rounded_number

def calculate_gpa(semesters):
    grading_scale = {
        100: {'grade_point': 4.0, 'remark': 'A+ Excellent'},
        99: {'grade_point': 4.0, 'remark': 'A+ Excellent'},
        98: {'grade_point': 4.0, 'remark': 'A+ Excellent'},
        97: {'grade_point': 4.0, 'remark': 'A+ Excellent'},
        96: {'grade_point': 4.0, 'remark': 'A+ Excellent'},
        95: {'grade_point': 4.0, 'remark': 'A+ Excellent'},
        94: {'grade_point': 4.0, 'remark': 'A Very Good'},
        93: {'grade_point': 4.0, 'remark': 'A Very Good'},
        92: {'grade_point': 4.0, 'remark': 'A Very Good'},
        91: {'grade_point': 4.0, 'remark': 'A Very Good'},
        90: {'grade_point': 4.0, 'remark': 'A Very Good'},
        89: {'grade_point': 4.0, 'remark': 'A Very Good'},
        88: {'grade_point': 4.0, 'remark': 'A Very Good'},
        87: {'grade_point': 4.0, 'remark': 'A Very Good'},
        86: {'grade_point': 4.0, 'remark': 'A Very Good'},
        85: {'grade_point': 4.0, 'remark': 'A Very Good'},
        84: {'grade_point': 3.9, 'remark': 'B+ Good'},
        83: {'grade_point': 3.9, 'remark': 'B+ Good'},
        82: {'grade_point': 3.8, 'remark': 'B+ Good'},
        81: {'grade_point': 3.7, 'remark': 'B+ Good'},
        80: {'grade_point': 3.7, 'remark': 'B+ Good'},
        79: {'grade_point': 3.6, 'remark': 'B Good'},
        78: {'grade_point': 3.5, 'remark': 'B Good'},
        77: {'grade_point': 3.5, 'remark': 'B Good'},
        76: {'grade_point': 3.4, 'remark': 'B Good'},
        75: {'grade_point': 3.3, 'remark': 'B Good'},
        74: {'grade_point': 3.3, 'remark': 'B Good'},
        73: {'grade_point': 3.2, 'remark': 'B Good'},
        72: {'grade_point': 3.1, 'remark': 'B Good'},
        71: {'grade_point': 3.1, 'remark': 'B Good'},
        70: {'grade_point': 3.0, 'remark': 'B Good'},
        69: {'grade_point': 2.9, 'remark': 'C Satisfactory'},
        68: {'grade_point': 2.8, 'remark': 'C Satisfactory'},
        67: {'grade_point': 2.7, 'remark': 'C Satisfactory'},
        66: {'grade_point': 2.6, 'remark': 'C Satisfactory'},
        65: {'grade_point': 2.5, 'remark': 'C Satisfactory'},
        64: {'grade_point': 2.4, 'remark': 'C Satisfactory'},
        63: {'grade_point': 2.3, 'remark': 'C Satisfactory'},
        62: {'grade_point': 2.2, 'remark': 'C Satisfactory'},
        61: {'grade_point': 2.1, 'remark': 'C Satisfactory'},
        60: {'grade_point': 2.0, 'remark': 'C Satisfactory'},
        59: {'grade_point': 1.9, 'remark': 'D Poor'},
        58: {'grade_point': 1.8, 'remark': 'D Poor'},
        57: {'grade_point': 1.7, 'remark': 'D Poor'},
        56: {'grade_point': 1.6, 'remark': 'D Poor'},
        55: {'grade_point': 1.5, 'remark': 'D Poor'},
        54: {'grade_point': 1.4, 'remark': 'D Poor'},
        53: {'grade_point': 1.3, 'remark': 'D Poor'},
        52: {'grade_point': 1.2, 'remark': 'D Poor'},
        51: {'grade_point': 1.1, 'remark': 'D Poor'},
        50: {'grade_point': 1.0, 'remark': 'D Poor'},
        49: {'grade_point': 0.0, 'remark': 'F Fail'}

    }

    total_grade_points = 0
    total_credit_hours = 0
    total_rounded_percentage = 0
    total_total_marks = 0
    total_obtained_marks = 0
    total_quality_points = 0
    semester_gp_list = []
    # Store grades for each subject across semesters
    subject_grade_remarks = {subject: [] for semester in semesters.values() for subject in semester}

    result_table = []


    

    for semester, subjects in semesters.items():
        #print(f"Semester: {semester}")
        semester_grade_points = 0
        semester_credit_hours = 0
        semester_rounded_percentage = 0
        semester_total_marks = 0
        semester_obtained_marks = 0
        semester_quality_points = 0
         

        for subject, details in subjects.items():
            credit_hours = details['credit_hours']
            obtained_marks = details['marks']
            max_marks = details.get('total_marks', 100)  # Default max_marks to 100 if not provided

            percentage = (obtained_marks / max_marks) * 100
            rounded_percentage = math.ceil(percentage)

            if rounded_percentage in grading_scale:
                grade_point = grading_scale[rounded_percentage]['grade_point']
                remark = grading_scale[rounded_percentage]['remark']
            elif rounded_percentage < 49:
                grade_point = 0.0  
                remark = 'F Fail'
            else:
                grade_point = 0.0  
                remark = ''

            quality_point = (grade_point * credit_hours)

            semester_grade_points += quality_point
            semester_credit_hours += credit_hours
            semester_rounded_percentage += rounded_percentage
            semester_total_marks += max_marks
            semester_obtained_marks += obtained_marks
            semester_quality_points += quality_point
            # Accumulate total grades for each subject across semesters
            # Accumulate grade remarks for each subject across semesters
            subject_grade_remarks[subject].append(remark)

            #print(f"Subject: {subject}, Credit Hours: {credit_hours}, Obtained Marks: {obtained_marks}, Percentage: {percentage}%, Rounded Percentage: {rounded_percentage}, Grade Point: {grade_point}, Remark: {remark}, Quality Point: {quality_point}")

        semester_gpa = (semester_grade_points / semester_credit_hours)
        semester_gpa = custom_round(semester_gpa, 2)
        semester_gp_list.append(semester_gpa)
        #print(f"SGPA for Semester {semester}: {semester_gpa}\n")

        total_grade_points += semester_grade_points
        total_credit_hours += semester_credit_hours
        total_rounded_percentage += semester_rounded_percentage
        total_total_marks += semester_total_marks
        total_obtained_marks += semester_obtained_marks
        total_quality_points += semester_quality_points

        result_table.append([
            semester,
            semester_gpa,
            semester_credit_hours,
            semester_rounded_percentage,
            semester_total_marks,
            semester_obtained_marks,
            semester_quality_points
        ])

    

    cgpa = (total_grade_points / total_credit_hours)

    # Display results in a table
    # Display results in a table
    headers = ['Semester', 'SGPA', 'Total CH', 'Total %', 'Total TM', 'Total OM', 'Total QP']
    print(tabulate(result_table, headers=headers, tablefmt='fancy_grid'))
   
    

    plt.figure(figsize=(15, 6))

    # Plot SGPA and Number of Subjects with Same Grade Remarks
    plt.subplot(1, 2, 1)
    sns.lineplot(x=list(semesters.keys()), y=semester_gp_list, marker='o', label='SGPA')
    plt.axhline(y=cgpa, color='r', linestyle='--', label=f'CGPA: {custom_round(cgpa, 2)}')
    plt.title('Semester-wise GPA')
    plt.xlabel('Semester')
    plt.ylabel('SGPA')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    sns.countplot(x=sum(list(subject_grade_remarks.values()), []))
    plt.title('Number of Subjects with Same Grade Remarks (All Semesters)')
    plt.xlabel('Grade Remarks')
    plt.ylabel('Number of Subjects')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.show()
    
    cgpa=custom_round(cgpa, 2)

    return cgpa



