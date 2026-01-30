import pandas as pd

###############
# Constants
###############
DATA_FNAME: str = "L10_coffee.csv"
DATA: dict[str, list[Any]] = {
'roaster': ['dunkin', 'onyx', 'pavement'],
'name': ['original blend', 'ethiopia bochesa natural', 'Rathskeller'],
'grams': [2040, 283, 20],
'price': [47.82, 27, 1.05]
}


###############
def get_data_csv() -> pd.DataFrame:
    """ 
    Gets sample data from a CSV
    
    Returns
    =======
    pd.DataFrame
    data☕️
   
    Raises
    ======
    FileNotFoundError
    Cannot find DATA_FNAME
    """
    return pd.read_csv(DATA_FNAME)


def get_data_literal() -> pd.DataFrame:
    """
    Gets sample data from Python code
    Returns
    =======
    pd.DataFrame
    data☕️
    """
    return pd.DataFrame(DATA)
    
def data_structure() -> pd.DataFrame:
    """
    Looks at the data big-picture
    """
    csv_df: pd.DataFrame = get_data_csv()
    python_df: pd.DataFrame = get_data_literal()

# seeing what the csv produces in code :)
print(f"DFs are same: { csv_df.equals(python_df) }")
#when checking if equal if they are not then 
# can use compare to see line by line if they are equal