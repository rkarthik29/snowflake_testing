# import snowflake.connector
# #import bodo
# import time
# from sqlalchemy.dialects import registry
# registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

# import os
# with open("/shared/snowflake_testing/snowflake-secrets.txt","r") as f:
#     for line in f:
#         args=line.split("=")
#         os.environ[args[0]]=args[1].strip()
# username=os.environ["username"]
# password=os.environ["password"]
# account=os.environ["account"]
# warehouse="BODO_VW"
# database="BODO_DB"
# role="BODO_R1"


import pandas as pd
import bodo
@bodo.jit
def load_data_testing_results():
    
    df=pd.read_parquet("part-000.parquet")
    return df
trips_testing_total=load_data_testing_results()

# @bodo.jit
# def write_to_sf(df):
#     df=df.head(20)
#     df.to_sql("TRIPS_TESTING_BODO",f"snowflake://{username}:{password}@{account}/{database}/public?role={role}&warehouse={warehouse}",if_exists="append",index=False)

# write_to_sf(trips_testing_total)