import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
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
  selector: 'app-create-coupon',
  templateUrl: './create-coupon.component.html',
  styleUrls: ['./create-coupon.component.css']
})
export class CreateCouponComponent implements OnInit {

  couponForm: FormGroup



  constructor() { }

  ngOnInit() {
  }

}
