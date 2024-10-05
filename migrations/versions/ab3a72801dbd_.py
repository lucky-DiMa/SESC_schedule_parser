"""empty message

Revision ID: ab3a72801dbd
Revises: bf1cc356884d
Create Date: 2023-12-16 22:36:44.358423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab3a72801dbd'
down_revision: Union[str, None] = 'bf1cc356884d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sub_info', sa.Text(), nullable=True))
    op.drop_column('users', 'sub_role')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sub_role', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('users', 'sub_info')
    # ### end Alembic commands ###
