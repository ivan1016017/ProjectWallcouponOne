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
  coupons: Array<Coupon>
}
