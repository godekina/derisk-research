"""add order_book and interest_rate

Revision ID: 593bb0a7d06b
Revises: e4c7f75ff173
Create Date: 2024-06-06 09:24:30.215515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy_utils
import sqlalchemy as sa
import sqlalchemy_utils

from handler_tools.constants import ProtocolIDs


# revision identifiers, used by Alembic.
revision: str = '593bb0a7d06b'
down_revision: Union[str, None] = 'e4c7f75ff173'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interest_rate',
    sa.Column('block', sa.BigInteger(), nullable=True),
    sa.Column('timestamp', sa.BigInteger(), nullable=True),
    sa.Column('protocol_id', sqlalchemy_utils.types.choice.ChoiceType(ProtocolIDs), nullable=False),
    sa.Column('collateral', sa.JSON(), nullable=True),
    sa.Column('debt', sa.JSON(), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interest_rate_block'), 'interest_rate', ['block'], unique=False)
    op.create_index(op.f('ix_interest_rate_timestamp'), 'interest_rate', ['timestamp'], unique=False)
    op.create_table('orderbook',
    sa.Column('token_a', sa.String(), nullable=False),
    sa.Column('token_b', sa.String(), nullable=False),
    sa.Column('timestamp', sa.BigInteger(), nullable=False),
    sa.Column('block', sa.BigInteger(), nullable=False),
    sa.Column('dex', sa.String(), nullable=False),
    sa.Column('asks', sa.JSON(), nullable=True),
    sa.Column('bids', sa.JSON(), nullable=True),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orderbook_dex'), 'orderbook', ['dex'], unique=False)
    op.create_index(op.f('ix_orderbook_token_a'), 'orderbook', ['token_a'], unique=False)
    op.create_index(op.f('ix_orderbook_token_b'), 'orderbook', ['token_b'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orderbook_token_b'), table_name='orderbook')
    op.drop_index(op.f('ix_orderbook_token_a'), table_name='orderbook')
    op.drop_index(op.f('ix_orderbook_dex'), table_name='orderbook')
    op.drop_table('orderbook')
    op.drop_index(op.f('ix_interest_rate_timestamp'), table_name='interest_rate')
    op.drop_index(op.f('ix_interest_rate_block'), table_name='interest_rate')
    op.drop_table('interest_rate')
    # ### end Alembic commands ###