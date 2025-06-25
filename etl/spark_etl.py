from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark4_ETL") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.json("data/sample.json")  # Replace with your path
df.show()
