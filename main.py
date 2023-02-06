import polars as pl
import datetime

series = pl.Series("Fibonacci",[0,1,1,2,3,5,8])
#print(series)

df_new = {
    "name": ["Alice","Steven","Joshua"],
    "age": [18,39,21],
    "email": ["alice123@yahoo.com","stuniverse3@gmail.com","markiman@hotmail.com"],
    "phone_number": [None,None,None],
    "created_at": [
        "2023-02-06",
        "2023-02-06",
        "2023-02-06"
        #(pl.datetime(2023,2,6)),
        #(pl.datetime(2023,2,6)),
        #(pl.datetime(2023,2,6))
    ]
}

# Polars can also interpret dates without calling datetime by typing dates as: "yyyy-mm-dd"

ds = pl.DataFrame(df_new)

parsed_ds = ds.lazy().with_columns(pl.col("created_at").str.strptime(pl.Date,"%Y-%m-%d"))
parsed_ds.collect() # If we are applying parsing to our dataset, polars will need to call collect() to print it.