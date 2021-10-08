import enum


class FirstClassCategory(enum.Enum):
    LOCALS = 1
    GOODS = 2
    HOTELS = 3

class SecondClassCategoryLocals(enum.Enum):
    BeautyAndSpas = 1
    ThingsToDo = 2
    FoodAndDrink = 3
    HealthAndFitness = 4
    More = 5
    

class SecondClassCategoryGoods(enum.Enum):
    HealthAndBeauty = 1
    ForTheHome = 2
    WomenFashion = 3 
    MenFashion = 4
    More = 5


class SecondClassCategoryHotels(enum.Enum):
    Hotels = 1
    Deals = 2

class ThirdClassCategoryLocalsBeautyAndSpas(enum.Enum):
    FaceSkinCare = 1
    Massage = 2
    Salons = 3
    CosmeticProcedures = 4
    BrowsAndLashes = 5
    HairRemoval = 6
    Spas = 7
    HairStyling = 8
    NailSalons = 9
    Makeup =  10
class ThirdClassCategoryLocalsThingsToDo(enum.Enum):
    Tanning = 1
    BlowoutsAndStyling = 2
    KidsActivities = 3
    FunAndLeisure = 4
    TicketsEvents = 5
    SightseeingTours = 6
    SportsOutdoors = 7
    Nightlife = 8
class ThirdClassCategoryLocalsFoodAndDrink(enum.Enum):
    Restaurants = 1
    BreweriesWineriesDistilleries = 2
    CafesTreats = 3
    GroceriesAndMarkets = 4
    Bars = 5
class ThirdClassCategoryLocalsHealthAndFitness(enum.Enum):
    Gyms = 1
    WeightLoss = 2
    FitnessClasses = 3
    Medical = 4
    Sports = 5
    NaturalMedicine = 6
    Dental = 7
    Vision = 8
class ThirdClassCategoryLocalsMore(enum.Enum):
    Automotive: 1
    HomeServices: 2
    MealPrepAndWineDelivery: 3
    OnlineLearning: 4
    PersonalServices:5
    PersolizedItems:6
    Retail:7


class ThirdClassCategoryGoodsHealthAndBeauty(enum.Enum):
    Aromatherapy = 1
    BathAndBody = 2
    Cosmetics = 3
    Fragrance = 4
    HairCare = 5
    HealthCare = 6
    Massage = 7
    MenHealthAndBeauty = 8
    OralCare = 9
    PersonalCare = 10
    SexualWellness = 11
    ShavingAndGrooming = 12
    SkinCare = 13
    VitaminsAndSupplements = 14
class ThirdClassCategoryGoodsForTheHome(enum.Enum):
    Art = 1
    Bath = 2
    Bedding = 3
    FloorCareAndCleaning = 4
    Furniture = 5
    HeatingCoolingAndAirQuality = 6
    HomeAppliances = 7
    HomeDecor = 8
    KitchenAndDining = 9
    Luggage = 10
    MattressesAndAccessories = 11
    OfficeAndSchoolSupplies = 12
    OutdoorDecor = 13
    PatioAndGarden = 14
    SeasonalDecor = 15
    StorageAndOrganization = 16
class ThirdClassCategoryGoodsWomenFashion(enum.Enum):
    Intimates = 1
    MaternityClothing = 2
    PlusSizeClothing = 3
    WomenAccessories = 4
    WomenClothing = 5
    WomenShoes = 6
class ThirdClassCategoryGoodsMenFashion(enum.Enum):
    MenAccessories = 1
    MenClothing = 2
    MenShoes = 3
class ThirdClassCategoryGoodsMore(enum.Enum):
    AutoAndHomeImprovement = 1
    BadyAndKids = 2
    Electronics = 3
    Entertainment = 4
    GroceryAndHousehold = 5
    JewelryAndWatches = 6
    PersonalizedItems = 7
    PetSupplies = 8
    SportsAndOutdoors = 9
    Toys = 10


class ThirdClassCategoryHotelsAllHotels(enum.Enum):
    AirInclusiveTrips = 1 
    Beach = 2
    Premium = 3
    FamilyFun = 4
    InternationalAndTours = 5
class ThirdClassCategoryHotelsUnder99(enum.Enum):
    NewDeals = 1
    OutdoorAndAdventure = 2
    RomanticGetaways = 3