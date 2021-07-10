import pickle

import sklearn

file=open('static/finalized.sav','rb')
loaded_model=pickle.load(file)


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def fkjfkjf():
    return render_template('new.html')
@app.route('/info',methods=['GET','POST'])
def fkjfk():
    if(request.method=='POST'):
        print("Asdfasdfa")
        
        distance=request.form['dis']
        name=request.form['name']
        surge=request.form['surge']
        source=request.form['source']
        desti=request.form['desti']
        
        
        
        # result = loaded_model.score(X_test, Y_test)
       
        # aa=f"{distance},{name},{surge},{source},{desti}"


        res=loaded_model.predict([[distance,name,surge,source,desti]])
        
        return render_template('new.html',pre=res)
        
if __name__=='__main__':
    app.run()
