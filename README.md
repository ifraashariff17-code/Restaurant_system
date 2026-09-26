RESTAURANT ORDER MANAGEMENT SYSTEM 
Project README / Reference Document 
A web-based Restaurant Order Management System developed using Python, Flask, HTML5, CSS3, Bootstrap 5, and JavaScript. The application helps food service establishments manage multi-cuisine menus, customer orders via an interactive sliding cart drawer, and real-time kitchen order tracking through a clean and professional dashboard. 
 
Features 
•	• Multi-Cuisine Menu Management across various culinary categories with pricing.
•	• Interactive Sliding Cart Drawer allowing seamless item review and quantity updates. 
•	• Real-time Order Placement via asynchronous JSON API requests. 
•	• Live Kitchen Orders Tracker Dashboard displaying incoming active orders. 
•	• Order Status Tracking supporting Pending, Processing, and Completed states. 
•	• Responsive Bootstrap 5 Interface optimized for multi-device viewing. 
•	• Professional Dark & Modern Dashboard Design providing high usability. 
Tech Stack 
•	Frontend:  HTML5, CSS3, Bootstrap 5, JavaScript 
•	Backend:  Python, Flask Framework 
•	Data Handling:  Python Dictionaries & Lists (Easily expandable to SQLite/SQLAlchemy) 
Project Structure 
restaurant_system/ 
│ 
├── app.py 
├── requirements.txt 
├── README.md 
├── static/ 
│   ├── style.css 
│   └── script.js 
└── templates/ 
    ├── base.html 
    ├── welcome.html 
    ├── menu.html 
    └── kitchen.html 
 
Core Data Entities 
Menu Item Structure 
•	• id:  Unique menu item identifier • 	• name:  Name of the dish 
•	• price:  Price in Indian Rupees (₹) 
•	• cuisine:  Category or cuisine type (North Indian, South Indian, Italian, Chinese) 
•	• image:  Image URL reference for visual appeal 
Order Structure 
•	• id:  Unique order identifier 
•	• items:  List of selected dishes and quantities ordered 
•	• total:  Calculated total monetary value of the order 
•	• status:  Current operational status of the order (Pending/Completed) 
Application Workflow 
•	1.  Launch application and view the welcome splash page. 
•	2.  Navigate to the multi-cuisine menu page. 
•	3.  Browse food items across different categories with pricing in ₹. 
•	4.  Add desired dishes to the active order cart. 
•	5.  Toggle the sliding cart drawer to review items and total price. 
•	6.  Click 'Place Order Now' to submit order payload via backend API. 
•	7.  Access the Kitchen Dashboard to view live incoming orders. 
•	8.  Monitor and update order fulfillment statuses in real time. 
Installation Guide 
•	1.  Clone or download the project repository. 
•	2.  Open terminal and navigate to the project root directory: cd restaurant_system 
•	3.  Create a Python virtual environment: python -m venv venv 
•	4.  Activate virtual environment (Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate) 
•	5.  Install project dependencies: pip install -r requirements.txt (Flask) 
Run the Application 
Execute the following command in your terminal to start the development server: 
python app.py 
 
Open your web browser and navigate to: http://127.0.0.1:5000/ 
Screenshots Reference 
•	•  Welcome Page: 

<img width="959" height="356" alt="Screenshot 2026-09-26 114208" src="https://github.com/user-attachments/assets/b54b0ced-527c-4c50-abcf-eca93014f9e2" />

 
•	•  Menu Page: 
<img width="942" height="370" alt="Screenshot 2026-09-26 114232" src="https://github.com/user-attachments/assets/8944a1e3-a19d-453e-8f65-68531b255753" />

 
•	•  Cart Drawer: 

        <img width="287" height="361" alt="Screenshot 2026-09-26 114657" src="https://github.com/user-attachments/assets/90ccf303-cd6a-43b2-ae65-e37d34e013f8" />

•	•  Kitchen Dashboard: 
<img width="441" height="347" alt="Screenshot 2026-09-26 114315" src="https://github.com/user-attachments/assets/2274f9c5-cc2a-4f90-be94-09378b185167" />

 
Future Enhancements 
•	•  Customer Authentication and User Login 
•	•  Role-based Access Control (Admin, Chef, Customer) 
•	•  Persistent Database Integration (SQLite / PostgreSQL) 
•	•  Payment Gateway Integration 
•	•  SMS and Email Order Confirmations 
Learning Outcomes 
•	•  Python programming and server-side routing fundamentals 
•	•  Flask web application framework development 
•	•  Frontend layout creation using HTML, CSS, and Bootstrap 5 
•	•  Asynchronous client-server communication using JavaScript Fetch API 
Author & Metadata 
Student Name:  Ifraa shariff  
Course: BCA 
Project Title:  Restaurant Order Management System 
Technologies:  Python | Flask | Bootstrap 5 | JavaScript 

GitHUB
https://github.com/ifraashariff17-code/Restaurant_system.git

License
Developed for educational, academic, internship, and portfolio purposes. 



