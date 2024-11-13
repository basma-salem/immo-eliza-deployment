from fastapi import FastAPI ,  HTTPException
from pydantic import BaseModel
from typing import Literal , Optional
from API.predict import predictions

    

app = FastAPI()

@app.get("/")
async def base():
    return {"message": "alive"}

EXPECTED_FEATURE_ORDER = ['zip_code', 'total_area_sqm', 'surface_land_sqm', 'nbr_frontages', 
 'nbr_bedrooms', 'terrace_sqm', 'garden_sqm',
 'property_type', 'state_building', 'heating_type', 
    'province','epc'
]

class PropertyData(BaseModel):
    property_type: Literal['APPARTMENT', 'HOUSE']
    province: Literal[ 'Brussels','East Flanders','Flemish Brabant',
              'Hainaut','Limburg','Liège', 'Luxembourg', 'Namur',
               'Walloon Brabant','West Flanders', 'Antwerp' ]
    zip_code:Optional[int]= 0
    total_area_sqm: Optional[int]= 0
    nbr_bedrooms: int
    surface_land_sqm: Optional[float]= 0
    state_building:Literal['TO_RESTORE','TO_BE_DONE_UP', 'TO_RENOVATE', 'JUST_RENOVATED','GOOD','AS_NEW']
    heating_type:Literal['CARBON','WOOD','PELLET','FUELOIL','GAS','ELECTRIC','SOLAR']
    epc:Literal['G', 'F', 'E', 'D','C','B','A','A+','A++']
    nbr_frontages:Optional[float]= 0
    terrace_sqm: Optional[float]= 0
    garden_sqm:Optional[float]= 0
    state_building:Literal['AS_NEW','TO_RESTORE','TO_BE_DONE_UP', 'TO_RENOVATE', 'JUST_RENOVATED','GOOD']
    heating_type:Literal['GAS','CARBON','WOOD','PELLET','FUELOIL','ELECTRIC','SOLAR']
    epc:Literal['G', 'F', 'E', 'D','C','B','A','A+','A++']
    
@app.post("/predict")
async def predictPrice(data: PropertyData):
    try:
        input_data = data.model_dump()
        reordered_data = {feature: input_data[feature] for feature in EXPECTED_FEATURE_ORDER}
        return predictions(reordered_data)
    except ValueError as e:
        # Handle invalid input values
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    
    except KeyError as e:
        # Handle missing keys
        raise HTTPException(status_code=422, detail=f"Missing key: {str(e)}")
    
    except Exception as e:
        # Handle any other unexpected errors
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

