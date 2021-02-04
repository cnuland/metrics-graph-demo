from flask import Flask, request, session, render_template, redirect, url_for
from flask import _request_ctx_stack as stack
from random import randint
import requests
import os

app = Flask(__name__)

def arccot(x, u):
    sum = ussu = u // x
    n = 3
    sign = -1
    while 1:
        ussu = ussu // (x*x)
        term = ussu // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum

def pi(basamak):
    u = 10**(basamak+10)
    pi = 4 * (4*arccot(5,u) - arccot(239,u))
    return pi // 10**10

@app.route("/")
def route():
    count = request.args.get("count",  default = 0, type = int) # How far to iterat
    return pi(count)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
