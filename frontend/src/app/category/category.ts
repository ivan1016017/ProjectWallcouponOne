import { FirstClassCategory } from "./firstClassCategory";
import { SecondClassCategoryLocals } from "./secondClassCategory";
import { SecondClassCategoryLocalsGoods } from "./secondClassCategory";
import { SecondClassCategoryLocalsHotels } from "./secondClassCategory";
import { ThirdClassCategoryLocals } from "./thirdClassCategory";
import { ThirdClassCategoryLocalsGoods } from "./thirdClassCategory";
import { ThirdClassCategoryLocalsHotels } from "./thirdClassCategory";

export class Category {
  id: number;
  firstClassCategory: FirstClassCategory;
  secondClassCategoryLocals: SecondClassCategoryLocals;
  secondClassCategoryGoods: SecondClassCategoryLocalsGoods;
  secondClassCategoryHotels: SecondClassCategoryLocalsHotels;
  thirdClassCategoryLocals: ThirdClassCategoryLocals;
  thirdClassCategoryGoods: ThirdClassCategoryLocalsGoods;
  thirdClassCategoryHotels: ThirdClassCategoryLocalsHotels;

}
