from flask import Flask, render_template,request,session,redirect
from DBConnection import Db



app = Flask(__name__)

app.secret_key="sdvfndsfs"
@app.route('/ab')
def hello_world():
    return 'Hello World!'

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/loginpost',methods=['post'])
def loginpost():
    uname=request.form['username']
    password = request.form['password']

    db=Db()
    qry="SELECT * FROM `login` WHERE `uname`='"+uname+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is None:
        return "<script>alert('Invalid Username and Password');window.loaction='/'</script>"
    else:
        session["lid"]=str(res["loginid"])
        if res['usertype']=="admin":
            # return render_template("Admin/home.html")
              return redirect('/adminindex')
        elif res['usertype']=="barbershop":
            # return render_template("Barber Shop/home.html")
            return redirect('/barberindex')
        elif res['usertype']=="user":
            # return render_template("User/home.html")
              return redirect('/userindex')
        else:
            return "<script>alert('Invalid Username and Password');window.loaction='/'</script>"

@app.route('/adminindex')
def adminindex():
    return render_template('Admin/home.html')

@app.route('/barberindex')
def barberindex():
    return render_template('Barber Shop/home.html')

@app.route('/userindex')
def userindex():
    return render_template('User/home.html')



@app.route('/View_and_Approve_Barbershop')
def View_and_Approve_Barbershop():
    db = Db()
    qry = "SELECT * FROM `barbershop` WHERE `status`='pending'"
    res = db.select(qry)
    return render_template("Admin/View and Approve Barbershop.html",data=res)

@app.route('/approve_shop/<id>')
def approve_shop(id):
    d = Db()
    qry = "UPDATE `barbershop` SET `status`='approved' WHERE `loginid`='"+str(id)+"'"
    res =d.update(qry)
    qry1 = "UPDATE `login` SET `usertype`='barbershop' WHERE `loginid`='"+str(id)+"'"
    res=d.update(qry1)
    return '''<script>alert('Approved');window.location='/View_and_Approve_Barbershop'</script>'''

@app.route('/reject_shop/<id>')
def reject_shop(id):
    d = Db()
    qry = "UPDATE `barbershop` SET `status`='rejected' WHERE `loginid`='"+str(id)+"'"
    res =d.update(qry)
    qry1 = "UPDATE `login` SET `usertype`='rejected' WHERE `loginid`='"+str(id)+"'"
    res=d.update(qry1)
    return '''<script>alert('Rejected');window.location='/View_and_Approve_Barbershop'</script>'''

@app.route('/search_pbarber',methods=['post'])
def search_pbarber():
    search=request.form['search']
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `shopname` LIKE '%"+search+"%' AND `status`='pending'"
    res=db.select(qry)
    return render_template("Admin/View and Approve Barbershop.html",data=res)


@app.route('/View_Approved_Shops')
def View_Approved_Shops():
    db = Db()
    qry = "select * from Barbershop where BarberShop.status='approved'"
    res = db.select(qry)
    return render_template("Admin/View Approved Shops.html",data=res)

@app.route('/reject_approved_shop/<id>')
def reject_approved_shop(id):
    d = Db()
    qry = "UPDATE `barbershop` SET `status`='rejected' WHERE `loginid`='"+id+"'"
    res =d.update(qry)
    qry1 = "UPDATE `login` SET `usertype`='rejected' WHERE `loginid`='"+id+"'"
    res=d.update(qry1)
    return '''<script>alert('Rejected');window.location='/View_Approved_Shops'</script>'''

@app.route('/search_abarber',methods=['post'])
def search_abarber():
    search=request.form['search']
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `shopname` LIKE '%"+search+"%' AND `status`='approved'"
    res=db.select(qry)
    return render_template("Admin/View Approved Shops.html",data=res)

@app.route('/View_Rejected_Shops')
def View_Rejected_Shops():
    db = Db()
    qry = "select * from Barbershop where BarberShop.status='rejected'"
    res = db.select(qry)
    return render_template("Admin/View Rejected Shops.html",data=res)

@app.route('/search_rbarber',methods=['post'])
def search_rbarber():
    search=request.form['search']
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `shopname` LIKE '%"+search+"%' AND `status`='rejected'"
    res=db.select(qry)
    return render_template("Admin/View Rejected Shops.html",data=res)


