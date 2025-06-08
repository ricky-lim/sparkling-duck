#%% [markdown]

# Sparkling Duck

#%%

movie = "data/movies.parquet"

#%%
import os

from pyspark.sql import SparkSession

import pyspark.sql.functions as F

# Ensure JAVA environment variable is set
java_home = os.path.expandvars("$HOME/.sdkman/candidates/java/17.0.10-amzn")
os.environ['JAVA_HOME'] = java_home
os.environ['PATH'] = java_home + '/bin:' + os.environ['PATH']


spark = SparkSession.builder.appName("Sparklie").getOrCreate()

#%%
%%timeit -r 3 -n 1

print(f"Spark version: {spark.version}")

# Check popular genres
spark_result = (
    spark.read.parquet(movie)
        .select(F.split(F.col("Genre"), ",").alias("Genre"))
        .select(F.explode(F.col("Genre")).alias("Genre"))
        .select(F.trim(F.col("Genre")).alias("Genre"))
        .select(F.lower(F.col("Genre")).alias("Genre"))
        .groupBy("Genre")
        .count()
        .orderBy("count", ascending=False)
        .limit(10)
)

spark_result.show()

#%%
import duckdb

#%%
%%timeit -r 3 -n 1

print(f"DuckDB version: {duckdb.__version__}")

duck_result = (
    duckdb.from_parquet(movie)
        .project("split(Genre, ',') AS genres")
        .project("unnest(genres) AS genres")
        .project("trim(lower(genres)) AS Genre")
        .aggregate("Genre, COUNT(*) AS count")  
        .order("count DESC")                    
        .limit(10)             
)

duck_result.show()

# %%
