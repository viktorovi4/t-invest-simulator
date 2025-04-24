from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.database import Base  # Стало

# Модель для пользователей
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)  # Уникальный email
    password_hash = Column(String)  # Хеш пароля
    balance = Column(Float, default=0.0)  # Виртуальный баланс

# Модель для портфеля (купленные акции)
class Portfolio(Base):
    __tablename__ = "portfolio"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Связь с пользователем
    ticker = Column(String)  # Тикер акции (например, "SBER")
    quantity = Column(Integer)  # Количество акций
    avg_price = Column(Float)  # Средняя цена покупки

# Модель для истории транзакций
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    ticker = Column(String)
    action = Column(String)  # "buy" или "sell"
    price = Column(Float)  # Цена сделки
    quantity = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)  # Дата и время сделки