@app.route('/View_Ratings/<id>')
def View_Ratings(id):
    db = Db()
    qry = "SELECT * FROM `rating` INNER JOIN `user` ON `rating`.`userid`=`user`.`loginid` INNER JOIN `barbershop` ON `barbershop`.`loginid`=`rating`.`barbershopid`"
    res = db.select(qry)
    return render_template("Admin/View Ratings.html",data=res)

@app.route('/View_User')
def View_User():
    db = Db()
    qry = "select * from User"
    res = db.select(qry)
    return render_template("Admin/View User.html",data=res)

@app.route('/search_user',methods=['post'])
def search_user():
    search=request.form['search']
    db=Db()
    qry="SELECT * FROM `user` WHERE `name` LIKE '%"+search+"%'"
    res=db.select(qry)
    return render_template("Admin/View User.html",data=res)

@app.route('/View_Complaints')
def View_Complaints():
    db = Db()
    qry = "SELECT complaints.*,`barbershop`.`shopname`,`barbershop`.`loginid`,`user`.`name` FROM `complaints` INNER JOIN `user` ON `user`.`loginid`=`complaints`.`userid` INNER JOIN `barbershop` ON `barbershop`.`loginid`=`complaints`.`barbershopid`"
    res = db.select(qry)
    return render_template("Admin/View Complaints.html",data=res)

@app.route('/Send_Reply/<id>')
def Send_Reply(id):
    db=Db()
    qry="SELECT * FROM `complaints` WHERE `complantid`='"+str(id)+"'"
    res=db.selectOne(qry)
    return render_template("Admin/Send Reply.html",data=res)

@app.route('/sendreplypost',methods=['post'])
def sendreplypost():
    id = request.form['h1']
    reply = request.form['textarea']
    d = Db()
    qry = "UPDATE `complaints` SET `reply`='"+reply+"', `status`='replied' WHERE `complantid`='"+str(id)+"'"
    res = d.update(qry)
    return "<script>alert('Replied');window.location='/View_Complaints'</script>"


###################################################################################################

@app.route('/Change_Password')
def Change_Password():
    return render_template("Barber Shop/Change Password.html")
@app.route('/chanepasspost',methods=['post'])
def changeppasspost():
    old=request.form['old']
    newp=request.form['newp']
    cnf = request.form['confirm']

    db=Db()
    qry="SELECT * FROM `login` WHERE `password`='"+old+"' "
    res=db.selectOne(qry)
    if res is not None:
        if newp==cnf:
            qry="UPDATE `login` SET `password`='"+newp+"' WHERE `loginid`='"+str(session['lid'])+"'"
            res=db.update(qry)
            return "<script>alert('Password Changed');window.location='/'</script>"
        else:
            return  "<script>alert('Password Mismatched');window.location='/Change_Password'</script>"
    else:
        return "<script>alert('Current Password Must Be Valid');window.location='/Change_Password'</script>"


@app.route('/Edit_Profile')
def Edit_Profile():
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `barbershop`.`loginid`='"+str(session["lid"])+"'"
    res=db.selectOne(qry)
    return render_template("Barber Shop/Edit Profile.html",data=res)

