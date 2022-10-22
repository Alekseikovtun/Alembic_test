from alembic.operations import Operations
from alembic.migration import MigrationContext
from config import db_config
import sqlalchemy as sa


db = f"""postgresql://\
{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}\
@localhost:{db_config.POSTGRES_OUT_PORT}/{db_config.DB_NAME}"""
engine = sa.create_engine(db)
conn = engine.connect()
ctx = MigrationContext.configure(conn)
op = Operations(ctx)


# op.add_column('drone_status', sa.Column('test1', sa.Integer))
# op.add_column('drone_status', sa.Column('test2', sa.Integer))
# op.add_column('drone_status', sa.Column('test3', sa.Integer))
op.drop_column('drone_status', 'test1')

print('\n Done \n')
