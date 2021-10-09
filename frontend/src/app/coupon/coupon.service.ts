import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Coupon } from './coupon';
import { Category } from '../category/category';

@Injectable({
  providedIn: 'root'
})
export class CouponService {

private backUrl: string = "http://localhost:5000"


constructor(private http: HttpClient) { }

getCouponsVendor(idVendor: number): Observable<Coupon[]>{
  return this.http.get<Coupon[]>(`${this.backUrl}/vendor/${idVendor}/coupons`)
}

createCoupon(idVendor: number, coupon:Coupon):Observable<Coupon>{
  return this.http.post<Coupon>(`${this.backUrl}/vendor/${idVendor}/coupons`, coupon)
}

}
