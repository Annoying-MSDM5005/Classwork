import pandas as pd
import geopandas as gpd

def read_json_data(path,epsg=4326,loc_cols=['lng','lat'],drop_duplicates=False):
    """
    Read the json data and return a geopandas dataframe
    """
    df = pd.read_json(path)
    if drop_duplicates:
        df.drop_duplicates(inplace=True)
    df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[loc_cols[0]], df[loc_cols[1]]))
    df.set_crs(epsg=epsg,inplace=True)
    return df