import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ValidationErrors, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { JwtHelperService } from "@auth0/angular-jwt";
import { VendorService } from '../vendor.service';
import { FirstClassCategory, firstClassCategoryArray } from 'src/app/category/firstClassCategory';
import { SecondClassCategoryLocals, secondClassCategoryLocalsArray } from 'src/app/category/secondClassCategory';
import { SecondClassCategoryGoods, secondClassCategoryGoodsArray } from 'src/app/category/secondClassCategory';
import { SecondClassCategoryHotels, secondClassCategoryHotelsArray } from 'src/app/category/secondClassCategory';
import { ThirdClassCategoryGoodsForTheHome, thirdClassCategoryGoodsForTheHomeArray } from 'src/app/category/thirdClassCategoryGoods';
import { ThirdClassCategoryGoodsHealthAndBeauty, thirdClassCategoryGoodsHealthAndBeautyArray} from 'src/app/category/thirdClassCategoryGoods';
import { ThirdClassCategoryGoodsMenFashion, thirdClassCategoryGoodsMenFashionArray } from 'src/app/category/thirdClassCategoryGoods';
import { ThirdClassCategoryGoodsWomenFashion, thirdClassCategoryGoodsWomenFashionArray } from 'src/app/category/thirdClassCategoryGoods';
import { ThirdClassCategoryGoodsMore, thirdClassCategoryGoodsMoreArray } from 'src/app/category/thirdClassCategoryGoods';
import { ThirdClassCategoryLocalsBeautyAndSpas, thirdClassCategoryLocalsBeautyAndSpasArray } from 'src/app/category/thirdClassCategoryLocals';
import { ThirdClassCategoryLocalsFoodAndDrink, thirdClassCategoryLocalsFoodAndDrinkArray } from 'src/app/category/thirdClassCategoryLocals';
import { ThirdClassCategoryLocalsHealthAndFitness, thirdClassCategoryLocalsHealthAndFitnessArray } from 'src/app/category/thirdClassCategoryLocals';
import { ThirdClassCategoryLocalsMore, thirdClassCategoryLocalsMoreArray } from 'src/app/category/thirdClassCategoryLocals';
import { ThirdClassCategoryLocalsThingsToDo, thirdClassCategoryLocalsThingsToDoArray } from 'src/app/category/thirdClassCategoryLocals';
import { ThirdClassCategoryHotelsAllHotels, thirdClassCategoryHotelsAllHotelsArray } from 'src/app/category/thirdClassCategoryHotels';
import { ThirdClassCategoryHotelsUnder99, thirdClassCategoryHotelsUnder99Array } from 'src/app/category/thirdClassCategoryHotels';



@Component({
  selector: 'app-vendor-signin',
  templateUrl: './vendor-signin.component.html',
  styleUrls: ['./vendor-signin.component.css']
})
export class VendorSigninComponent implements OnInit {

  helper = new JwtHelperService();
  vendorForm: FormGroup;
  firstClassCategory: string;
  firstClassCategoryArray: Array<FirstClassCategory> = firstClassCategoryArray
  secondClassCategoryLocalsArray: Array<SecondClassCategoryLocals> = secondClassCategoryLocalsArray
  secondClassCategoryGoodsArray: Array<SecondClassCategoryGoods> = secondClassCategoryGoodsArray
  secondClassCategoryHotelsArray: Array<SecondClassCategoryHotels> = secondClassCategoryHotelsArray
  thirdClassCategoryGoodsHealthAndBeautyArray: Array<ThirdClassCategoryGoodsHealthAndBeauty> = thirdClassCategoryGoodsHealthAndBeautyArray
  thirdClassCategoryGoodsForTheHomeArray: Array<ThirdClassCategoryGoodsForTheHome> = thirdClassCategoryGoodsForTheHomeArray
  thirdClassCategoryGoodsWomenFashionArray: Array<ThirdClassCategoryGoodsWomenFashion> = thirdClassCategoryGoodsWomenFashionArray
  thirdClassCategoryGoodsMenFashionArray: Array<ThirdClassCategoryGoodsMenFashion> = thirdClassCategoryGoodsMenFashionArray
  thirdClassCategoryGoodsMoreArray: Array<ThirdClassCategoryGoodsMore> = thirdClassCategoryGoodsMoreArray
  thirdClassCategoryLocalsBeautyAndSpasArray: Array<ThirdClassCategoryLocalsBeautyAndSpas> = thirdClassCategoryLocalsBeautyAndSpasArray
  thirdClassCategoryLocalsThingsToDoArray: Array<ThirdClassCategoryLocalsThingsToDo> = thirdClassCategoryLocalsThingsToDoArray
  thirdClassCategoryLocalsFoodAndDrinkArray: Array<ThirdClassCategoryLocalsFoodAndDrink> = thirdClassCategoryLocalsFoodAndDrinkArray
  thirdClassCategoryLocalsHealthAndFitnessArray: Array<ThirdClassCategoryLocalsHealthAndFitness> = thirdClassCategoryLocalsHealthAndFitnessArray
  thirdClassCategoryLocalsMoreArray: Array<ThirdClassCategoryLocalsMore> = thirdClassCategoryLocalsMoreArray
  thirdClassCategoryHotelsAllHotelsArray: Array<ThirdClassCategoryHotelsAllHotels> = thirdClassCategoryHotelsAllHotelsArray
  thirdClassCategoryHotelsUnder99Array: Array<ThirdClassCategoryHotelsUnder99> = thirdClassCategoryHotelsUnder99Array


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
      phone: ["", [Validators.required, Validators.maxLength(12), Validators.minLength(4)]],
      image: ["", [Validators.required, Validators.maxLength(200), Validators.minLength(4)]],
      address: ["", [Validators.required, Validators.maxLength(100), Validators.minLength(4)]],
      zipcode: ["", [Validators.required, Validators.maxLength(100), Validators.minLength(4)]],
      bio: ["", [Validators.required, Validators.maxLength(100), Validators.minLength(4)]],
      firstClass: ["", [Validators.required]],
      secondClass: ["", [Validators.required]],
    })
  }

  signVendor(){}

  showError(error: string){
    this.toastr.error(error, "Error")
  }

  showSuccess() {
    this.toastr.success(`Se ha registrado exitosamente`, "Registro exitoso");
  }

  onSelect(event: any){
    this.firstClassCategory = event.target.value
    console.log(event.target.value)
    if (event.target.value == "GOODS"){
      console.log("the option match with the word GOOD")

    }
  }


}
