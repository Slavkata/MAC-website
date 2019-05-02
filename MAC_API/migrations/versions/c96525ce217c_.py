"""empty message

Revision ID: c96525ce217c
Revises: 
Create Date: 2019-04-18 19:54:14.066795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c96525ce217c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AccountDeposti',
    sa.Column('deposit_number', sa.Integer(), nullable=False),
    sa.Column('ticket_number', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('deposit_number')
    )
    op.create_table('Client',
    sa.Column('ticket_number', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('ongoing_loan', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('ticket_number')
    )
    op.create_table('PaymentAccount',
    sa.Column('ticket_number', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticket_number')
    )
    op.create_table('Ticket',
    sa.Column('ticket_number', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('ticket_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Ticket')
    op.drop_table('PaymentAccount')
    op.drop_table('Client')
    op.drop_table('AccountDeposti')
    # ### end Alembic commands ###
