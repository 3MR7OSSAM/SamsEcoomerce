from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'Products'

    # Columns based on the table definition
    product_id = db.Column("ProductID", db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing Product ID
    product_name = db.Column("ProductName", db.String(100), nullable=False)  # Product name
    description = db.Column("Description", db.String(255), nullable=True)  # Description of the product
    image = db.Column("Image", db.String(500), nullable=True)  # Description of the product
    price = db.Column("Price", db.Numeric(10, 2), nullable=False)  # Price of the product
    quantity = db.Column("Quantity", db.Integer, nullable=False)  # Quantity available
    vendor = db.Column("Vendor", db.String(100), nullable=True)  # Vendor name
    created_at = db.Column("CreatedAt", db.DateTime, default=datetime.utcnow)  # Timestamp of product creation
    updated_at = db.Column("UpdatedAt", db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp of product update

    def __repr__(self):
        return f"<Product {self.product_name} - ${self.price}>"
