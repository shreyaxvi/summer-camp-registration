import sqlite3

def connect():
    conn = sqlite3.connect("camp.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS camp(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,phone_number TEXT,address TEXT,activity TEXT,no_of_days INTEGER,total INTEGER)")
    conn.commit()
    conn.close()

def insert(name, age, phone_number, address, activity, no_of_days, total):
    errors = validate_input(name, age, phone_number, activity, no_of_days)
    if errors:
        return errors

    conn = sqlite3.connect("camp.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO camp VALUES (NULL, ?,?,?,?,?,?,?)", (name, age, phone_number, address, activity, no_of_days, calculation(no_of_days, activity)))
    conn.commit()
    conn.close()
    return None

def view():
    conn = sqlite3.connect("camp.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM camp")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("camp.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM camp WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, name, age, phone_number, address, activity, no_of_days, total):
    errors = validate_input(name, age, phone_number, activity, no_of_days)
    if errors:
        return errors

    conn = sqlite3.connect("camp.db")
    cur = conn.cursor()
    cur.execute("UPDATE camp SET name=?, age=?, phone_number=?, address=?, activity=?, no_of_days=?, total=? WHERE id=?", (name, age, phone_number, address, activity, no_of_days, total, id))
    conn.commit()
    conn.close()
    return None

def calculation(no_of_days, activity):
    if activity.lower() == "sketching":
        total = int(no_of_days) * 80
        return total
    elif activity.lower() == "chess":
        total = int(no_of_days) * 110
        return total
    elif activity.lower() == "coding":
        total = int(no_of_days) * 100
        return total
    else:
        return 0

def validate_input(name, age, phone_number, activity, no_of_days):
    errors = []

    if not name.replace(" ", "").isalpha():
        errors.append("Name can only contain alphabets and spaces")

    if not age.isdigit() or int(age) <= 0:
        errors.append("Enter valid age")

    if not phone_number.isdigit() or len(phone_number) != 10:
        errors.append("Phone number must be 10 digits")

    valid_activities = ["sketching", "chess", "coding"]
    if activity.lower() not in valid_activities:
        errors.append("Invalid activity selected")

    if not no_of_days.isdigit():
        errors.append("Number of days must be a number")

    return errors
