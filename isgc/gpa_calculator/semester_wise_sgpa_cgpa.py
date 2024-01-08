from custom_round import custom_round
import matplotlib.pyplot as plt
import seaborn as sns


def semester_wise_plot(a, b, c):
    plt.subplot(1, 2, 1)
    plt.subplot(1, 2, 1)
    sns.lineplot(x=list(a), y=b, marker='o', label='SGPA')
    plt.axhline(y=c, color='r', linestyle='--', label=f'CGPA: {custom_round(c, 2)}')
    plt.title('Semester-wise GPA')
    plt.xlabel('Semester')
    plt.ylabel('SGPA')
    plt.legend()
    plt.grid(True)
    plt.show()