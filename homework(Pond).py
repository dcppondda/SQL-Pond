import sqlite3

con = sqlite3.connect('Sqlite_Northwind.sqlite3')
cur = con.cursor()

#1
for row in cur.execute('SELECT ProductName,UnitPrice FROM Products where CategoryId = 8'):
  print(row)
    
#2
for row in cur.execute('SELECT ProductName,UnitPrice FROM Products where UnitPrice >=5 and UnitPrice <=10'):
  print(row)

#3
for row in cur.execute('SELECT Country,count(Country) FROM Suppliers group by Country order by count(Country)desc'):
  print(row)

#4
for row in cur.execute('SELECT * FROM Customers'):
  print(row)

#5
for row in cur.execute('SELECT ProductName,UnitPrice * UnitsInStock FROM Products where UnitPrice * UnitsInStock > 3000 order by UnitPrice * UnitsInStock desc'):
  print(row)

#6
for row in cur.execute('SELECT ProductName,sum(Products.UnitPrice * Products.UnitsInStock) from Categories left join Products on Products.CategoryID = Categories.CategoryID group by Categories.CategoryID having sum(Products.UnitPrice * Products.UnitsInStock) > 5000 order by sum(Products.UnitPrice * Products.UnitsInStock)'):
  print(row)

#7
for row in cur.execute('SELECT FirstName,LastName,count(OrderID) from Employees left join Orders on Employees.EmployeeID = Orders.EmployeeID group by Employees.EmployeeID order by count(OrderID)'):
  print(row)

#8   29 row
for row in cur.execute('SELECT CompanyName,count(ProductID),sum(Products.UnitPrice)/count(ProductID) from Suppliers left join Products on Suppliers.SupplierId = Products.SupplierId group by Products.SupplierId order by CompanyName'):
  print(row)

#9
sum = 0
for row in cur.execute('SELECT OrdersDetails.OrderID,OrderDate,ShipName,Products.ProductName,OrdersDetails.UnitPrice*OrdersDetails.Quantity from OrdersDetails left join Orders on OrdersDetails.OrderID = Orders.OrderID left join Products on OrdersDetails.ProductId = Products.ProductId where OrdersDetails.OrderID = 10309 order by Products.ProductName'):
  print(row)
  sum += row[-1]
  print(sum)
print(sum*0.07)
print(sum*1.07)

#10  งงนิดนึงผลลัพธ์ไม่ตรงโจทย์
for row in cur.execute('SELECT ShipCountry,count(Orders.OrderID),sum(OrdersDetails.UnitPrice*OrdersDetails.Quantity),sum(OrdersDetails.UnitPrice*OrdersDetails.Quantity)/count(Orders.OrderID) from Orders left join OrdersDetails on OrdersDetails.OrderID =  Orders.OrderID left join Products on Products.ProductID = OrdersDetails.ProductId group by ShipCountry'):
  print(row)
  
#11
for row in cur.execute('SELECT ProductName,UnitPrice,UnitPrice-(select avg(UnitPrice)from Products) from Products where UnitPrice >= (select avg(UnitPrice) from Products) order by UnitPrice desc'):
  print(row)

#12
for row in cur.execute('SELECT ProductName from OrdersDetails left join Products on OrdersDetails.ProductID = Products.ProductID group by Products.ProductID having count(ProductName) > 50'):
  print(row)
