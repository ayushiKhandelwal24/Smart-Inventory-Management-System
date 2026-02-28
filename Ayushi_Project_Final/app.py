from flask import Flask, render_template, request, redirect, url_for, session, Response
import mysql.connector
import csv
import io

app = Flask(__name__)
app.secret_key = "multi_shop_secret_key"

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="NayaPassword123", # Aapka password
        database="inventory_db"
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['logged_in'] = True
            return redirect(url_for('shop_page')) # Login ke baad Shop Selection
        error = "Invalid Credentials!"
    return render_template('login.html', error=error)

@app.route('/shop_selection')
def shop_page():
    if not session.get('logged_in'): return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM shops") # MySQL se shops lana
    all_shops = cursor.fetchall()
    conn.close()
    return render_template('shop_selection.html', shops=all_shops)

@app.route('/select_shop', methods=['POST'])
def select_shop():
    session['current_shop'] = request.form['shop_name'] # Shop name save karna
    return redirect(url_for('index'))

@app.route('/')
def index():
    if not session.get('logged_in') or 'current_shop' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    inventory = cursor.fetchall()
    
    total_items = len(inventory)
    total_value = sum(item['quantity'] * item['price'] for item in inventory)
    low_stock_count = sum(1 for item in inventory if item['quantity'] < 5)
    conn.close()
    return render_template('index.html', items=inventory, total_items=total_items, total_value=total_value, low_stock_count=low_stock_count)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# CRUD aur Export Routes (Same as before)
@app.route('/add', methods=['POST'])
def add_product():
    if not session.get('logged_in'): return redirect(url_for('login'))
    name, qty, price = request.form['name'], request.form['qty'], request.form['price']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", (name, qty, price))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_product(id):
    if not session.get('logged_in'): return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit_product(id):
    if not session.get('logged_in'): return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
    product = cursor.fetchone()
    conn.close()
    return render_template('edit.html', product=product)

@app.route('/update', methods=['POST'])
def update_product():
    if not session.get('logged_in'): return redirect(url_for('login'))
    id, name, qty, price = request.form['id'], request.form['name'], request.form['qty'], request.form['price']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=%s, quantity=%s, price=%s WHERE id=%s", (name, qty, price, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/export')
def export_csv():
    if not session.get('logged_in'): return redirect(url_for('login'))
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, quantity, price FROM products")
    items = cursor.fetchall()
    conn.close()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Product Name', 'Quantity', 'Price'])
    for item in items:
        writer.writerow([item['name'], item['quantity'], item['price']])
    output.seek(0)
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-disposition": "attachment; filename=report.csv"})

if __name__ == '__main__':
    app.run(debug=True)