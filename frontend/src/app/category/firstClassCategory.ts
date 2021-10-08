export class FirstClassCategory{
  key: string;
  value: number
  constructor(
    key: string,
    value: number
  ){
    this.key = key,
    this.value = value
  }
}

let firstClassCategoryArray: Array<FirstClassCategory> = [
  {    key: "LOCALS",
        value:  1
},
{    key: "GOODS",
value:  2
},
{    key: "HOTELS",
value:  3
},

]

export {firstClassCategoryArray}
