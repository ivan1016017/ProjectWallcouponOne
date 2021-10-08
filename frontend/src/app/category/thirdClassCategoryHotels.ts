export class ThirdClassCategoryHotelsAllHotels{
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

export class ThirdClassCategoryHotelsUnder99{
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


let thirdClassCategoryHotelsAllHotelsArray: Array<ThirdClassCategoryHotelsAllHotels> = [
  {    key: "AirInclusiveTrips",
    value:  1
  },
  {    key: "Beach",
  value:  2
  },
  {    key: "Premium",
  value:  3
  },
  {    key: "FamilyFun",
  value:  4
  },
  {    key: "InternationalAndTours",
  value:  5
  },
  ]


  let thirdClassCategoryHotelsUnder99Array: Array<ThirdClassCategoryHotelsUnder99> = [
    {    key: "NewDeals",
      value:  1
    },
    {    key: "OutdoorAndAdventure",
    value:  2
    },
    {    key: "RomanticGetaways",
    value:  3
    },
    ]


export {thirdClassCategoryHotelsAllHotelsArray}

export {thirdClassCategoryHotelsUnder99Array}
