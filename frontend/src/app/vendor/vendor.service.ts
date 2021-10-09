import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vendor } from './vendor';
import { Category } from '../category/category';


@Injectable({
  providedIn: 'root'
})
export class VendorService {

 private backUrl: string = "http://localhost:5000"

constructor(private http: HttpClient) { }

vendorLogIn(companyName: string, password: string):Observable<any>{
  return this.http.post<any>(`${this.backUrl}/vendor/logIn`, {"company_name": companyName, "password": password });
}

}
