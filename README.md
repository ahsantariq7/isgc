# Islamia University Bahawalpur SGPA, CGPA Calculation And Analysis

1. How to Run the project.

`pip install isgc`

2. import calculation_gpa

`from isgc.gpa_calculator.calculator import calculate_gpa`


3. Enter Semesters detail like that.


<div>
    <pre>
        <code id="semesters" class="json">
{
    "Semester 1": {
        "Subject 1": {"credit_hours": 2, "marks": 44, "total_marks": 50},
        "Subject 2": {"credit_hours": 3, "marks": 76, "total_marks": 100},
        "Subject 3": {"credit_hours": 2, "marks": 36, "total_marks": 50},
        "Subject 4": {"credit_hours": 1, "marks": 46, "total_marks": 50},
        "Subject 5": {"credit_hours": 3, "marks": 31, "total_marks": 50},
        "Subject 6": {"credit_hours": 1, "marks": 43, "total_marks": 50},
        "Subject 7": {"credit_hours": 3, "marks": 88, "total_marks": 100},
        "Subject 8": {"credit_hours": 1, "marks": 44, "total_marks": 50}
    },
    "Semester 2": {
        "Subject 1": {"credit_hours": 2, "marks": 44, "total_marks": 50},
        "Subject 2": {"credit_hours": 3, "marks": 76, "total_marks": 100},
        "Subject 3": {"credit_hours": 2, "marks": 36, "total_marks": 50},
        "Subject 4": {"credit_hours": 1, "marks": 46, "total_marks": 50},
        "Subject 5": {"credit_hours": 3, "marks": 31, "total_marks": 50},
        "Subject 6": {"credit_hours": 1, "marks": 43, "total_marks": 50},
        "Subject 7": {"credit_hours": 3, "marks": 160, "total_marks": 200},
        "Subject 8": {"credit_hours": 1, "marks": 44, "total_marks": 50}
    }
}
        </code>
    </pre>
</div>


4. Make an Object.

`cgpa=calculation_gpa(semesters)`

5. print output.

`print(cgpa)`

![Full Code](image.png)


Grading Scale we Use For Calculation official IUB :

<div>
    <pre>
        <code class="json">
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

</div>

# Pseude Code

<div>
FUNCTION custom_round(number, decimal_places)
    factor = 10 raised to the power of decimal_places
    rounded_number = integer part of (number * factor + 0.5) divided by factor
    RETURN rounded_number

FUNCTION calculate_gpa(semesters)
    DEFINE grading_scale as a dictionary with grade points and remarks

    INITIALIZE total_grade_points, total_credit_hours, total_rounded_percentage, total_total_marks,
               total_obtained_marks, total_quality_points, semester_gp_list, and subject_grade_remarks

    INITIALIZE result_table as an empty list

    FOR EACH semester, subjects IN semesters
        INITIALIZE semester-specific variables

        FOR EACH subject, details IN subjects
            CALCULATE percentage, rounded_percentage, grade_point, remark, and quality_point

            ACCUMULATE semester-specific data

            ADD grade remarks for each subject across semesters to subject_grade_remarks

        CALCULATE semester_gpa
        ADD semester_gpa to semester_gp_list

        ACCUMULATE total data across semesters

        APPEND semester-wise data to result_table

    CALCULATE cgpa based on total_grade_points and total_credit_hours

    DISPLAY results in a table format using tabulate

    PLOT visualizations using Matplotlib and Seaborn for SGPA and subject grade remarks

    RETURN cgpa rounded to 2 decimal places
</div>