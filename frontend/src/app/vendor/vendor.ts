import { Category } from "../category/category";
import { Coupon } from "../coupon/coupon";


export class Vendor {
  id: number;
  company_name: string;
  phone: string;
  image: string;
  address: string;
  zipcode: string;
  created_at: Date;
  bio: string;
  rating: number;
  location_id: number;
  coupons: Array<Coupon>;
  categories: Array<Category>

  constructor(
    id: number,
    company_name: string,
    phone: string,
    image: string,
    address: string,
    zipcode: string,
    created_at: Date,
    bio: string,
    rating: number,
    location_id: number,
    coupons: Array<Coupon>,
    categories: Array<Category>


  ){
    this.id = id
    this.company_name = company_name
    this.phone = phone
    this.image =image
    this.address = address
    this.zipcode = zipcode
    this.created_at = created_at
    this.bio = bio
    this.rating = rating
    this.location_id = location_id
    this.coupons = coupons
    this.categories = categories
  }
}
