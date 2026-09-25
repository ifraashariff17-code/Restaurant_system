from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Extended Multi-Cuisine Menu Database (Prices in INR ₹)
menu = [
    # North Indian
    {
        "id": 1,
        "name": "Butter Chicken",
        "price": 450,
        "cuisine": "North Indian",
        "image": "https://images.unsplash.com/photo-1588166524941-3bf61a9c41db?w=500",
    },
    {
        "id": 2,
        "name": "Paneer Tikka Masala",
        "price": 380,
        "cuisine": "North Indian",
        "image": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=500",
    },
    {
        "id": 3,
        "name": "Dal Makhani",
        "price": 300,
        "cuisine": "North Indian",
        "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=500",
    },
    # South Indian
    {
        "id": 4,
        "name": "Masala Dosa",
        "price": 180,
        "cuisine": "South Indian",
        "image": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=500",
    },
    {
        "id": 5,
        "name": "Hyderabadi Chicken Biryani",
        "price": 420,
        "cuisine": "South Indian",
        "image": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=500",
    },
    # Italian / Continental
    {
        "id": 6,
        "name": "Woodfire Margherita Pizza",
        "price": 499,
        "cuisine": "Italian",
        "image": "https://images.unsplash.com/photo-1604382355076-af4b0eb60143?w=500",
    },
    {
        "id": 7,
        "name": "Creamy White Sauce Pasta",
        "price": 399,
        "cuisine": "Italian",
        "image": "https://images.unsplash.com/photo-1621996346565-e3d5d6281298?w=500",
    },
    # Chinese / Asian
    {
        "id": 8,
        "name": "Veg Hakka Noodles",
        "price": 250,
        "cuisine": "Chinese",
        "image": "https://images.unsplash.com/photo-1585032226651-759b368d7246?w=500",
    },
    {
        "id": 9,
        "name": "Chilli Garlic Chicken",
        "price": 350,
        "cuisine": "Chinese",
        "image": "https://images.unsplash.com/photo-1525755662778-989d0524087e?w=500",
    },
]

orders = []


@app.route("/")
def welcome():
  return render_template("welcome.html")


@app.route("/menu")
def index():
  return render_template("menu.html", menu=menu)


@app.route("/kitchen")
def kitchen():
  return render_template("kitchen.html", orders=orders)


@app.route("/api/order", methods=["POST"])
def place_order():
  data = request.get_json()
  new_order = {
      "id": len(orders) + 1,
      "items": data.get("items", []),
      "total": data.get("total", 0),
      "status": "Pending",
  }
  orders.append(new_order)
  return jsonify(
      {"message": "Order placed successfully!", "order": new_order}
  ), 201


@app.route("/api/order/<int:order_id>/status", methods=["POST"])
def update_status(order_id):
  data = request.get_json()
  new_status = data.get("status")
  for order in orders:
    if order["id"] == order_id:
      order["status"] = new_status
      return jsonify({"message": "Status updated successfully!"})
  return jsonify({"error": "Order not found"}), 404


if __name__ == "__main__":
  app.run(debug=True)