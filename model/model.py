from flask import flash

from exts import db


class DetailsList(db.Model):
    __tableName__ = 'details_list'
    uid = db.Column(db.VARCHAR(40), primary_key=True)
    odd_num = db.Column(db.Text)
    designation = db.Column(db.Text)
    flow = db.Column(db.Text)  # 流程
    budget = db.Column(db.Text)  # 预算
    submit_date = db.Column(db.DateTime)
    submit_m = db.Column(db.Text)
    department_apply = db.Column(db.Text)
    budget_dept = db.Column(db.Text)  # 预算部门
    beyond_bud = db.Column(db.Text)
    company = db.Column(db.Text)
    tax_inclusive = db.Column(db.Text)
    no_tax = db.Column(db.Text)
    distinguish = db.Column(db.Text)
    budget_account = db.Column(db.Text)  # 预算科目
    time_frame = db.Column(db.Text)  # 时间段
    remark = db.Column(db.Text)
    flow_id = db.Column(db.Text)
    state = db.Column(db.Text)
    submitter = db.Column(db.Text)  # 提交人


class ExamineList(db.Model):
    __tableName__ = 'examine_list'
    uid = db.Column(db.VARCHAR(40), primary_key=True)
    reply_time = db.Column(db.Text)  # (批复时长）
    odd_num = db.Column(db.Text)
    flow = db.Column(db.Text)
    node_type = db.Column(db.Text)
    officer = db.Column(db.Text)  # 审批人
    reply_b = db.Column(db.DateTime)  # (批复时间）
    time_frame = db.Column(db.Text)  # (时段）
    node_name = db.Column(db.Text)
    flow_type = db.Column(db.Text)
