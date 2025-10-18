from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Base class for models
Base = declarative_base()

# Database URL
DATABASE_URL = "postgresql+asyncpg://dw_user:dw_pass@localhost:5433/datawhiz"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create async session
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency for FastAPI routes (will use later)
async def get_session():
    async with async_session() as session:
        yield session
