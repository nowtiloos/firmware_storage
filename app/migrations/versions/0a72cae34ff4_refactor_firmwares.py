"""refactor Firmwares

Revision ID: 0a72cae34ff4
Revises: 9ed0c5651b65
Create Date: 2023-12-20 00:43:08.871156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a72cae34ff4'
down_revision: Union[str, None] = '9ed0c5651b65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('firmwares', 'firmware')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('firmwares', sa.Column('firmware', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
