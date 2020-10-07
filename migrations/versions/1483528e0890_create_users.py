"""create users

Revision ID: 1483528e0890
Revises: 56ad0201a44d
Create Date: 2020-10-07 12:14:14.159542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1483528e0890'
down_revision = '56ad0201a44d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(length=280), nullable=False),
    sa.Column('email', sa.String(length=280), nullable=True),
    sa.Column('api_key', sa.String(length=280), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    op.add_column('tweets', sa.Column('user_username', sa.String(), nullable=True))
    op.create_foreign_key(None, 'tweets', 'users', ['user_username'], ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tweets', type_='foreignkey')
    op.drop_column('tweets', 'user_username')
    op.drop_table('users')
    # ### end Alembic commands ###