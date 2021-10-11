import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VendorComponent } from './vendor.component';
import { VendorLoginComponent } from './vendor-login/vendor-login.component';
import { VendorSigninComponent } from './vendor-signin/vendor-signin.component';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';



@NgModule({
  imports: [
    CommonModule, ReactiveFormsModule
  ],
  declarations: [VendorComponent, VendorLoginComponent, VendorSigninComponent],
  exports: [VendorLoginComponent, VendorSigninComponent, VendorComponent]
})
export class VendorModule { }
