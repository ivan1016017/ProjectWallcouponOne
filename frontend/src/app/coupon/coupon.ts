export class Coupon {
  id: number;
  total_price: number;
  percentage_discount: number;
  vendor_category: number;
  vendor_plan_id: number;
  created_at: Date;
  starts_at: Date;
  finishes_at: Date;
  vendor_id: number


  constructor(
    id: number,
    total_price: number,
    percentage_discount: number,
    vendor_category: number,
    vendor_plan_id: number,
    created_at: Date,
    starts_at: Date,
    finishes_at: Date,
    vendor_id: number
  ){
    this.id = id
    this.total_price = total_price
    this.percentage_discount = percentage_discount
    this.vendor_category = vendor_category
    this.vendor_plan_id = vendor_plan_id
    this.created_at = created_at
    this.starts_at = starts_at
    this.finishes_at = finishes_at
    this.vendor_id = vendor_id
  }

}




