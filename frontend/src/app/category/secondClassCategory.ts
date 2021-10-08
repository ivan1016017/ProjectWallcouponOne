export class SecondClassCategoryLocals{
  key: string;
  value: number
  constructor(
    key: string,
    value: number
  ){
    this.key = key
    this.value = value
  }
}

export class SecondClassCategoryGoods{
  key: string;
  value: number
  constructor(
    key: string,
    value: number
  ){
    this.key = key
    this.value = value
  }
}

export class SecondClassCategoryHotels{
  key: string;
  value: number
  constructor(
    key: string,
    value: number
  ){
    this.key = key
    this.value = value
  }
}


let secondClassCategoryLocalsArray: Array<SecondClassCategoryLocals> = [
  {    key: "BeautyAndSpas",
  value:  1
},
{    key: "ThingsToDo",
value:  2
},
{    key: "FoodAndDrink",
value:  3
},
{    key: "HealthAndFitness",
value:  4
},
{    key: "More",
value:  5
}
]

let secondClassCategoryGoodsArray: Array<SecondClassCategoryGoods> = [
  {    key: "HealthAndBeauty",
  value:  1
},
{    key: "ForTheHome",
value:  2
},
{    key: "WomenFashion",
value:  3
},
{    key: "MenFashion",
value:  4
},
{    key: "More",
value:  5
}
]

let secondClassCategoryHotelsArray: Array<SecondClassCategoryHotels> = [
  {    key: "Hotels",
  value:  1
},
{    key: "Deals",
value:  2
}
]

export { secondClassCategoryLocalsArray, secondClassCategoryGoodsArray, secondClassCategoryHotelsArray}
