import sqlalchemy
import databases
from sqlalchemy.dialects.postgresql import UUID


DATABASE_URL = "postgresql://postgres:1234@localhost:5432/db"
metadata = sqlalchemy.MetaData()
notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", UUID(as_uuid=True), primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)