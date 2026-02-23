# Make a 5MB sample of the full dataset for exploratory analysis
import duckdb
file = "archive/all_reviews/all_reviews.csv"
output = "../data/review_sample.csv"
number_of_rows = 10000 

print(f"Making a sample with {number_of_rows} rows.")

duckdb.sql(f'''
COPY (
    SELECT * FROM read_csv_auto('{file}', max_line_size=10485760)
    USING SAMPLE RESERVOIR ({number_of_rows} ROWS)
)
TO {output}
''')

