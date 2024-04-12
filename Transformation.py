from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Simple PySpark Example") \
    .getOrCreate()

# Read CSV file into DataFrame
df = spark.read.csv("path/to/your/csv/file.csv", header=True, inferSchema=True)

# Show the first few rows of the DataFrame
df.show()

# Perform some transformations (e.g., filter, select)
filtered_df = df.filter(df["column_name"] > 10)
selected_df = filtered_df.select("column_name", "another_column")

# Show the results
selected_df.show()

# Stop the SparkSession
spark.stop()
