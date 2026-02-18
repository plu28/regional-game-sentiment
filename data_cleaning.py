# Drop unnecessary rows, and format data
import duckdb
input = "./archive/all_reviews/all_reviews.csv"
output = "reviews.parquet"

# Made executive decision to only keep a few columns that I need

print("Compressing review csv.")
duckdb.sql(f'''
    COPY (
        SELECT
            game,
            language,
            voted_up,
        FROM read_csv_auto('{input}', max_line_size=10485760)
    ) 
    TO '{output}'
    (FORMAT parquet, COMPRESSION snappy)
''')
print("Done")

