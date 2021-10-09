from flask_restful import Resource 
from ..models  import db, Vendor, Coupon, Category, VendorSchema, CouponSchema, CategorySchema
from flask import request
from flask_jwt_extended import jwt_required, create_access_token

vendor_schema = VendorSchema()
coupon_schema = CouponSchema()
category_schema = CategorySchema()

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
    @jwt_required()
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

class ViewLogInVendor(Resource):

    def post(self):
        vendor = Vendor.query.filter(Vendor.company_name == request.json["company_name"], Vendor.password == request.json["password"]).first()
        db.session.commit()
        if vendor is None:
            return "El vendedor no existe", 404
        else:
            access_token = create_access_token(identity = vendor.id)
            return {"mensaje":"Inicio de sesión exitoso", "token": access_token}


class ViewCoupons(Resource):
    def get(self, id_vendor):
        vendor = Vendor.query.get_or_404(id_vendor)
        return [coupon_schema.dump(coupon) for coupon in  vendor.coupons]

    def post(self, id_vendor):
        new_coupon = Coupon(total_price = request.json['total_price'],
        percentage_discount = request.json['percentage_discount'],
        starts_at = request.json['starts_at'],
        finishes_at = request.json['finishes_at'])

        vendor = Vendor.query.get_or_404(id_vendor)
        vendor.coupons.append(new_coupon)
        db.session.add(new_coupon)
        db.session.commit()
        return coupon_schema.dump(new_coupon)

    def put(self, id_coupon):
        coupon = Coupon.query.get_or_404(id_coupon)
        coupon.total_price = request.json.get("total_price", coupon.total_price)
        coupon.percentage_discount = request.json.get("percentage_discount", coupon.percentage_discount)
        coupon.starts_at = request.json.get("starts_at", coupon.starts_at)
        coupon.finishes_at = request.json.get("finishes_at", coupon.finishes_at)
        db.session.commit()
        return coupon_schema.dump(coupon)


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



class ViewCategory(Resource):
    def get(self):
        return [category_schema.dump(vendor_category) for vendor_category in Category.query.all()]