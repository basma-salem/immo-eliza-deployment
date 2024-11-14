from fastapi import FastAPI ,  HTTPException
from pydantic import BaseModel
from typing import Literal , Optional
from predict import predictions

    

app = FastAPI()

@app.get("/")
async def base():
    return {"message": "alive"}

Features_orders = ['zip_code', 'total_area_sqm', 'surface_land_sqm', 'nbr_frontages', 
 'nbr_bedrooms', 'terrace_sqm', 'garden_sqm',
 'property_type', 'state_building', 'heating_type'
  ,'epc' , 'province'
]

class PropertyData(BaseModel):
    property_type: Literal['APARTMENT', 'HOUSE']
    province: Literal[ 'Brussels','East Flanders','Flemish Brabant',
              'Hainaut','Limburg','Liège', 'Luxembourg', 'Namur',
               'Walloon Brabant','West Flanders', 'Antwerp' ]
    zip_code:Optional[int]= 0
    total_area_sqm: Optional[int]= 0
    nbr_bedrooms: int
    surface_land_sqm: Optional[float]= 0
    state_building:Literal['AS_NEW', 'JUST_RENOVATED','GOOD','TO_RESTORE','TO_BE_DONE_UP', 'TO_RENOVATE']
    heating_type:Literal['GAS','ELECTRIC','SOLAR','CARBON','WOOD','PELLET','FUELOIL']
    epc:Literal['A++','A+','A','B','C','D','E','F', 'G' ]
    nbr_frontages:Optional[int]= 0
    terrace_sqm: Optional[float]= 0
    garden_sqm:Optional[float]= 0
    
@app.post("/predict")
async def predictPrice(data: PropertyData):
    try:
        input_data = data.model_dump()
        reordered_data = {feature: input_data[feature] for feature in Features_orders}
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

