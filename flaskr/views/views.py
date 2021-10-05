from flask_restful import Resource 
from ..models  import db, Vendor, Coupon, VendorCategory, VendorSchema, CouponSchema, VendorCategorySchema


vendor_schema = VendorSchema()
coupon_schema = CouponSchema()
vendor_category_schema = VendorCategorySchema()

class ViewVendor(Resource):
    def get(self):
        return [vendor_schema.dump(vendor) for vendor in Vendor.query.all()]


class ViewCoupon(Resource):
    def get(self):
        return [coupon_schema.dump(coupon) for coupon in  Coupon.query.all()]


class ViewVendorCategory(Resource):
    def get(self):
        return [vendor_category_schema.dump(vendor_category) for vendor_category in VendorCategory.query.all()]