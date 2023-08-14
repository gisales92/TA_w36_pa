"""create people

Revision ID: 21576a1b2cba
Revises:
Create Date: 2023-08-12 13:24:21.733610

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21576a1b2cba'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("simple_people",
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("name", sa.String(50), nullable=False),
                    sa.Column("age", sa.Integer),
                    sa.Column("bio", sa.String(2000)))


def downgrade() -> None:
    op.drop_table("simple_people")
