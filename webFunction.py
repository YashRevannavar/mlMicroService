from flask import Flask, request
import numpy as np

def get_data_from_form():
    """
    Retrieves the input data from the form.
    Returns:
    -------
    data: numpy.ndarray
    A numpy array containing the input data.
    """
    sl = request.form["sl"]
    sw = request.form["sw"]
    pl = request.form["pl"]
    pw = request.form["pw"]
    data = np.array([[sl, sw, pl, pw]])
    return data
