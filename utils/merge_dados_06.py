from .load_csv import load_csv
from .load_shp import load_shp
from .save_shp import save_shp
import pandas as pd

def funcao_merge_dados(
        df_ppa_fonte=load_csv("ppa_fonte.csv"),
        df_ppa_reg = load_csv("ppa_reg.csv"),
        gdf_subprefs = load_shp("subprefs.shp")
):
    
    df_ppa_merged = df_ppa_fonte.merge(
        df_ppa_reg,
        left_on = "id",
        right_on = "id",
        how = "left"
    )
    gdf_merged = gdf_subprefs.merge(
        df_ppa_merged,
        left_on = "nm_subpref",
        right_on = "descricao prefeitura regional",
        how = "left"
    )

    pd.set_option("display.max_columns", None)
    import warnings
    warnings.filterwarnings("ignore", category = UserWarning)
    warnings.filterwarnings("ignore", category = RuntimeWarning)

    save_shp(gdf_merged, "gdf_merged.shp")

    return gdf_merged

def caregar_dados_plusmerge_teste(
        df_ppa_fonte=load_csv("ppa_fonte.csv"),
        df_ppa_reg = load_csv("ppa_reg.csv"),
        gdf_subprefs = load_shp("subprefs.shp")
):
    
    df_ppa_merged = df_ppa_fonte.merge(
        df_ppa_reg,
        left_on = "id",
        right_on = "id",
        how = "left"
    )
    gdf_merged = gdf_subprefs.merge(
        df_ppa_merged,
        left_on = "nm_subpref",
        right_on = "descricao prefeitura regional",
        how = "left"
    )

    pd.set_option("display.max_columns", None)
    import warnings
    warnings.filterwarnings("ignore", category = UserWarning)
    warnings.filterwarnings("ignore", category = RuntimeWarning)

    save_shp(gdf_merged, "gdf_merged.shp")

    return df_ppa_reg, gdf_subprefs, gdf_merged