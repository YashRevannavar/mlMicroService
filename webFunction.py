from flask import Flask, request
import numpy as np

def get_data_from_form():
    sl = request.form["sl"]
    sw = request.form["sw"]
    pl = request.form["pl"]
    pw = request.form["pw"]
    data = np.array([[sl, sw, pl, pw]])
    return data
