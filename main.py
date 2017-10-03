from flask import Flask, request, redirect, render_template
import cgi

app=Flask(__name__)
app.config['DEBUG']=True


@app.route("/", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    error=""
    perror=""
    verror=""
    email_error=""
    
    # look inside the request to figure out what the user typed
    if  username=="": 
        error="'{0}'Enter your username".format(username)
        username=""
    else:
        if  len(username) > 20:
            error="Please enter your username less than 20 character"
            username=""
        else:
            if  len(username) <3:
                error="Please enter your username more than character"
                username=""
            else:
                username=username    
    
    if  password == '':
        perror="'{0} Please enter your password".format(password)
        
        
    else:
        if len(password) > 20:
            perror="Enter your password not more than 20 char"
            password=""
        else:
            if len(password) < 3:
                perror="Enter your password not less than 3 char"
                password=""
            else:
                password=password
        

    if  verify=="":
        verror="'{0}' password re-enter is empty".format(verify)
        
    else:
        if  verify!=password:
            perror="Password did not match"
        else:    
            verify=verify


    if email != "":
        
    
        if " " in email:
            email_error="wrong email address" 
           
        else:
            if len(email)<3 or len(email)>20:
                email_error="enter email is less than 3 character or more than 20 char"
               
            else:
                if "@" in email and "." in email:
                    email=email
                
    if email=="":
        email=email        
    
        
    if not error and not perror and not verror and not email_error:
       return render_template('welcome.html',username=username)
    else:
        return render_template("signup.html",
                    username=username,password=password,
                    verify=verify,email=email,
                    error=error,perror=perror,verror=verror,
                    email_error=email_error)
@app.route("/")
def index():
    
    return render_template('signup.html')

    

    

app.run()
