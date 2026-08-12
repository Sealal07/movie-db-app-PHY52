from datetime import datetime
from sqlalchemy import ForeignKey, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.sessions import Base


class Review(Base):
    __tablename__="reviews"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False) 
    tmdb_movie_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="reviews")
 

    