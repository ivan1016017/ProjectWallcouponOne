import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ValidationErrors, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { JwtHelperService } from "@auth0/angular-jwt";
import { VendorService } from '../vendor.service';



@Component({
  selector: 'app-vendor-signin',
  templateUrl: './vendor-signin.component.html',
  styleUrls: ['./vendor-signin.component.css']
})
export class VendorSigninComponent implements OnInit {

  helper = new JwtHelperService();
  vendorForm: FormGroup;


  constructor(
    private vendorService: VendorService,
    private formBuilder: FormBuilder,
    private router: Router,
    private toastr: ToastrService
  ) { }

  ngOnInit() {
    this.vendorForm = this.formBuilder.group({
      companyName: ["", [Validators.required, Validators.maxLength(50)]],
      password: ["", [Validators.required, Validators.maxLength(50), Validators.minLength(4)]],
      confirmPassword: ["", [Validators.required, Validators.maxLength(50), Validators.minLength(4)]],
      phone: ["", [Validators.required, Validators.maxLength(50), Validators.minLength(4)]],
      image: ["", [Validators.required, Validators.maxLength(200), Validators.minLength(4)]],
      address: ["", [Validators.required, Validators.maxLength(100), Validators.minLength(4)]],
      zipcode: ["", [Validators.required, Validators.maxLength(100), Validators.minLength(4)]],
      bio: ["", [Validators.required, Validators.maxLength(100), Validators.minLength(4)]]
    })
  }

  signVendor(){}

  showError(error: string){
    this.toastr.error(error, "Error")
  }

  showSuccess() {
    this.toastr.success(`Se ha registrado exitosamente`, "Registro exitoso");
  }
// This is a new comment added

}
