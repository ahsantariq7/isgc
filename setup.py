from setuptools import setup, find_packages

setup(
    name='isgc',
    version='1.0.2',
    author='Ahsan Tariq',
    author_email='ahsantariq0724@gmail.com',
    description='A SGPA and CGPA Calculator for Islamia University Bahawalpur Graduation Students under supervision of Malik Shahzad, a Senior Developer. Also thankful for departmental support from M. Bux Alvi Sahb and Engr. Mubashir Hussain. A motivation from Muhammad Ibrar. Also very thankful to Sundas Tariq and Laiba Saleem for contributing to this project and making it usable for all IUB Graduation Students. Some friendly support from Asim Zubair and Usman Akram',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ahsantariq7/isgc',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords=['isgc, ISGC, GPA calculator education','Islamia University Bahawalpur', 'Ahsan Tariq','Ahsan Tariq 0724'],
    install_requires=[
        'pyfiglet',
        'matplotlib',
        'seaborn',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'calculate_gpa=isgc.gpa_calculator.calculator:calculate_gpa',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/ahsantariq7/isgc/issues',
        'Source': 'https://github.com/ahsantariq7/isgc',
    },
)
