"""empty message

Revision ID: f401e272b80f
Revises: 
Create Date: 2019-12-23 14:37:54.864253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f401e272b80f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('details_list',
    sa.Column('uid', sa.VARCHAR(length=40), nullable=False),
    sa.Column('odd_num', sa.Text(), nullable=True),
    sa.Column('designation', sa.Text(), nullable=True),
    sa.Column('flow', sa.Text(), nullable=True),
    sa.Column('budget', sa.Text(), nullable=True),
    sa.Column('submit_date', sa.DateTime(), nullable=True),
    sa.Column('submit_m', sa.Text(), nullable=True),
    sa.Column('department_apply', sa.Text(), nullable=True),
    sa.Column('budget_dept', sa.Text(), nullable=True),
    sa.Column('beyond_bud', sa.Text(), nullable=True),
    sa.Column('company', sa.Text(), nullable=True),
    sa.Column('tax_inclusive', sa.Text(), nullable=True),
    sa.Column('no_tax', sa.Text(), nullable=True),
    sa.Column('distinguish', sa.Text(), nullable=True),
    sa.Column('budget_account', sa.Text(), nullable=True),
    sa.Column('time_frame', sa.Text(), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.Column('flow_id', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('submitter', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('examine_list',
    sa.Column('uid', sa.VARCHAR(length=40), nullable=False),
    sa.Column('reply_time', sa.Text(), nullable=True),
    sa.Column('odd_num', sa.Text(), nullable=True),
    sa.Column('flow', sa.Text(), nullable=True),
    sa.Column('node_type', sa.Text(), nullable=True),
    sa.Column('officer', sa.Text(), nullable=True),
    sa.Column('reply_b', sa.DateTime(), nullable=True),
    sa.Column('time_frame', sa.Text(), nullable=True),
    sa.Column('node_name', sa.Text(), nullable=True),
    sa.Column('flow_type', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('examine_list')
    op.drop_table('details_list')
    # ### end Alembic commands ###