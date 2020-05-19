"""empty message

Revision ID: 6b8d2f485091
Revises: c510c1afadd4
Create Date: 2020-05-19 23:58:32.814390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b8d2f485091'
down_revision = 'c510c1afadd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relate_genre_artist',
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
    sa.PrimaryKeyConstraint('genre_id', 'artist_id')
    )
    op.create_table('relate_genre_venue',
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Venue.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
    sa.PrimaryKeyConstraint('genre_id', 'artist_id')
    )
    op.drop_table('relate_gere_artist')
    op.drop_table('relate_gere_venue')
    op.add_column('Show', sa.Column('start_time', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'start_time')
    op.create_table('relate_gere_venue',
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Venue.id'], name='relate_gere_venue_artist_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], name='relate_gere_venue_genre_id_fkey'),
    sa.PrimaryKeyConstraint('genre_id', 'artist_id', name='relate_gere_venue_pkey')
    )
    op.create_table('relate_gere_artist',
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='relate_gere_artist_artist_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], name='relate_gere_artist_genre_id_fkey'),
    sa.PrimaryKeyConstraint('genre_id', 'artist_id', name='relate_gere_artist_pkey')
    )
    op.drop_table('relate_genre_venue')
    op.drop_table('relate_genre_artist')
    # ### end Alembic commands ###
