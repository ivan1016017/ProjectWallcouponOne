import enum


class FirstClassCategory(enum.Enum):
    LOCALS = 1
    GOODS = 2
    HOTELS = 3

class SecondClassCategoryLocals(enum.Enum):
    BEAUTYANDSPAS = 1
    THINGSTODO = 2
    FOODANDDRINK = 3
    HEALTHANDFITNESS = 4
    MORE = 4
    

class SecondClassCategoryGoods(enum.Enum):
    HEALTHANDBEAUTY = 1
    FORTHEHOME = 2
    WOMENFASHION = 3 
    MENFASION = 4
    MORE = 5


class SecondClassCategoryHotels(enum.Enum):
    HOTEL = 1
    DEALS = 2

class ThirdClassCategoryLocals(enum.Enum):
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
    Tanning = 11
    BlowoutsAndStyling = 12
    KidsActivities = 13
    FunAndLeisure = 14
    TicketsEvents = 15
    SightseeingTours = 16
    SportsOutdoors = 17
    Nightlife = 18
    Restaurants = 19
    BreweriesWineriesDistilleries = 20
    CafesTreats = 21
    GroceriesAndMarkets = 22
    Bars = 23
    Gyms = 24
    WeightLoss = 25
    FitnessClasses = 26
    Medical = 27
    Sports = 28
    NaturalMedicine = 29
    Dental = 30
    Vision = 31


class ThirdClassCategoryGoods(enum.Enum):
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
    Art = 15
    Bath = 16
    Bedding = 17
    FloorCareAndCleaning = 18
    Furniture = 19
    HeatingCoolingAndAirQuality = 20
    HomeAppliances = 21
    HomeDecor = 22
    KitchenAndDining = 23
    Luggage = 24
    MattressesAndAccessories = 25
    OfficeAndSchoolSupplies = 26
    OutdoorDecor = 27
    PatioAndGarden = 28
    SeasonalDecor = 29
    StorageAndOrganization = 30
    Intimates = 31
    MaternityClothing = 32
    PlusSizeClothing = 33
    WomenAccessories = 34
    WomenClothing = 35
    WomenShoes = 36
    MenAccessories = 37
    MenClothing = 38
    MenShoes = 39

class ThirdClassCategoryHotels(enum.Enum):
    AirInclusiveTrips = 1 
    Beach = 2
    Premium = 3
    FamilyFun = 4
    InternationalAndTours = 5
    NewDeals = 6
    OutdoorAndAdventure = 7
    RomanticGetaways = 8