@app.route('/editprofilepost',methods=['post'])
def editprofilepost():
    shopname=request.form['shopname']
    shoptype=request.form['shoptype']
    place=request.form['place']
    city=request.form['city']
    state=request.form['state']
    pincode=request.form['pincode']
    about=request.form['about']
    email=request.form['email']
    phone=request.form['phone']
    photo=request.files['photo']

    path = "C:\\Users\\Savad\\PycharmProjects\\Belleza\\static\\photo\\"
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    photo.save(path + filename)

    b = "/static/photo/" + filename

    if request.files != None:
        if photo.filename != "":
            qry="UPDATE `barbershop` SET `shopname`='"+shopname+"',`shoptype`='"+shoptype+"',`place`='"+place+"',`city`='"+city+"',`state`='"+state+"',`pincode`='"+pincode+"',`about`='"+about+"',`email`='"+email+"',`phone`='"+phone+"',`photo`='"+b+"'  WHERE `barbershop`.`loginid`='"+str(session["lid"])+"' "
            db=Db()
            db.update(qry)
            qry2 = "UPDATE `login` SET `uname` ='" + email + "' WHERE `loginid`='" + str(session['lid']) + "'"
            db.update(qry2)
        else:
            qry="UPDATE `barbershop` SET `shopname`='"+shopname+"',`shoptype`='"+shoptype+"',`place`='"+place+"',`city`='"+city+"',`state`='"+state+"',`pincode`='"+pincode+"',`about`='"+about+"',`email`='"+email+"',`phone`='"+phone+"'  WHERE `barbershop`.`loginid`='"+str(session["lid"])+"' "
            db=Db()
            db.update(qry)
            qry2 = "UPDATE `login` SET `uname` ='" + email + "' WHERE `loginid`='" + str(session['lid']) + "'"
            db.update(qry2)

    else:
        qry="UPDATE `barbershop` SET `shopname`='"+shopname+"',`shoptype`='"+shoptype+"',`place`='"+place+"',`city`='"+city+"',`state`='"+state+"',`pincode`='"+pincode+"',`about`='"+about+"',`email`='"+email+"',`phone`='"+phone+"'  WHERE `barbershop`.`loginid`='"+str(session["lid"])+"' "
        db=Db()
        db.update(qry)
        qry2 = "UPDATE `login` SET `uname` ='" + email + "' WHERE `loginid`='" + str(session['lid']) + "'"
        db.update(qry2)

    return "<script>alert('Successfully Updtaed');window.location='/View_Profile'</script>"

@app.route('/View_Services')
def View_Services():
    db=Db()
    qry="SELECT * FROM `services` WHERE `services`.`barbershopid`='"+str(session["lid"])+"'"
    res=db.select(qry)
    return render_template("Barber Shop/View Services.html",data=res)

@app.route('/deleteservice/<id>')
def deleteservice(id):
    db=Db()
    qry="DELETE FROM  `services` WHERE serviceid='"+str(id)+"'"
    res=db.delete(qry)
    return "<script>alert('Deleted');window.location='/View_Services'</script>"

@app.route('/editsercives/<id>')
def editservices(id):
    db=Db()
    qry="SELECT * FROM `services` WHERE `barbershopid`='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    return render_template("Barber Shop/Edit_Services.html",data=res)

@app.route('/editservicepost',methods=['post'])
def editservicepost():
    servicename=request.form['servicename']
    servicerate=request.form['servicerate']
    photo=request.files['photo']
    description=request.form['description']

    path="C:\\Users\\Savad\\PycharmProjects\\Belleza\\static\\photo\\"
    from datetime import datetime
    filename=datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    photo.save(path +filename)
    e="/static/photo" + filename

    if request.files != None:
        if photo.filename != "":
            db=Db()
            qry="UPDATE `services` SET `servicename`='"+servicename+"',`photo`='"+e+"',`servicerate`='"+servicerate+"',`description`='"+description+"' WHERE `barbershopid`='"+str(session["lid"])+"'"
            res=db.update(qry)
            return "<script>alert('Edited Successfully');window.location='/View_Services'</script>"
        else:
            db = Db()
            qry = "UPDATE `services` SET `servicename`='" + servicename + "',`servicerate`='" + servicerate + "',`description`='" + description + "' WHERE `barbershopid`='"+str(session["lid"])+"'"
            res = db.update(qry)
            return "<script>alert('Edited Successfully');window.location='/View_Services'</script>"
    else:
        db = Db()
        qry = "UPDATE `services` SET `servicename`='" + servicename + "',`servicerate`='" + servicerate + "',`description`='" + description + "' WHERE `barbershopid`='" + str(    session["lid"]) + "'"
        res = db.update(qry)
        return "<script>alert('Edited Successfully');window.location='/View_Services'</script>"


@app.route('/Add_Service')
def Add_Service():

    return render_template("Barber Shop/Add_service.html")

