import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateCouponComponent } from './coupon/create-coupon/create-coupon.component';
import { VendorLoginComponent } from './vendor/vendor-login/vendor-login.component';
import { VendorSigninComponent } from './vendor/vendor-signin/vendor-signin.component';

const routes: Routes = [
  {
    path:'',
    component:VendorLoginComponent,
    pathMatch: 'full'
  },
  {
    path:'signin',
    component:VendorSigninComponent,
    // pathMatch: 'full'
  },
  {
    path:'coupons/:vendorId/:vendorToken',
    component:CreateCouponComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
