from flaskr import create_app
from .models import db, Vendor, Coupon, VendorCategory
from .models import VendorSchema, CouponSchema, VendorCategorySchema
from flask_restful import Api 
from .views import ViewCoupon, ViewVendor, ViewVendorCategory

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# test

with app.app_context():
    vendor_schema = VendorSchema()
    vendor_one = Vendor(company_name = "vendorOne",
                    phone = "123456789",
                    image = "",
                    address = "Seventh avenue NYC",
                    zipcode = "2345",
                    bio = "This is the bio of the vendor one",
                    rating = 10,
                    location_id = 1)
    vendor_two = Vendor(company_name = "vendorTwo",
                    phone = "12345",
                    image = "",
                    address = "Fifth avenue NYC",
                    zipcode = "25",
                    bio = "This is the bio of the vendor two",
                    rating = 10,
                    location_id = 1)
    
    coupon_one = Coupon(total_price=100,
                        percentage_discount = 0.10,
                        vendor_category_id = 2,
                        vendor_plan_id = 3)
    vendor_two.coupons.append(coupon_one)
    db.session.add(vendor_one)
    db.session.add(vendor_two)
    db.session.commit()
    print([vendor_schema.dumps(vendor) for vendor in Vendor.query.all()])
    print(Vendor.query.all()[0].coupons)
    print(Vendor.query.all()[1].coupons)
    print(Vendor.query.all())
    print(Coupon.query.all())
    db.session.delete(vendor_two)
    db.session.commit()
    print(Vendor.query.all())
    print(Coupon.query.all())
