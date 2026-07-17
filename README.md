<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=6C63FF&center=true&vCenter=true&width=650&lines=Smart+Student+Management+System;Console-Based+Python+Application;TechMaster+Academy+-+AI+%26+ML+Track" alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Storage-JSON-black?style=for-the-badge&logo=json&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

<p align="center">
A console-based Student Management System built with Python, using Object-Oriented Programming (OOP) principles and JSON files for data persistence — no external database required.
</p>

> 🚧 **Work in Progress:** This project is still under active development. New features, refactors, and improvements are being added regularly — see the [Roadmap](#-roadmap--future-improvements) section below.

---

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Screenshot](#-screenshot)
- [Tech Stack](#-tech-stack)
- [Data Storage](#-data-storage)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How to Use](#-how-to-use)
- [Roadmap / Future Improvements](#-roadmap--future-improvements)
- [Contact](#-contact)

---

## 📌 About the Project

**Smart Student Management System** is a console application built in **Python** to manage students, courses, and enrollments, along with generating basic statistical reports.

This project is part of the **AI & Machine Learning Track** at **TechMaster Academy**, developed during **Phase 01 - Python Foundations**, which focuses on building a solid foundation in:

- Python Fundamentals
- Functions & Logic
- File Handling
- Problem Solving

These are the core skills every later phase — from data analysis to AI application development — will build on.

> ⚠️ **Note:** This is an evolving learning project, not a finished production system. The current version covers the core requirements, but the codebase, structure, and feature set are expected to keep changing.

---

## ✨ Features

### 👨‍🎓 Student Management
- Add a new student (with input validation)
- View all students
- Search for a student by ID
- Delete a student

### 📚 Course Management
- Add a new course
- View all available courses

### 📝 Enrollment
- Enroll a student in a course
- Prevents duplicate enrollment in the same course

### 📊 Reports
- Total number of students
- Average GPA
- Student with the highest GPA
- Number of students per department

---

## 🖼️ Screenshot

<img width="955" height="617" alt="screenshot" src="https://github.com/user-attachments/assets/1d718d4a-28f0-410f-af41-2fb1a8cbdf9a" />


---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3** | Core programming language |
| **OOP (Object-Oriented Programming)** | Code organized into classes (`Person`, `Student`, `Course`, `Enrollment`) |
| **JSON** | Data storage and retrieval |
| **Git & GitHub** | Version control and hosting |
| **VS Code** | Development environment |

---

## 🗄️ Data Storage

This project does **not** use any external database (like MySQL or MongoDB). Instead, it relies on **File Handling** with plain **JSON** files stored in the `data/` folder:

- `students.json` → student records
- `courses.json` → course records
- `enrollments.json` → student-course enrollment records

Data persists between runs, meaning it's saved even after closing and reopening the application — one of the core requirements of this project.

---

## 📂 Project Structure

```
SMART-STUDENT-MANAGEMENT-SYSTEM/
│
├── data/
│   ├── students.json
│   ├── courses.json
│   └── enrollments.json
│
├── manag/
│   ├── Student_manager.py
│   ├── Course_manager.py
│   ├── Enrollment_manager.py
│   └── Report_manager.py
│
├── Person.py
├── Student.py
├── Course.py
├── Enrollment.py
├── main.py
├── screenshot.png
└── README.md
```

---

## ⚙️ Getting Started

1. Make sure you have **Python 3.10+** installed:
   ```bash
   python --version
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/kareemahme999/-SMART-STUDENT-MANAGEMENT-SYSTEM.git
   ```

3. Navigate to the project folder:
   ```bash
   cd -SMART-STUDENT-MANAGEMENT-SYSTEM
   ```

4. Run the application:
   ```bash
   python main.py
   ```

> The project uses only Python's Standard Library, so no external packages need to be installed.

---

## ▶️ How to Use

Once you run `main.py`, you'll see the main menu:

```
=========================
 Student Management
=========================

1. Add Student
2. View Students
3. Search Student
4. Delete Student

5. Add Course
6. View Courses
7. Enroll Student

8. Reports

0. Exit
=========================
```

Choose a number for the operation you want, and the app will guide you step by step (name, age, ID, department, GPA, etc.), validating your input along the way.

---

## 🚀 Roadmap / Future Improvements

This project is not final — here's what's planned next:

- [ ] Add the ability to update an existing student's data from the main menu
- [ ] Add a grading system per course, with automatic GPA calculation
- [ ] Improve error handling and input validation across all managers
- [ ] Refactor file paths and fix inconsistent method naming (e.g. `load_courses` vs `load_students`)
- [ ] Build a GUI or web interface instead of the console
- [ ] Add unit tests to verify each operation

---

## 📬 Contact

Have a question or a suggestion to improve the project? Feel free to reach out through the repository.

<div align="center">

**TechMaster Academy** — Phase 01 / Project 01 — AI & Machine Learning Track

⭐ If you found this project useful, consider giving it a star!

</div>