@app.route('/addservice',methods=['post'])
def addservice():
    servicename=request.form['servicename']
    photo=request.files['photo']
    servicerate=request.form['servicerate']
    description=request.form['description']

    path = "C:\\Users\\Savad\\PycharmProjects\\Belleza\\static\\photo\\"
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    photo.save(path + filename)

    p = "/static/photo/" + filename

    qry="INSERT INTO `services` (`servicename`,`photo`,`servicerate`,`description`,`barbershopid`) VALUES ('"+servicename+"','"+p+"','"+servicerate+"','"+description+"','"+session['lid']+"')"
    db=Db()
    db.insert(qry)

    return "<script>alert('Added Successfully');window.location='/View_Services'</script>"


@app.route('/Sign_Up')
def Sign_Up():
    return render_template("Barber Shop/signup.html")


@app.route("/barbershopsignuppost",methods=['post'])
def barbershopsignuppost():
    shopname=request.form["shopname"]
    shoptype=request.form["shoptype"]
    place = request.form["place"]
    city = request.form["city"]
    state = request.form["state"]
    pincode = request.form["pincode"]
    about = request.form["about"]
    email = request.form["email"]
    phone = request.form["phone"]
    photo = request.files["photo"]
    password = request.form["password"]

    path="C:\\Users\\Savad\\PycharmProjects\\Belleza\\static\\photo\\"
    from datetime import datetime
    filename=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    photo.save(path+filename)

    s="/static/photo/"+ filename

    qry = "INSERT INTO `login` (`uname`,`password`,`usertype`) VALUES ('" + email + "','" + password + "','pending')"

    db = Db()
    lid = db.insert(qry)

    qry="INSERT INTO `barbershop` (`shopname`,`shoptype`,`place`,`city`,`state`,`pincode`,`about`,`email`,`phone`,`photo`,status,loginid) VALUES ('"+shopname+"','"+shoptype+"','"+place+"','"+city+"','"+state+"','"+pincode+"','"+about+"','"+email+"','"+phone+"','"+s+"','pending','"+str(lid)+"')"
    db.insert(qry)

    return "<script>alert('Registered successfully');window.location='/'</script>"



@app.route('/View_Booking')
def View_Booking():
    db=Db()
    qry="SELECT `slot`.`from`,`slot`.`to`,`user`.*,`booking`.* FROM `booking` INNER JOIN `slot` ON `slot`.`barbershopid`=`booking`.`barbershopid` AND `slot`.`slotid`=`booking`.`slotid` INNER JOIN `user` ON `user`.`loginid` = `booking`.`userid`  WHERE `booking`.`barbershopid`='"+str(session["lid"])+"'"
    res=db.select(qry)
    return render_template("Barber Shop/View Booking.html",data=res)

@app.route('/acceptbooking/<id>')
def acceptbooking(id):
    db=Db()
    qry="UPDATE `booking` SET `status`='accepted' WHERE`bookingid`='"+str(id)+"'"
    res=db.update(qry)
    return "<script>alert('Accepted');window.location='/View_Booking'</script>"


@app.route('/rejectbooking/<id>')
def rejectbooking(id):
    db=Db()
    qry="UPDATE `booking` SET `status`='rejected' WHERE`bookingid`='"+str(id)+"'"
    res=db.update(qry)
    return "<script>alert('Rejected');window.location='/View_Booking'</script>"



@app.route('/View_Profile')
def View_Profile():
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `barbershop`.`loginid`='"+str(session["lid"])+"'"
    res=db.selectOne(qry)

    return render_template("Barber Shop/viewprofile.html",data=res)


@app.route('/View_Ratings_BarberShop')
def View_Ratings_BarberShop():
    db=Db()
    qry="SELECT * FROM `user` INNER JOIN `rating` ON `rating`.`userid`=`user`.`loginid` INNER JOIN `barbershop` ON `barbershop`.`loginid`=`rating`.`barbershopid` WHERE `barbershop`.`loginid`='"+str(session["lid"])+"' "
    res=db.select(qry)
    return render_template("Barber Shop/View Ratings.html",data=res)

@app.route('/View_Slot')
def View_Slot():
    db=Db()
    qry="SELECT * FROM `slot` WHERE `barbershopid`='"+str(session['lid'])+"' "
    res=db.select(qry)

    return render_template("Barber Shop/View Slot.html",data=res)

