python_projects_grocery_webapp
In this python project, we will build a grocery store management application. It will be 3 tier application,

Front end: UI is written in HTML/CSS/Javascript/Bootstrap
Backend: Python and Flask
Database: mysql
<img width="1919" height="874" alt="image" src="https://github.com/user-attachments/assets/09cb193f-6fb7-4e6d-b746-be7d91bbf24d" />


<img width="836" height="525" alt="image" src="https://github.com/user-attachments/assets/45155ea2-0b01-40a7-be63-86949686bd43" />

<img width="1919" height="870" alt="image" src="https://github.com/user-attachments/assets/511114e7-056f-4e5f-9a04-285ee8f86bd3" />




Installation Instructions
Download mysql for windows: https://dev.mysql.com/downloads/installer/

pip install mysql-connector-python

Exercise
The grocery management system that we built is functional but after we give it to users for use, we got following feedback. The exercise for you to address this feedback and implement these features in the application,

Products Module: In products page that lists current products, add an edit button next to delete button that allows to edit current product
Products Module: Implement a new form that allows you to add new UOM in the application. For example you want to add Cubic Meter as a new UOM as the grocery store decided to start selling wood as well. This requies changing backend (python server) and front end (UI) both.
Orders Module: When you place an order it doesn't have any validation. For example one can enter an order with empty customer name. You need to add validation for customer name and invalid item name or not specifying a quantity etc. This is only front end UI work.
Orders Module: In new order page there is a bug. When you manually change total price of an item it doesn't change the grand total. You need to fix this issue.
Orders Module: In the grid where orders are listed, add a view button in the last column. On clicking this button it should show you order details where individual items in that order are listed along with their price/quantity etc.
