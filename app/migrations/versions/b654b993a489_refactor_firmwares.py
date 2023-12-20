"""refactor Firmwares

Revision ID: b654b993a489
Revises: 0a72cae34ff4
Create Date: 2023-12-20 00:48:48.012888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b654b993a489'
down_revision: Union[str, None] = '0a72cae34ff4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('firmwares', sa.Column('file_size', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('firmwares', 'file_size')
    # ### end Alembic commands ###
