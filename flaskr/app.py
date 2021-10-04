from flaskr import create_app
from .models import db, Vendor

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# test

with app.app_context():
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
    db.session.add(vendor_one)
    db.session.add(vendor_two)
    db.session.commit()
    print(Vendor.query.all())