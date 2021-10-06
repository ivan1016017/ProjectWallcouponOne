from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql import func 
import enum
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint
from .enumerations import *

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
    coupons = db.relationship('Coupon', cascade='all, delete, delete-orphan')
    categories = db.relationship('Category', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return "{} - {}".format(self.company_name, self.address)

class Coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer)
    percentage_discount = db.Column(db.Float)
    vendor_category_id = db.Column(db.Integer)
    vendor_plan_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    starts_at = db.Column(db.DateTime(timezone=True), default=func.now())
    finishes_at = db.Column(db.DateTime(timezone=True), default=func.now())
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    categories = db.relationship('Category', cascade='all, delete, delete-orphan')

    



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_class_category = db.Column(db.Enum(FirstClassCategory))
    second_class_category_locals = db.Column(db.Enum(SecondClassCategoryLocals))
    second_class_category_goods = db.Column(db.Enum(SecondClassCategoryGoods))
    second_class_category_hotels = db.Column(db.Enum(SecondClassCategoryHotels))
    third_class_category_locals = db.Column(db.Enum(ThirdClassCategoryLocals))
    third_class_category_goods = db.Column(db.Enum(ThirdClassCategoryGoods))
    third_class_category_hotels = db.Column(db.Enum(ThirdClassCategoryHotels))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupon.id'))


    

class EnumDictionary(fields.Field):
    def _serialize(self, value, attr, obj, *kwargs):
        if value is None:
            return None 
        return {"key": value.name, "value": value.value}

class VendorSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = Vendor 
        include_relationships = True 
        load_instance = True 

class CouponSchema(SQLAlchemyAutoSchema):
    class Meta: 
        model = Coupon
        include_relationships = True 
        load_instance = True 

class CategorySchema(SQLAlchemyAutoSchema):
    first_class_category = EnumDictionary(attribute=("first_class_category"))
    second_class_category_locals = EnumDictionary(attribute=("second_class_category_locals"))
    second_class_category_goods = EnumDictionary(attribute=("second_class_category_goods"))
    second_class_category_hotels = EnumDictionary(attribute=("second_class_category_hotels"))
    third_class_category_locals = EnumDictionary(attribute=("third_class_category_locals"))
    third_class_category_goods = EnumDictionary(attribute=("third_class_category_goods"))
    third_class_category_hotels = EnumDictionary(attribute=("third_class_category_hotels"))

    class Meta: 
        model = Category
        include_relationships = True 
        load_instance = True 












    