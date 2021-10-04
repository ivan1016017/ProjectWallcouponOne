from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func 
import enum

from sqlalchemy.sql.schema import PrimaryKeyConstraint

db = SQLAlchemy()

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    image = db.Column(db.String(200))
    address = db.Column(db.String(100))
    zipcode = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    bio = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    location_id = db.Column(db.Integer)
    coupons = db.relationship('Coupon', cascade='all, delte, delete-orphan')

    def __repr__(self):
        return "{} - {}".format(self.company_name, self.address)

class Coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer)
    percentage_discount = db.Column(db.Float)
    vendor_category_id = db.Column(db.Integer)
    vendor_plan_id = db.Column(db.Integer)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))

class VendorCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # first_class_category = db.Column(db.Enum(FirstClassCategory))
    # second_class_category_local = db.Column(db.Enum(SecondClassCategoryLocal))
    # second_class_category_good = db.Column(db.Enum(SecondClassCategoryGood))
    # second_class_category_hotel = db.Column(db.Enum(SecondClassCategoryHotel))




class FirstClassCategory(enum.Enum):
    LOCALS = 1
    GOODS = 2
    HOTELS = 3

class SecondClassCategoryLocal(enum.Enum):
    BEAUTYANDSPAS = 1
    THINGSTODO = 2
    FOODANDDRINK = 3
    HEALTHANDFITNESS = 4
    MORE = 4
    

class SecondClassCategoryGood(enum.Enum):
    HEALTHANDBEAUTY = 1
    FORTHEHOME = 2
    WOMENFASHION = 3 
    MENFASION = 4
    MORE = 5


class SecondClassCategoryHotel(enum.Enum):
    HOTEL = 1
    DEALS = 2

class ThirdClassCategory(enum.Enum):
    FACESKINCARE = 1
    MESSAGE = 2
    SALOND = 3
    COSMETICPROCEDURES = 4
    HAIRREMOVAL = 5









    