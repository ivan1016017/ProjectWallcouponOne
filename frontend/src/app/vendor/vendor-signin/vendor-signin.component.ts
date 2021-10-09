import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ValidationErrors, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { JwtHelperService } from "@auth0/angular-jwt";


@Component({
  selector: 'app-vendor-signin',
  templateUrl: './vendor-signin.component.html',
  styleUrls: ['./vendor-signin.component.css']
})
export class VendorSigninComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
