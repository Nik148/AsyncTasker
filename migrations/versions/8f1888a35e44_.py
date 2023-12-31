"""empty message

Revision ID: 8f1888a35e44
Revises: 
Create Date: 2023-10-08 23:21:43.765629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8f1888a35e44'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SEQUENCE task_id_sequence")
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.String(length=155), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('result', postgresql.BYTEA(), nullable=True),
    sa.Column('date_done', sa.DateTime(), nullable=True),
    sa.Column('traceback', sa.Text(), nullable=True),
    sa.Column('name', sa.String(length=155), nullable=True),
    sa.Column('args', postgresql.BYTEA(), nullable=True),
    sa.Column('kwargs', postgresql.BYTEA(), nullable=True),
    sa.Column('worker', sa.String(), nullable=True),
    sa.Column('retries', sa.Integer(), nullable=True),
    sa.Column('queue', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
