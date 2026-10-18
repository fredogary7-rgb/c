"""login attempt table

Revision ID: a1b2c3d4e5f6
Revises: 6310378df89b
Create Date: 2026-10-18 16:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = '6310378df89b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('login_attempt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(length=120), nullable=False),
    sa.Column('success', sa.Boolean(), nullable=True),
    sa.Column('ip_address', sa.String(length=64), nullable=True),
    sa.Column('user_agent', sa.String(length=300), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('login_attempt')
