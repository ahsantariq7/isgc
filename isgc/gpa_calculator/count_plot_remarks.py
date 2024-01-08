import seaborn as sns
import matplotlib.pyplot as plt

    
def subject_remarks(a):
    sns.countplot(x=sum(list(a), []))
    plt.title('Number of Subjects with Same Grade Remarks (All Semesters)')
    plt.xlabel('Grade Remarks')
    plt.ylabel('Number of Subjects')
    plt.xticks(rotation=45, ha='right')
    plt.show()
