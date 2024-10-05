"""add last_message_id

Revision ID: 1451cd520c0b
Revises: 88a165336bd9
Create Date: 2024-10-04 21:41:28.353060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1451cd520c0b'
down_revision: Union[str, None] = '88a165336bd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_message_id', sa.BigInteger(), nullable=False, server_default='0'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_message_id')
    # ### end Alembic commands ###
