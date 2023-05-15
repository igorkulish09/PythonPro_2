from flask import Flask
import random

constant = [1, 2, 3]

app = Flask(__name__)

@app.route("/")
def show_items():
    return f"<h3>Our Items are: {constant}!!!<h3>"

@app.route("/delete_item")
def delete_item():
    if len(constant) > 0:
        constant.pop() # Видаляє останній елемент зі списку
        return f"<h3>Deleted Item! Current Items: {constant}</h3>"
    else:
        return f"<h3>No items to delete!</h3>"

@app.route("/add_item")
def add_item():
    new_item = random.randint(0, 100) # Створює випадкове число з діапазону 0..100
    constant.append(new_item) # Додає новий елемент до списку
    return f"<h3>Added Item! Current Items: {constant}</h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

