import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateCouponComponent } from './coupon/create-coupon/create-coupon.component';

const routes: Routes = [
  {
    path:'',
    component:CreateCouponComponent,
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
