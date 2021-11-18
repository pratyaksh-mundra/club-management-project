def insert():
    c_no = cust_no_field.get()
    c_name = name_field.get()
    c_age = age_field.get()
    c_gen = rad.get()
    c_mail = email_field.get()
    c_ph = ph_field.get()
    c_add = add_field.get()
    mycur = con.cursor()

    new = [(c_no, c_name, c_age, c_gen, c_ph, c_mail, c_add)]
    mycur.executemany(
        "insert into customers(cust_no,cust_name,cust_age,cust_gen,cust_ph,cust_email,cust_add) values(:1,:2,:3,:4,:5,:6,:7)",
        new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    mycur.close()


# function for inserting product details

def insert1():
    p_no1 = p_no_field.get()
    p_name1 = p_name_field.get()
    p_stock1 = p_stock_field.get()
    p_price1 = p_price_field.get()
    cur = con.cursor()
    new = [(p_no1, p_name1, p_stock1, p_price1)]
    cur.executemany("insert into products(p_id,p_name,p_stock,p_price) values(:1,:2,:3,:4)", new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    cur.close()


# function for inserting bill details

def billinsert():
    bill_pid = bill1.get()
    bill_cid = bill2.get()
    bill_qty = bill3.get()
    bill_price = bill4.get()
    cur = con.cursor()
    new = [(bill_pid, bill_cid, bill_qty, bill_price)]
    cur.executemany("insert into billing(p_id,c_id,p_price,qty) values(:1,:2,:3,:4)", new)
    con.commit()
    messagebox.showinfo("successful!", "inserted")
    cur.close()


# function for displaying customer details

def display():
    print("CID|C_NAME|C_AGE|GENDER|PHONE NO|EMAIL|ADD")
    print()
    curr = con.cursor()
    curr.execute("select * from customers")
    data = curr.fetchall()
    for row in data:
        print(row)
    print()
    curr.close()


# function for displaying product details

def display1():
    print("P_ID P_NAME  STOCK  PRICE")
    print()
    cury = con.cursor()
    cury.execute("select * from products")
    data = cury.fetchall()
    for row in data:
        print(row)
    print()
    cury.close()


# function for deleting customer details

def delete():
    c_id = cust_no_field.get()
    cur2 = con.cursor()
    cur2.execute("delete from customers where cust_no=" + str(c_id))
    con.commit()
    messagebox.showinfo("successful!", "deleted")
    cur2.close()


# function for deleting product details

def delete1():
    p_id2 = p_no_field.get()
    curry = con.cursor()
    curry.execute("delete from products where p_id=" + str(p_id2))
    con.commit()
    messagebox.showinfo("successful!", "deleted")
    curry.close()


# function for updating customer ID

def u1():
    c_i = cust_no_field.get()
    c_i_1 = name1_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_no= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    if c_i_1 != NULL:
        messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer name

def u2():
    c_i = cust_no_field.get()
    c_i_1 = name2_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_name= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer age

def u3():
    c_i = cust_no_field.get()
    c_i_1 = name3_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_age= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    if c_i_1 is None:
        messagebox.showinfo("error!", " not updated")
    else:
        messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer phone no

def u4():
    c_i = cust_no_field.get()
    c_i_1 = name4_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_ph= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer email ID

def u5():
    c_i = cust_no_field.get()
    c_i_1 = name5_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_email= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating customer address

def u6():
    c_i = cust_no_field.get()
    c_i_1 = name6_field.get()
    cur5 = con.cursor()
    statement = 'update customers set cust_add= :1 where cust_no= :2'
    cur5.execute(statement, (c_i_1, c_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()


# function for updating product stock

def stockupdate():
    p_i = p_no_field.get()
    p_i_1 = stock_e.get()
    cur5 = con.cursor()
    statement = 'update products set p_stock= :1 where p_id= :2'
    cur5.execute(statement, (p_i_1, p_i))
    con.commit()
    messagebox.showinfo("successful!", "updated")
    cur5.close()