@app.route('/deleteslot/<id>')
def deleteslot(id):
    db=Db()
    qry="DELETE FROM  `slot` WHERE slotid='"+str(id)+"'"
    res=db.delete(qry)
    return "<script>alert('Deleted');window.location='/View_Slot'</script>"

@app.route('/Create_Slot')
def Create_Slot():

    return render_template("Barber Shop/Create_Slot.html")

@app.route('/Create_slot_post',methods=['post'])
def Create_slot_post():
    f=request.form['from']
    to=request.form['to']
    db = Db()
    qry = "INSERT INTO `slot` (`from`,`to`,`barbershopid`) VALUES('"+f+"','"+to+"','"+str(session['lid'])+"')"
    db.insert(qry)

    return "<script>alert:('Added Successfully');window.location='/View_Slot#about'</script>"


#############################################################################################################


@app.route('/Booking/<id>')
def Booking(id):
    session["shopid"]=id
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `barbershop`.`loginid`='"+str(id)+"'"
    res=db.selectOne(qry)
    qry2="SELECT * FROM `services` WHERE `services`.`barbershopid`='"+str(id)+"'"
    res2=db.select(qry2)
    qry3="SELECT * FROM `rating` INNER JOIN `barbershop` ON `barbershop`.`loginid`=`rating`.`barbershopid` WHERE `rating`.`barbershopid`='"+str(id)+"'"
    res3=db.select(qry3)
    qry4 = "SELECT * FROM `slot` WHERE `barbershopid`='" + str(id) + "' and  `slotid` NOT IN (SELECT `slotid` FROM `booking` WHERE `date`=CURDATE())"
    res4 = db.select(qry4)
    return render_template("User/Booking.html",data=res,data2=res2,data3=res3,data4=res4)



@app.route('/Bookings')
def Bookings():
    id=str(session["shopid"])
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `barbershop`.`loginid`='"+str(id)+"'"
    res=db.selectOne(qry)
    qry2="SELECT * FROM `services` WHERE `services`.`barbershopid`='"+str(id)+"'"
    res2=db.select(qry2)
    qry3="SELECT * FROM `rating` INNER JOIN `user` ON `user`.`loginid`=`rating`.`userid` WHERE `rating`.`barbershopid`='"+str(id)+"'"
    res3=db.select(qry3)
    qry4 = "SELECT * FROM `slot` WHERE `barbershopid`='" + str(id) + "' and  `slotid` NOT IN (SELECT `slotid` FROM `booking` WHERE `date`=CURDATE())"
    res4 = db.select(qry4)
    return render_template("User/Booking.html",data=res,data2=res2,data3=res3,data4=res4)


@app.route('/bookingpost',methods=['post'])
def bookingpost():
    button=request.form['button']
    shopid=str(session["shopid"])
    st=request.form["st"]
    db = Db()
    if button =="Book":
        services=request.form.getlist("checkbox")
        print(services)
        qry="INSERT INTO `booking`(`userid`,`date`,`time`,`total amount`,`status`,`barbershopid`,`slotid`)VALUES('"+str(session["lid"])+"',CURDATE(),CURTIME(),'','pending','"+str(shopid)+"','"+st+"')"
        bookid=str(db.insert(qry))
        qry5=""
        # q="SELECT COUNT(`bookingid`) AS cnt FROM `booking` WHERE `barbershopid`='"+shopid+"' "
        # r=db.selectOne(q)
        sr=0
        for i in services:
            qry2="SELECT `servicerate` AS sr FROM `services` WHERE `serviceid`='"+str(i)+"'"
            res=db.selectOne(qry2)
            sr+=float(res["sr"])
            qry3="INSERT INTO `bookingsub`(`bookingid`,`serviceid`)VALUES('"+bookid+"','"+str(i)+"')"
            db.insert(qry3)
        qry4="UPDATE `booking` SET `total amount`='"+str(sr)+"' WHERE`bookingid`='"+bookid+"'"
        db.update(qry4)
        return "<script>alert('Booked Succesfully');window.location='/Bookings'</script>"
    else:
        review=request.form['review']
        pp=request.form["aa"]
        rating=pp
        db = Db()
        qry = "INSERT INTO `rating`(`userid`,`barbershopid`,`review`,`rating`,`date`) VALUES('"+str(session["lid"])+"','"+str(shopid)+"','"+review+"','"+rating+"',CURDATE())"
        res = db.insert(qry)
        return "<script>alert('Review Send Successfully');window.location='/Bookings'</script>"
    # else:
    #     return "<script>alert('Notavailable');window.location='/Bookings'</script>"

