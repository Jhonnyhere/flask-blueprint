from flask import Blueprint, render_template, url_for, flash, redirect, request,Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
from .extensions import db
from .models import User,Contact,students,sql,Product
from flask_mail import Mail,Message 


main = Blueprint('main', __name__)
# mail = Mail(main)

@main.route("/")
def index():
    return render_template('index.html')

 
@main.route('/show')
def show_all():
   return render_template('show_all.html', students = students.query.all() )


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        clientdata=Contact(name=name, email=email,message=message)                 
        db.session.add(clientdata)
        db.session.commit()
        # msg = Message("Hello",
        #           sender="from@example.com",
        #           recipients=[main.config['MAIL_USERNAME']])
        # msg.body = "testing"
        # msg.html = "<b>testing</b>"
        # mail.send(msg)
        flash('Record was successfully added')
        return redirect(url_for('show_all'))
    return render_template('contact.html')

@main.route('/products')
def product():
    return render_template('product.html', product = Product.query.all())


@main.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method == 'POST':
        brand = request.form.get('brand')
        model = request.form.get('model')
        images = request.form.get('images')
        price = request.form.get('price')
        
        mobiledata = Product(brand=brand, model=model,images=images,price=price)
        db.session.add(mobiledata)
        db.session.commit()
        flash('succesfully added')
        return redirect(url_for('product'))
    return render_template('add_user.html')

@main.route("/edit_user/<string:id>",methods=['POST','GET'])
def edit_user(id):
    if request.method=='POST':
        brand = request.form.get('brand')
        model = request.form.get('model')
        images = request.form.get('images')
        price = request.form.get('price')
        
        mobiledata = Product(brand=brand, model=model,images=images,price=price)
        db.session.update(mobiledata)
        db.session.commit()
        flash('succesfully updated')
        return redirect(url_for('product'))
    return render_template('edit_user.html')

# @main.route("/delete_user/<string:uid>",methods=['GET'])
# def delete_user(id):
    
        
@main.route("/price")
def price():
    return render_template("price.html")

@main.route("/services")
def services():
    # j = open('video.json')

    # videos = json.load(j) # or from database mysql
    # title="My videos"
    return render_template('services.html')


@main.route("/subscribe")
@login_required
def subscribe():
    return render_template("subscribe.html")


@main.route("/team")
def team():
    return render_template("team.html")


@main.route("/works")
@login_required
def works():
    return render_template("works.html")

@main.route("/about")    
def about():
    return render_template("about.html")

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


    
     
# @main.route("/product")
# def product():
#     con = sql.connect("db_web.db")
#     con.row_factory = sql.Row
#     cur = con.cursor()
#     cur.execute("select * from Mobiles")
#     data = cur.fetchall()
#     return render_template('product.html', datas=data)

# @main.route("/add_user",methods=['POST','GET'])
# def add_user():
#     if request.method == 'POST':
#         brand = request.form['brand']
#         model = request.form['model']
#         images = request.form['images']
#         price = request.form['price']
#         con = sql.connect("db_web.db")
#         cur=con.cursor()
#         cur.execute('insert into Mobiles(BRAND,MODEL,IMAGES,PRICE) values(?,?,?,?)', (brand,model,images,price))
#         con.commit()
#         flash('User Added','success')
#         return redirect(url_for("product"))
#     return render_template("add_user.html")

# @main.route("/edit_user/<string:uid>",methods=['POST','GET'])
# def edit_user(id):
#     if request.method=='POST':
#         brand = request.form['brand']
#         model = request.form['model']
#         images = request.form['images']
#         price = request.form['price']
#         con = sql.connect("db_web.db")
#         cur=con.cursor()
#         cur.execute("update users set BRAND=?,MODEL=?,IMAGES=?,PRICE=? where ID=?",(brand,model,images,price))
#         con.commit()
#         flash('User Updated','success')
#         return redirect(url_for("product"))
#     con=sql.connect("db_web.db")
#     con.row_factory=sql.Row
#     cur=con.cursor()
#     cur.execute("select * from Mobiles where ID=?",(id,))
#     data=cur.fetchone()
#     return render_template("edit_user.html",datas=data)

# @main.route("/delete_user/<string:uid>",methods=['GET'])
# def delete_user(id):
#     con=sql.connect("db_web.db")
#     cur=con.cursor()
#     cur.execute("delete from Mobiles where ID=?",(id,))
#     con.commit()
#     flash('User Deleted','warning')
#     return redirect(url_for("product"))

# if __name__ =="__main__":
#     db.create_all()
#     main.run(debug=True)