import datetime
import hashlib

from sqlalchemy import func, and_
from sqlalchemy import extract
from model.model import *


def hex_md5(s):
    m = hashlib.md5()
    m.update(s.encode('UTF-8'))
    return m.hexdigest()


def query_distinguish_list(form_data):
    if form_data.get('query_date'):
        d = form_data.get('query_date').replace('-', '')
    else:
        d = datetime.datetime.now().strftime('%Y%m')
    d1 = db.session.query(DetailsList.distinguish, func.count(DetailsList.uid)).filter(
        DetailsList.submit_m.ilike(d + '%')).group_by(DetailsList.distinguish).all()
    d2 = db.session.query(DetailsList.company, func.count(DetailsList.uid)).filter(
        DetailsList.submit_m.ilike(d + '%')).group_by(DetailsList.company).all()
    return {'inside': {i[0]: i[1] for i in d2}, 'outside': {i[0]: i[1] for i in d1}}


def query_flow_data(form_data):
    if form_data.get('query_date'):
        d = form_data.get('query_date').replace('-', '')
    else:
        d = datetime.datetime.now().strftime('%Y%m')
    d1 = db.session.query(DetailsList.flow, func.count(DetailsList.uid)).filter(
        DetailsList.submit_m.ilike(d + '%')).group_by(DetailsList.flow).order_by(
        func.count(DetailsList.uid).desc()).all()
    return [{'flow': i[0], 'flow_num': i[1]} for i in d1]


def query_oa_user_list():
    d1 = db.session.query(DetailsList.submit_m, DetailsList.company, func.count(DetailsList.uid)).group_by(
        DetailsList.company, DetailsList.submit_m).order_by(
        DetailsList.submit_m).all()
    return [{'m': '{}年{}月'.format(i[0][:4], int(i[0][4:])), 'company': i[1], 'num': i[2]} for i in d1]


def query_rseview_period_list():
    year = datetime.date.today().year
    result = []
    for i in range(12):
        d1 = db.session.query(ExamineList.time_frame, func.count(ExamineList.uid)).filter(and_(
            extract('year', ExamineList.reply_b) == year, extract('month', ExamineList.reply_b) == i + 1)).group_by(
            ExamineList.time_frame).all()
        if d1:
            result.append({d[0]: d[1] for d in d1})
        else:
            result.append({})
    return result


def query_avg_reply_time(form_data):
    if form_data.get('query_date'):
        d = form_data.get('query_date')
    else:
        d = datetime.datetime.now().strftime('%Y-%m')
    d1 = db.session.query(ExamineList.node_type, func.avg(ExamineList.reply_time)).filter(
        ExamineList.reply_b.ilike(d + '%')).group_by(
        ExamineList.node_type).all()
    return {d[0]: round(d[1], 2) for d in d1}


def query_lable_data(form_data):
    if form_data.get('query_date'):
        d = form_data.get('query_date').replace('-', '')
    else:
        d = datetime.datetime.now().strftime('%Y%m')

    d1 = db.session.query(func.count(DetailsList.uid)).filter(
        DetailsList.submit_m.ilike(d + '%')).all()
    d2 = db.session.query(func.count(DetailsList.uid)).filter(
        DetailsList.submit_m.ilike(d + '%'), DetailsList.state == '审批不通过').all()
    d3 = db.session.query(func.count(DetailsList.uid)).filter(
        DetailsList.submit_m.ilike(d + '%'), DetailsList.beyond_bud == '是').all()
    return {'all': d1[0], 'back': d2[0], 'beyond': d3[0]}
