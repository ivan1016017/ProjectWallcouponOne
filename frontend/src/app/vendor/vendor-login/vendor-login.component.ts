import { Component, OnInit } from '@angular/core';
import { VendorService } from '../vendor.service';
import { Router } from '@angular/router';
import { JwtHelperService } from "@auth0/angular-jwt";

// import { stringify } from 'querystring';


@Component({
  selector: 'app-vendor-login',
  templateUrl: './vendor-login.component.html',
  styleUrls: ['./vendor-login.component.css']
})
export class VendorLoginComponent implements OnInit {
  helper = new JwtHelperService();

  constructor(private vendorService: VendorService,
    private router: Router) { }

    error: boolean = false

  ngOnInit() {

  }

  onLogInVendor(companyName: string, password:string){
    this.error = false


    this.vendorService.vendorLogIn(companyName, password).subscribe(res => {
      console.log(res)
      const decodedToken = this.helper.decodeToken(res.token);
      console.log(decodedToken)
      console.log(decodedToken.sub)
      console.log(res.token)

      this.router.navigate([`/coupons/${decodedToken.sub}/${res.token}`])
    })
  }

}