@app.route('/Change_Password_User')
def Change_Password_User():
    return render_template("User/Change Password.html")

@app.route('/changepassuserpost',methods=['post'])
def changeppassuserpost():
    old=request.form['old']
    newp=request.form['newp']
    cnf = request.form['confirm']
    db=Db()
    qry="SELECT * FROM `login` WHERE `password`='"+old+"' "
    res=db.selectOne(qry)
    if res is not None:
        if newp==cnf:
            qry="UPDATE `login` SET `password`='"+newp+"' WHERE `loginid`='"+str(session['lid'])+"'"
            res=db.update(qry)
            return "<script>alert('Password Changed');window.location='/'</script>"
        else:
            return  "<script>alert('Password Mismatched');window.location='/Change_Password_User'</script>"
    else:
        return "<script>alert('Current Password Must Be Valid');window.location='/Change_Password_User'</script>"



@app.route('/Edit_Profile_User')
def Edit_Profile_User():
    db=Db()
    qry="SELECT * FROM `user` WHERE `user`.`loginid`='"+str(session["lid"])+"'"
    res=db.selectOne(qry)
    return render_template("User/Edit Profile.html",data=res)

@app.route('/editprofileuserpost',methods=['post'])
def editprofileuserpost():
    name = request.form["name"]
    gender = request.form["gender"]
    place = request.form["place"]
    city = request.form["city"]
    state = request.form["state"]
    pincode = request.form["pincode"]
    email = request.form["email"]
    phone = request.form["phone"]
    photo = request.files["photo"]

    path = "C:\\Users\\Savad\\PycharmProjects\\Belleza\\static\\photo\\"
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    photo.save(path + filename)

    u = "/static/photo/" + filename

    if request.files != None:
        if photo.filename != "":
            qry = "UPDATE `user` SET `name`='"+name+"',`gender`='"+gender+"',`place`='"+place+"',`city`='"+place+"',`state`='"+state+"',`pincode`='"+pincode+"',`email`='"+email+"',`phone`='"+phone+"',`photo`='"+u+"' WHERE `user`.`loginid`='"+str(session["lid"])+"' "
            db = Db()
            db.update(qry)
            qry2="UPDATE `login` SET `uname` ='"+email+"' WHERE `loginid`='"+str(session['lid'])+"'"
            db.update(qry2)
        else:
            qry = "UPDATE `user` SET `name`='"+name+"',`gender`='"+gender+"',`place`='"+place+"',`city`='"+place+"',`state`='"+state+"',`pincode`='"+pincode+"',`email`='"+email+"',`phone`='"+phone+"' WHERE `user`.`loginid`='"+str(session["lid"])+"'"
            db = Db()
            db.update(qry)
            qry2 = "UPDATE `login` SET `uname` ='" + email + "' WHERE `loginid`='" + str(session['lid']) + "'"
            db.update(qry2)

    else:
            qry = "UPDATE `user` SET `name`='"+name+"',`gender`='"+gender+"',`place`='"+place+"',`city`='"+place+"',`state`='"+state+"',`pincode`='"+pincode+"',`email`='"+email+"',`phone`='"+phone+"' WHERE `user`.`loginid`='"+str(session["lid"])+"'"
            db = Db()
            db.update(qry)
            qry2 = "UPDATE `login` SET `uname` ='" + email + "' WHERE `loginid`='" + str(session['lid']) + "'"
            db.update(qry2)

    return "<script>alert('Successfully Updtaed');window.location='/View_Profile_User'</script>"

@app.route('/Send_Complaint/<id>')
def Send_Complaint(id):
    db=Db()
    qry="SELECT * FROM `barbershop` WHERE `barbershopid`='"+id+"' "
    res=db.selectOne(qry)
    return render_template("User/Send Complaint.html",data=res)

