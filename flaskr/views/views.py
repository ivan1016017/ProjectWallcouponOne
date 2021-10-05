from flask_restful import Resource 
from ..models  import db, Vendor, Coupon, VendorCategory, VendorSchema, CouponSchema, VendorCategorySchema
from flask import request

vendor_schema = VendorSchema()
coupon_schema = CouponSchema()
vendor_category_schema = VendorCategorySchema()

class ViewVendors(Resource):
    def get(self):
        return [vendor_schema.dump(vendor) for vendor in Vendor.query.all()]

    def post(self):
        new_vendor = Vendor(company_name = request.json['company_name'], 
        phone = request.json['phone'],
        image = request.json['image'],
        address = request.json['address'],
        zipcode = request.json['zipcode'],
        bio = request.json['bio'])
        db.session.add(new_vendor)
        db.session.commit()
        return vendor_schema.dump(new_vendor)

class ViewVendor(Resource):
    def get(self, id_vendor):
        return vendor_schema.dump(Vendor.query.get_or_404(id_vendor))

    def put(self, id_vendor):
        vendor = Vendor.query.get_or_404(id_vendor)
        vendor.company_name = request.json.get('company_name', vendor.company_name)
        vendor.phone = request.json.get('phone',vendor.phone)
        vendor.image = request.json.get('image',vendor.image)
        vendor.address = request.json.get('address',vendor.address)
        vendor.zipcode = request.json.get('zipcode',vendor.zipcode)
        vendor.bio = request.json.get('bio',vendor.bio)
        db.session.commit()
        return vendor_schema.dump(vendor)

    def delete(self, id_vendor):
        vendor = Vendor.query.get_or_404(id_vendor)
        db.session.delete(vendor)
        db.session.commit()
        return "", 204


class ViewCoupons(Resource):
    def get(self):
        return [coupon_schema.dump(coupon) for coupon in  Coupon.query.all()]

    def post(self):
        new_coupon = Coupon(total_price = request.json['total_price'],
        percentage_discount = request.json['percentage_discount'],
        starts_at = request.json['starts_at'],
        finishes_at = request.json['finishes_at'])
        db.session.add(new_coupon)
        db.session.commit()
        return coupon_schema.dump(new_coupon)


class ViewCoupon(Resource):

    def get(self, id_coupon):
        return coupon_schema.dump(Coupon.query.get_or_404(id_coupon))

    def put(self, id_coupon):
        coupon = Coupon.query.get_or_404(id_coupon)
        coupon.total_price = request.json.get('total_price', coupon.total_price)
        coupon.percentage_discount = request.json.get('percentage_discount', coupon.percentage_discount)
        coupon.starts_at = request.json.get('starts_at', coupon.starts_at)
        coupon.finishes_at = request.json.get('finishes_at', coupon.finishes_at)
        db.session.commit()
        return coupon_schema.dump(coupon)

    def delete(self,id_coupon):
        coupon = Coupon.query.get_or_404(id_coupon)
        db.session.delete(coupon)
        db.session.commit()
        return '', 204



class ViewVendorCategory(Resource):
    def get(self):
        return [vendor_category_schema.dump(vendor_category) for vendor_category in VendorCategory.query.all()]