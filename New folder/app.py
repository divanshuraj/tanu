#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def xyz():
     return render_template('d:sum2.html')
app.route('data',methods=['POST'])
def obj():
    num1=request.form['a']
    num2=request.form['b']
    total=int(num1)+int(num2)
    return render_template('d:sum2.html',tanu=total)
if __name__ == '__main__':
    app.run()    


# In[ ]:




