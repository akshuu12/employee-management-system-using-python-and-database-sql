# Employee Management System 🧑‍💼

A simple, GUI-based **Employee Management System** built using Python, Tkinter, and MySQL. This project helps users manage employee information through an easy-to-use graphical interface.

## 📌 About the Project

The Employee Management System is a desktop application designed to store and manage employee records in a MySQL database.

It uses **Tkinter** for the graphical user interface and **MySQL** for storing employee information persistently.

This project is suitable for beginners who want to learn Python GUI development and database connectivity.

## ✨ Features

- 🖥️ **Graphical User Interface:** Simple interface built with Tkinter.
- 🗄️ **MySQL Database:** Stores employee information in a database.
- 👤 **Employee Records:** Manages employee details such as ID, name, designation, department, and salary.
- 🔍 **Employee Search:** Includes dialog-based interaction for employee-related operations.
- 💬 **Message Boxes:** Displays useful messages and alerts to users.
- 📊 **Organized Data:** Keeps employee information structured in a database table.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Tkinter | Graphical user interface |
| MySQL | Database management |
| `mysql-connector-python` | Connects Python to MySQL |
| `ttk` | Enhanced Tkinter widgets |

## 📋 Requirements

Before running the application, install:

- Python 3
- MySQL Server or XAMPP with MySQL/MariaDB
- pip (Python package manager)

## 🚀 Installation and Setup

### 1. Clone the repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/akshuu12/employee-management-system.git
```

Move into the project directory:

```bash
cd employee-management-system
```

> If your GitHub repository has a different name, replace `employee-management-system` with your actual repository name.

### 2. Install the required Python package

```bash
python -m pip install mysql-connector-python
```

Tkinter is included with many standard Python installations. On some Linux distributions, it must be installed separately.

### 3. Start MySQL

Start your MySQL server. If you use XAMPP, open the XAMPP Control Panel and start MySQL.

Make sure the server is running before launching the application.

### 4. Create the database

Open MySQL and execute:

```sql
CREATE DATABASE IF NOT EXISTS rythm;

USE rythm;

CREATE TABLE IF NOT EXISTS Employee_details (
    ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Designation VARCHAR(150) NOT NULL,
    Department VARCHAR(150) NOT NULL,
    Salary FLOAT
);
```

This creates the database and employee table used by the application.

### 5. Configure the database connection

In your Python file, locate the database connection:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='rythm'
)
```

Update the connection settings according to your local MySQL configuration.

- `host`: Your MySQL server address.
- `user`: Your MySQL username.
- `passwd`: Your MySQL password.
- `database`: The database name.

**Important:** The example uses an empty password. If your MySQL account has a password, enter it in the configuration. Never commit real database passwords to a public repository.

### 6. Run the application

Run the main Python file from your terminal:

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file if it is different.

The application window should open, allowing you to interact with the employee management system.

## 🗃️ Database Structure

The application uses the `Employee_details` table.

| Column | Data Type | Description |
|---|---|---|
| `ID` | INT | Unique employee identifier |
| `Name` | VARCHAR(100) | Employee name |
| `Designation` | VARCHAR(150) | Employee job title |
| `Department` | VARCHAR(150) | Employee department |
| `Salary` | FLOAT | Employee salary |

The `ID` column is the primary key, so each employee must have a unique ID.

## 📁 Project Structure

A suggested project structure is:

```text
employee-management-system/
│
├── main.py
├── README.md
└── requirements.txt
```

Your actual filenames may differ. Keep the Python source file and README in the appropriate locations.

## 📦 Dependencies

You can create a `requirements.txt` file containing:

```text
mysql-connector-python
```

Install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

Tkinter is part of the Python standard library on many systems and generally does not need to be installed through pip.

## 🔧 Troubleshooting

**1. MySQL connection error**

- Check that MySQL is running.
- Verify the username and password.
- Confirm that the `rythm` database exists.

**2. ModuleNotFoundError: No module named 'mysql'**

Install the connector:

```bash
python -m pip install mysql-connector-python
```

**3. Database or table does not exist**

Run the SQL commands provided in the database setup section.

**4. Employee ID already exists**

Each employee must have a unique ID because `ID` is the primary key.

## 🎯 Learning Objectives

This project demonstrates practical use of:

- Python programming
- GUI development with Tkinter
- Connecting Python applications to MySQL
- Executing SQL queries
- Handling user input and dialog boxes
- Organizing a small desktop application

## 🔮 Future Improvements

Potential improvements include:

- Employee record update and deletion
- Employee search and filtering
- Input validation
- Salary reports and department-wise summaries
- Exporting records to CSV or Excel
- Improved interface design
- Secure database configuration

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a pull request.

## 📄 License

This project is available for learning and personal use. Add an appropriate open-source license, such as the MIT License, if you want others to reuse and distribute it under those terms.

---

**Built with ❤️ using Python, Tkinter, and MySQL.**
