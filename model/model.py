from flask import flash, current_app
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, Required
from ldap3 import Server, Connection, ALL, SUBTREE, ServerPool
from exts import db


class Users(db.Model, UserMixin):
    __tableName__ = 'temp_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username

    # 定义验证密码的函数confirm_password
    def confirm_password(self, password):
        return password == self.password

    @staticmethod
    def try_ldap_login(username, password):
        return True

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


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


class FailData(db.Model):
    __tableName__ = 'fail_data'
    uid = db.Column(db.VARCHAR(40), primary_key=True)
    fail_time = db.Column(db.Text)
    jid = db.Column(db.Text)


class LoginForm(FlaskForm):
    username = StringField(
        label="昵称(账号)",
        description="昵称(账号)",
        validators=[
            DataRequired("请输入昵称(账号)"),
            Length(5, 10, message=u'长度位于5~10之间')
        ],

        render_kw={
            'id': 'username',
            "class": "form-control input-lg",
            "placeholder": "昵称(账号)",
        }
    )
    password = PasswordField(
        label="密码",
        description="密码",
        validators=[
            DataRequired("请输入密码"),
            Length(5, 20, message=u'长度位于5~20之间')
        ],
        render_kw={
            'id': 'password',
            "class": "form-control input-lg",
            "placeholder": "密码",
        }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-lg btn-success btn-block submit",
        }
    )
