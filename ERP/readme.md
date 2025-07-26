# 🧾 Mini ERP System using Flask

This is a simple **ERP (Enterprise Resource Planning)** demo application built using **Flask**, **SQLite**, and **HTML templates**. It includes basic modules like Inventory Management with full CRUD functionality.

---

## 📌 Features

- ✅ View Inventory Items  
- ➕ Add New Item  
- ✏️ Edit Item  
- ❌ Delete Item  
- 💾 SQLite DB Integration  
- 🎨 HTML UI using Jinja2 templates  

---

## 🛠️ Tech Stack

- Python 3.x  
- Flask  
- SQLite  
- HTML/CSS (Jinja Templates)  

---

## 🚀 Setup Instructions

1. **Clone this repo or download the source code**

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate    # On Windows: env\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Visit in browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## 🧩 Database Schema

### Table: Inventory

| Column    | Type    | Description         |
|-----------|---------|---------------------|
| id        | Integer | Primary Key         |
| name      | String  | Item Name           |
| quantity  | Integer | Item Quantity       |

---

## 🌐 Flask Routes Reference

| Route                         | Method | Description                      |
|------------------------------|--------|----------------------------------|
| `/`                          | GET    | Homepage / Dashboard             |
| `/inventory`                 | GET    | View inventory list              |
| `/add_inventory`             | GET/POST | Add new inventory item          |
| `/edit_inventory/<int:id>`  | GET/POST | Edit selected inventory item    |
| `/delete_inventory/<int:id>`| GET    | Delete selected inventory item   |

---

## 📂 Folder Structure

```
project/
│
├── app.py                   # Main Flask app
├── models.py                # DB Models (if separated)
├── routes.py                # All routes and logic
├── templates/
│   └── inventory/
│       ├── inventory.html   # Inventory list view
│       ├── add_inventory.html
│       └── edit_inventory.html
├── static/                  # (Optional CSS, JS)
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

*(Add screenshots of UI here if available)*

---

## 📘 How it Works

1. The user opens `/inventory` to see all inventory items.
2. They can click **"Add Item"**, **"Edit"**, or **"Delete"**.
3. Forms submit using POST to update the SQLite database.
4. Changes are reflected immediately and persisted.

---

## 🙋‍♀️ Author

- **Tamilarasi A** – Computer Science Graduate  


---

## 📎 License

This project is for learning/demo purposes and is not production-grade.
