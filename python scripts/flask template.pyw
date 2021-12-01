import os
from tkinter import *

root = Tk()
a = StringVar()


def DoSomethingWithInput(a):
    di = a
    x = 1
    while True:
        if os.path.isdir(di):
            di = di + str(x)
            x = x + 1
        else:
            break
    os.mkdir(di)
    os.chdir(di)
    fi = open('app.py', 'w')
    p = '''
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)'''
    fi.write(p)
    fi.close()
    os.mkdir("templates")
    os.chdir('templates')
    fil = open('template.html', 'w')
    d = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
 <head>
     <meta charset="utf-8">
     <link rel="stylesheet" href="static/css/main.css">
     <title></title>
 </head>
<body>      
</body>
</html>'''
    fil.write(d)
    fil.close()
    os.chdir('..')
    os.mkdir('static')
    os.chdir('static')
    os.mkdir('css')
    os.chdir('css')
    fi = open('main.css', 'w')
    fi.close()
    os.chdir('..')
    exit(0)



Entry(root, textvariable=a).pack()
Label(root, text='enter something').pack()
Button(root, text='Ok', command=lambda: DoSomethingWithInput(a.get())).pack()
root.mainloop()
