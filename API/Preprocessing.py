import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

class DataProcessor:

    def Preprocess_categorical_features(self,input):
        # Map the 'property_type' column to an ordinal scale
        property_type = {'HOUSE': 1, 'APARTMENT': 0}
        if 'property_type' in input.columns:
            input['property_type'] = input['property_type'].map(property_type).fillna(-1)

        provinces = [
             'province_Brussels','province_East Flanders','province_Flemish Brabant',
              'province_Hainaut','province_Limburg','province_Liège', 'province_Luxembourg', 'province_Namur',
               'province_Walloon Brabant','province_West Flanders'
               #, 'province_Antwerp'
        ]
        if 'province' in input.columns:
            input['province'] = input['province'].str.lower()
            
            # Initialize province columns with 0
            for province in provinces:
                input[province] = 0
            
            for province in provinces:
                province_name = province.split('_', 1)[1].lower()
                input[province] = input['province'].apply(lambda x: 1 if x == province_name else 0)
            
            input.drop('province', axis=1, inplace=True)
            
        building_state_hierarchy = [
            'TO_RESTORE', 'TO_BE_DONE_UP', 'TO_RENOVATE',
            'JUST_RENOVATED', 'GOOD', 'AS_NEW'
        ]
        encoder_building = OrdinalEncoder(categories=[building_state_hierarchy])

        # Convert to DataFrame to allow fillna
        input['state_building'] = pd.Series(
            encoder_building.fit_transform(input[['state_building']]).flatten()
        ).fillna(-1)

        epc_hierarchy = ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'A+', 'A++']
        encoder_epc = OrdinalEncoder(categories=[epc_hierarchy])

        # Convert to DataFrame or Series to apply fillna
        input['epc'] = pd.Series(
            encoder_epc.fit_transform(input[['epc']]).flatten()
        ).fillna(-1)

        # Map 'heating_type' to an ordinal scale
        energy_order = {
            'CARBON': 0, 'WOOD': 1, 'PELLET': 2, 'FUELOIL': 3,
            'GAS': 4, 'ELECTRIC': 5, 'SOLAR': 6
        }
        if 'heating_type' in input.columns:
            input['heating_type'] = input['heating_type'].map(energy_order).fillna(-1)

        return input

    def preprocess(self,input):
        # Convert the dictionary to a DataFrame
        data_df = pd.DataFrame([input])
        encoded_data= self.Preprocess_categorical_features(data_df)

        return encoded_data

   