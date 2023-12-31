"""refactor

Revision ID: f090d5648f35
Revises: 12de90987a4f
Create Date: 2023-12-20 23:29:38.390210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f090d5648f35'
down_revision: Union[str, None] = '12de90987a4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('firmwares', 'truck_model',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('firmwares', 'engine_model',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('firmwares', 'ecu_model',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('firmwares', 'flasher',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('firmwares', 'flasher',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('firmwares', 'ecu_model',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('firmwares', 'engine_model',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('firmwares', 'truck_model',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
