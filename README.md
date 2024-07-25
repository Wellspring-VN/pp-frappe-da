# Data Analysis Tools for the Parent Portal App at WSSG

## Introduction

This repository contains the data analysis tools for the Parent Portal App at WSSG. The tools are written in Python and are used to analyze the data collected from the Parent Portal App. The Parent Portal App is written in Frappe Framework.

To connect to the server, this tool needs the following environment variables:

- `FRAPPE_URL`: The URL of the Frappe server.
- `ACADEMIC_YEAR`: The id of the academic year in the Frappe server.

The input data of this tool is cleaned data in form of Excel Files:

- `sis_student.xlsx`: Contains the data of the students. This data will be fill into SIS Student and SIS Person
- `sis_school_class.xlsx`: Contains the data of the school classes (e.g. Class 1.2, Class 2.2, ...). Grade levels will be extracted from class names, e.g. 1.1 -> 1, 2.1 -> 2, ...
- `sis_teacher.xlsx`: Contains the data of the teachers.
- `sis_family.xlsx`: Contains the data of the family members including guardians and students.
- `sis_course.xlsx`: Contains the data of the courses.
- `sis_timetable_columns.xlsx`: Contains the data of the timetable columns and rows.
- `sis_timetable.xlsx`: Contains the data of the timetable and timetable day.
- `sis_school_feed.xlsx` (Optional): Contains the data of the school news & events.
- `sis_class_activity.xlsx` (Optional): Contains the data of the class activities.

## Getting Started

This code base can be executed in a Jupyter Notebook or Python script. To import the code to a Jupyter Notebook or Colab, clone the repository to your local machine.

```bash
git clone git@github.com:Wellspring-VN/pp-frappe-da.git
```

Then, navigate to the repository and install the required packages.

```bash
cd pp-frappe-da
pip install -r requirements.txt
```

To setup the code in a Python environment, you can create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or use your own conda environment.

To run the code, you need to set the environment variables `FRAPPE_URL`, `FRAPPE_API_KEY`, `FRAPPE_API_SECRET`, and `ACADEMIC_YEAR`. You can set these environment variables in a `.env` file in the root directory of the repository.

```bash
FRAPPE_URL=https://wellspring.edu.vn
ACADEMIC_YEAR=2021-2022
```
