import datetime
import hashlib
import json

from sqlalchemy import func, and_
from sqlalchemy import extract
from model.model import *


def hex_md5(s):
    m = hashlib.md5()
    m.update(s.encode('UTF-8'))
    return m.hexdigest()


def query_distinguish_list(form_data):
    if form_data.get('query_date'):
        t = json.loads(form_data.get('query_date'))
        wait_parameter = [i.replace('-', '') for i in t]
    else:
        wait_parameter = [datetime.datetime.now().strftime('%Y%m')]
    if len(wait_parameter[0]) == 4:
        d1 = db.session.query(DetailsList.distinguish, func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.ilike(wait_parameter[0] + '%')).group_by(DetailsList.distinguish).all()
        d2 = db.session.query(DetailsList.company, func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.ilike(wait_parameter[0] + '%')).group_by(DetailsList.company).all()
    else:
        d1 = db.session.query(DetailsList.distinguish, func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.in_(wait_parameter)).group_by(DetailsList.distinguish).all()
        d2 = db.session.query(DetailsList.company, func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.in_(wait_parameter)).group_by(DetailsList.company).all()
    return {'inside': {i[0]: i[1] for i in d2}, 'outside': {i[0]: i[1] for i in d1}}


def query_flow_data(form_data):
    if form_data.get('query_date'):
        t = json.loads(form_data.get('query_date'))
        wait_parameter = [i.replace('-', '') for i in t]
    else:
        wait_parameter = [datetime.datetime.now().strftime('%Y%m')]
    if len(wait_parameter[0]) == 4:
        d1 = db.session.query(DetailsList.flow, func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.ilike(wait_parameter[0] + '%')).group_by(DetailsList.flow).order_by(
            func.count(DetailsList.uid).desc()).all()
    else:
        d1 = db.session.query(DetailsList.flow, func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.in_(wait_parameter)).group_by(DetailsList.flow).order_by(
            func.count(DetailsList.uid).desc()).all()
    return [{'flow': i[0], 'flow_num': i[1]} for i in d1]


def query_oa_user_list(form_data):
    if form_data.get('query_date'):
        year = json.loads(form_data.get('query_date'))[0].split('-')[0]
    else:
        year = datetime.date.today().year
    d1 = db.session.query(DetailsList.submit_m, DetailsList.company, func.count(DetailsList.uid)).filter(
        DetailsList.submit_m.ilike(str(year) + '%')).group_by(
        DetailsList.company, DetailsList.submit_m).order_by(
        DetailsList.submit_m).all()
    return [{'m': '{}年{}月'.format(i[0][:4], int(i[0][4:])), 'company': i[1], 'num': i[2]} for i in d1]


def query_rseview_period_list(form_data):
    form_data=form_data.encode("utf8")
    if form_data.get('query_date'):
        year = json.loads(form_data.get('query_date'))[0].split('-')[0]
    else:
        year = datetime.date.today().year
        month = datetime.date.today().month
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
        t = json.loads(form_data.get('query_date'))
        wait_parameter = [i for i in t]
    else:
        wait_parameter = [datetime.datetime.now().strftime('%Y-%m')]
    result = {}
    if len(wait_parameter[0]) == 4:
        d1 = db.session.query(ExamineList.node_type, func.avg(ExamineList.reply_time)).filter(
            ExamineList.reply_b.ilike(wait_parameter[0] + '%')).group_by(
            ExamineList.node_type).all()
        result = {d[0]: d[1] for d in d1}
    else:
        for i in wait_parameter:
            d1 = db.session.query(ExamineList.node_type, ExamineList.reply_time).filter(
                ExamineList.reply_b.ilike(i + '%')).all()
            for d in d1:
                if d[0] not in result:
                    result[d[0]] = []
                result[d[0]].append(float(d[1]))
        for r in result:
            result[r] = sum(result[r]) / len(result[r])
    return {d[0]: round(d[1], 2) for d in sorted(result.items(), key=lambda d: d[1])}


def query_lable_data(form_data):
    if form_data.get('query_date'):
        t = json.loads(form_data.get('query_date'))
        wait_parameter = [i.replace('-', '') for i in t]
    else:
        wait_parameter = [datetime.datetime.now().strftime('%Y%m')]
    if len(wait_parameter[0]) == 4:
        d1 = db.session.query(func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.ilike(wait_parameter[0] + '%')).all()
        d2 = db.session.query(func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.ilike(wait_parameter[0] + '%'), DetailsList.state == '审批不通过').all()
        d3 = db.session.query(func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.ilike(wait_parameter[0] + '%'), DetailsList.beyond_bud == '是').all()
    else:
        d1 = db.session.query(func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.in_(wait_parameter)).all()
        d2 = db.session.query(func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.in_(wait_parameter), DetailsList.state == '审批不通过').all()
        d3 = db.session.query(func.count(DetailsList.uid)).filter(
            DetailsList.submit_m.in_(wait_parameter), DetailsList.beyond_bud == '是').all()
    return {'all': d1[0], 'back': d2[0], 'beyond': d3[0]}
