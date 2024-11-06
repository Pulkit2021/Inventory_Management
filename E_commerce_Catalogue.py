
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="#Network2",
        db="E_Store"
    )

#
def add_category():
    category_name = category_entry.get()
    if category_name:
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Category (CategoryName) VALUES (%s)", (category_name,))
            db.commit()
            messagebox.showinfo("Success", "Category added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            db.close()
            category_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a category name.")

# Function to add a customer
def add_customer():
    customer_name = customer_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    if customer_name and email and phone and address:
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Customer (CustomerName, Email, Phone, Address) VALUES (%s, %s, %s, %s)",
                           (customer_name, email, phone, address))
            db.commit()
            messagebox.showinfo("Success", "Customer added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            db.close()
            customer_name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to add a product
def add_product():
    product_name = product_name_entry.get()
    price = price_entry.get()
    category_id = category_id_entry.get()
    if product_name and price and category_id:
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Product (ProductName, Price, CategoryID) VALUES (%s, %s, %s)",
                           (product_name, price, category_id))
            db.commit()
            messagebox.showinfo("Success", "Product added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            db.close()
            product_name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            category_id_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to add an order
def add_order():
    customer_id = customer_id_order_entry.get()
    order_date = order_date_entry.get()
    if customer_id and order_date:
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Orders (CustomerID, OrderDate) VALUES (%s, %s)", (customer_id, order_date))
            db.commit()
            messagebox.showinfo("Success", "Order added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            db.close()
            customer_id_order_entry.delete(0, tk.END)
            order_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to add an order item
def add_order_item():
    order_id = order_id_entry.get()
    product_id = product_id_order_entry.get()
    quantity = quantity_entry.get()
    price = price_order_entry.get()
    if order_id and product_id and quantity and price:
        db = connect_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Order_item (OrderID, ProductID, Quantity, Price) VALUES (%s, %s, %s, %s)",
                           (order_id, product_id, quantity, price))
            db.commit()
            messagebox.showinfo("Success", "Order item added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            db.close()
            order_id_entry.delete(0, tk.END)
            product_id_order_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            price_order_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Create main window
root = tk.Tk()
root.title("E-Store Management")

# Category frame
category_frame = tk.Frame(root)
category_frame.pack(pady=10)

tk.Label(category_frame, text="Category Name:").grid(row=0, column=0)
category_entry = tk.Entry(category_frame)
category_entry.grid(row=0, column=1)

tk.Button(category_frame, text="Add Category", command=add_category).grid(row=0, column=2)

# Customer frame
customer_frame = tk.Frame(root)
customer_frame.pack(pady=10)

tk.Label(customer_frame, text="Customer Name:").grid(row=0, column=0)
customer_name_entry = tk.Entry(customer_frame)
customer_name_entry.grid(row=0, column=1)

tk.Label(customer_frame, text="Email:").grid(row=1, column=0)
email_entry = tk.Entry(customer_frame)
email_entry.grid(row=1, column=1)

tk.Label(customer_frame, text="Phone:").grid(row=2, column=0)
phone_entry = tk.Entry(customer_frame)
phone_entry.grid(row=2, column=1)

tk.Label(customer_frame, text="Address:").grid(row=3, column=0)
address_entry = tk.Entry(customer_frame)
address_entry.grid(row=3, column=1)

tk.Button(customer_frame, text="Add Customer", command=add_customer).grid(row=4, column=0, columnspan=2)

# Product frame
product_frame = tk.Frame(root)
product_frame.pack(pady=10)

tk.Label(product_frame, text="Product Name:").grid(row=0, column=0)
product_name_entry = tk.Entry(product_frame)
product_name_entry.grid(row=0, column=1)

tk.Label(product_frame, text="Price:").grid(row=1, column=0)
price_entry = tk.Entry(product_frame)
price_entry.grid(row=1, column=1)

tk.Label(product_frame, text="Category ID:").grid(row=2, column=0)
category_id_entry = tk.Entry(product_frame)
category_id_entry.grid(row=2, column=1)

tk.Button(product_frame, text="Add Product", command=add_product).grid(row=3, column=0, columnspan=2)

# Order frame
order_frame = tk.Frame(root)
order_frame.pack(pady=10)

tk.Label(order_frame, text="Customer ID:").grid(row=0, column=0)
customer_id_order_entry = tk.Entry(order_frame)
customer_id_order_entry.grid(row=0, column=1)

tk.Label(order_frame, text="Order Date (YYYY-MM-DD):").grid(row=1, column=0)
order_date_entry = tk.Entry(order_frame)
order_date_entry.grid(row=1, column=1)

tk.Button(order_frame, text="Add Order", command=add_order).grid(row=2, column=0, columnspan=2)

# Order Item frame
order_item_frame = tk.Frame(root)
order_item_frame.pack(pady=10)

tk.Label(order_item_frame, text="Order ID:").grid(row=0, column=0)
order_id_entry = tk.Entry(order_item_frame)
order_id_entry.grid(row=0, column=1)

tk.Label(order_item_frame, text="Product ID:").grid(row=1, column=0)
product_id_order_entry = tk.Entry(order_item_frame)
product_id_order_entry.grid(row=1, column=1)

tk.Label(order_item_frame, text="Quantity:").grid(row=2, column=0)
quantity_entry = tk.Entry(order_item_frame)
quantity_entry.grid(row=2, column=1)

tk.Label(order_item_frame, text="Price:").grid(row=3, column=0)
price_order_entry = tk.Entry(order_item_frame)
price_order_entry.grid(row=3, column=1)

tk.Button(order_item_frame, text="Add Order Item", command=add_order_item).grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()