from datetime import datetime
from sqlalchemy import ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.sessions import Base


class Watchlist(Base):
    __tablename__="watchlist"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    tmdb_movie_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    added_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
 
    user = relationship("User", back_populates="watchlist")