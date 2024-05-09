

### Step 1: Set up your MySQL database

1. Install MySQL on your system if you haven't already.
2. Create a new database for your project.
3. Create a table named `users` with columns `id`, `username`, and `password`.

Here's a SQL script to create the table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);
```

### Step 2: Set up your Python environment

1. Install Python if you haven't already.
2. Install Flask and Flask-Bcrypt using pip:

```
pip install Flask Flask-Bcrypt
```

3. Install MySQL connector:

```
pip install mysql-connector-python
```

### Step 3: Create your Flask app

Create a new Python file (e.g., `app.py`) and copy the code for your Flask app into it.

### Step 4: Configure your Flask app

Replace `your_username`, `your_password`, and `your_database` in the code with your MySQL database credentials.

### Step 5: Run your Flask app

Run your Flask app:

```
python app.py
```

Your Flask app should now be running on `http://localhost:5000`.

### Step 6: Test your APIs

Use tools like Postman or cURL to test your APIs. Here are example requests:

1. User Signup:
   ```
   POST http://localhost:5000/signup
   Body: {"username": "example_user", "password": "example_password"}
   ```

2. User Login:
   ```
   POST http://localhost:5000/login
   Body: {"username": "example_user", "password": "example_password"}
   ```

3. User Logout:
   ```
   POST http://localhost:5000/logout
   ```

4. Password Reset:
   ```
   POST http://localhost:5000/password-reset
   Body: {"username": "example_user", "new_password": "new_example_password"}
   ```

5. Token Refresh:
   ```
   POST http://localhost:5000/token-refresh
   ```