@app.route("/sendcomplaint",methods=['post'])
def sendcomplaint():
    id=request.form['h1']
    complaint=request.form['complaint']
    db=Db()
    qry="INSERT INTO `complaints` (`complaint`,`date`,`userid`,`reply`,`status`,`barbershopid`) VALUES('"+complaint+"',CURDATE(),'"+str(session["lid"])+"','pending','pending','"+str(id)+"')"
    res=db.insert(qry)

    return "<script>alert('Complaint Registered Successfully');window.location='/View_BarberShops'</script>"



@app.route('/SignUp_User')
def SignUp_User():
    return render_template("User/sign up.html")


@app.route("/usersignuppost",methods=['post'])
def usersignuppost():
    name=request.form["name"]
    gender = request.form["RadioGroup1"]
    place = request.form["place"]
    city = request.form["city"]
    state = request.form["state"]
    pincode = request.form["pincode"]
    email = request.form["email"]
    phone = request.form["phone"]
    photo = request.files["photo"]
    password = request.form["password"]

    path = "C:\\Users\\Savad\\PycharmProjects\\Belleza\\static\\photo\\"
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    photo.save(path + filename)

    u = "/static/photo/" + filename

    qry="INSERT INTO `login` (`uname`,`password`,`usertype`) VALUES ('"+email+"','"+password+"','user')"
    db=Db()
    lid=db.insert(qry)
    qry="INSERT INTO `user` (`name`,`gender`,`place`,`city`,`state`,`pincode`,`email`,`phone`,`photo`,loginid) VALUES ('"+name+"','"+gender+"','"+place+"','"+city+"','"+state+"','"+pincode+"','"+email+"','"+phone+"','"+u+"','"+str(lid)+"')"
    db.insert(qry)

    return "<script>alert('Registered successfully');window.location='/'</script>"

@app.route('/View_BarberShops')
def View_BarberShops():
    db=Db()
    qry="SELECT `barbershop`.*,`user`.`place` FROM `barbershop` INNER JOIN `user` ON `barbershop`.`place`=`user`.`place`  WHERE `barbershop`.`place`=`user`.`place`"
    res=db.select(qry)

    return render_template("User/View BarberShops.html",data=res)


@app.route('/View_Booking_User')
def View_Booking_User():
    db=Db()
    qry="SELECT booking.*,`slot`.`from`,`slot`.`to`,user.*,barbershop.*,booking.status AS s FROM `booking` INNER JOIN `user` ON `user`.`loginid` = `booking`.`userid` INNER JOIN `slot` ON `slot`.`barbershopid`=`booking`.`barbershopid` AND `slot`.`slotid`=`booking`.`slotid` INNER JOIN  `barbershop` ON `barbershop`.`loginid`=`booking`.barbershopid WHERE `user`.`loginid`='"+str(session['lid'])+"' AND `booking`.`status`='accepted' "
    res=db.select(qry)
    return render_template("User/View Booking.html",data=res)

@app.route('/cancelbooking/<id>')
def cancelbooking(id):
    db=Db()
    qry="DELETE FROM  `booking` WHERE bookingid='"+str(id)+"'"
    res=db.delete(qry)
    return "<script>alert('Booking Cancelled');window.location='/View_Booking_User'</script>"


@app.route('/View_Complaints_User')
def View_Complaints_User():
    db=Db()
    qry="SELECT complaints.*,`barbershop`.`shopname`,`barbershop`.`loginid`,`user`.`name` FROM `complaints` INNER JOIN `user` ON `user`.`loginid`=`complaints`.`userid` INNER JOIN `barbershop` ON `barbershop`.`loginid`=`complaints`.`barbershopid` WHERE `user`.`loginid`='"+str(session["lid"])+"'"
    res=db.select(qry)
    return render_template("User/View Complaints.html",data=res)


@app.route('/View_Profile_User',)
def View_Profile_User():
    db=Db()
    qry="select * from user WHERE `user`.`loginid`='"+str(session["lid"])+"'"
    res=db.selectOne(qry)
    return render_template("User/viewprofile.html",data=res)





if __name__ == '__main__':
    app.run(debug=True,port=4999)
