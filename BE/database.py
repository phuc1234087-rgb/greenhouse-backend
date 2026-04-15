import os  # Thêm dòng này ở trên cùng
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Lệnh này nghĩa là: Ưu tiên lấy DATABASE_URL trên Render. Nếu không có (lúc chạy ở nhà), thì xài tạm localhost.
SQL_ALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:123456@localhost:5432/FASTAPI")

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()