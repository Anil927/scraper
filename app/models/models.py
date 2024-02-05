# "columns": ["Country_Name", "Company_Name", "Product_Name", "ProductURL", "ImageURL", "Raw_Category", "Category", "Currency", "Price", "Description", "Gold_Colour", "Weight", "Gold_Purity", "Diamond_Colour", "Diamond_Clarity", "Diamond_Pieces", "Diamond_Weight", "Ratings", "RatingCounts"]
from sqlalchemy import Column, Integer, String, Float
from app.database_config.database import Base


class Ornament(Base):
    __tablename__ = "ornament"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Country_Name = Column(String(255), nullable=False)
    Company_Name = Column(String(255), nullable=False)
    Product_Name = Column(String(255))
    ProductURL = Column(String(255), nullable=False)
    ImageURL = Column(String(1000))
    Raw_Category = Column(String(255))
    Category = Column(String(255))
    Currency = Column(String(255), nullable=False)
    Price = Column(String(255))
    Description = Column(String(10000))
    Gold_Colour = Column(String(255))
    Weight = Column(String(255))
    Gold_Purity = Column(String(255))
    Diamond_Colour = Column(String(255))
    Diamond_Clarity = Column(String(255))
    Diamond_Pieces = Column(String(255))
    Diamond_Weight = Column(String(255))
    Ratings = Column(String(255))
    RatingCounts = Column(String(255))