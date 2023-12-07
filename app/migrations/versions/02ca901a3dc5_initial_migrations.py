"""Initial migrations

Revision ID: 02ca901a3dc5
Revises: 
Create Date: 2023-12-07 22:47:11.589550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02ca901a3dc5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('firmware_calibrators',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('firmwares',
    sa.Column('file_name', sa.String(), nullable=False),
    sa.Column('truck_model', sa.String(), nullable=False),
    sa.Column('engine_model', sa.String(), nullable=False),
    sa.Column('ecu_model', sa.String(), nullable=False),
    sa.Column('firmware', sa.String(), nullable=False),
    sa.Column('flasher', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('user_uploaded', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('file_name')
    )
    op.create_table('modified_firmwares',
    sa.Column('file_name', sa.String(), nullable=False),
    sa.Column('file_name_original', sa.String(), nullable=False),
    sa.Column('calibrator_name', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=False),
    sa.Column('user_uploaded', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('file_name')
    )
    op.create_table('users',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('access_to_read', sa.Boolean(), nullable=False),
    sa.Column('access_to_write', sa.Boolean(), nullable=False),
    sa.Column('tg_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('modified_firmwares')
    op.drop_table('firmwares')
    op.drop_table('firmware_calibrators')
    # ### end Alembic commands ###