"""empty message

Revision ID: 37ef515b370d
Revises: 
Create Date: 2020-12-08 19:15:38.124079

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '37ef515b370d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('performance_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inventory_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('performance_record', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('performance_score', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('report_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('inventory_id', 'report_date')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('performance_profile')
    # ### end Alembic commands ###
