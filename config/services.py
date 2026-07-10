from pydantic import Field

from pyrannic import Configuration


class SqlAlchemyConfig(Configuration):
    asyncio: bool = Field(default=False)
    """Whether to use SQLAlchemy async engine for connections."""


class ServicesConfig(Configuration):
    sqlalchemy: SqlAlchemyConfig = Field(default=SqlAlchemyConfig())
    """Configuration for SQLAlchemy."""
