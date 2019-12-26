import os
from datetime import timedelta

from flask import request, app, send_from_directory, abort, render_template, redirect, flash, url_for, session

from page.server import *
from . import page


@page.route('/')
def index():
    return render_template('index.html')
