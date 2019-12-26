import json
import os
import time

from flask import request, app, send_from_directory, abort, session, redirect
from api.server import *
from . import api


@api.route('/')
def index():
    return "api"


@api.route('/get_distinguish_list/', methods=['POST'])
def distinguish_list():
    form_data = request.form.to_dict()
    result = query_distinguish_list(form_data)
    return json.dumps(result, ensure_ascii=False)


@api.route('/get_flow_list/', methods=['POST'])
def flow_list():
    form_data = request.form.to_dict()
    result = query_flow_data(form_data)
    return json.dumps(result, ensure_ascii=False)


@api.route('/get_oauser_list/')
def oauser_list():
    result = query_oa_user_list()
    return json.dumps(result, ensure_ascii=False)


@api.route('/get_rseview_period_list/')
def rseview_period_list():
    result = query_rseview_period_list()
    return json.dumps(result, ensure_ascii=False)


@api.route('/get_avg_reply_time/', methods=['POST'])
def avg_reply_time():
    form_data = request.form.to_dict()
    result = query_avg_reply_time(form_data)
    return json.dumps(result, ensure_ascii=False)


@api.route('/get_lable_data/', methods=['POST'])
def lable_data():
    form_data = request.form.to_dict()
    result = query_lable_data(form_data)
    return json.dumps(result, ensure_ascii=False)
