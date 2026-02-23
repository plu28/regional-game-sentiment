# Drop unnecessary rows, and format data
import duckdb
input = "../archive/all_reviews/all_reviews.csv"
output = "../datareviews"
min_reviews = 1000


# entries = duckdb.sql(f'''
#         SELECT
#             game,
#             language,
#             voted_up,
#         FROM read_csv_auto('{input}', max_line_size=10485760)
#     COPY (
#     ) 
#     TO '{output}.parquet'
#     (FORMAT parquet, COMPRESSION snappy)
# ''')
# print(f"Generating {output}.parquet file.")
# duckdb.sql(f'''
#     COPY (
#         SELECT * FROM entries
#     ) 
#     TO '{output}.parquet'
#     (FORMAT parquet, COMPRESSION snappy)
# ''')
#
# print("Generating aggregated csv file for tableau.")
# duckdb.sql(f'''
# COPY (
#     SELECT
#         game,
#         language,
#         SUM(voted_up) AS up_votes, 
#         COUNT(*) AS review_amt
#     FROM read_csv_auto('{input}', max_line_size=10485760)
#     GROUP BY game, language
#     HAVING review_amt > '{min_reviews}'
#         ) 
# TO '{output}.csv'
# ''')

# csv with sentiment and popularity computed for tableau
base = duckdb.sql(f'''
    SELECT
        language,
        game,
        voted_up
    FROM '{output}.parquet'
              ''')
duckdb.sql(f'''
COPY (
        WITH reg_reviews_tbl AS (
            SELECT
                language,
                game,
                AVG(voted_up) AS reg_positive_percent,
                COUNT(*) AS region_game_reviews
            FROM base
            GROUP BY language, game
            HAVING region_game_reviews > 100
        ),
        reg_total_reviews_tbl AS (
            SELECT
                language,
                COUNT(*) AS region_total_reviews
            FROM base
            GROUP BY language
        ),
        global_game_reviews_tbl AS (
            SELECT
                game,
                AVG(voted_up) AS global_positive_percent,
                COUNT(*) AS global_game_reviews,
            FROM base
            GROUP BY game
        ),
        global_reviews_tbl AS (
            SELECT
                COUNT(*) AS global_reviews
            FROM base
        )
        SELECT
            rrc.language,
            rrc.game,
            (rrc.region_game_reviews / rtr.region_total_reviews) / (ggr.global_game_reviews / gr.global_reviews) AS popularity,
            (rrc.reg_positive_percent) / (ggr.global_positive_percent) AS sentiment,
            rrc.reg_positive_percent, 
            rrc.region_game_reviews,
            ggr.global_game_reviews,
            ggr.global_positive_percent,
        FROM
            reg_reviews_tbl rrc
            JOIN reg_total_reviews_tbl rtr ON rtr.language = rrc.language
            JOIN global_game_reviews_tbl ggr ON ggr.game = rrc.game
            CROSS JOIN global_reviews_tbl gr
        WHERE ggr.global_game_reviews > 100000 AND rrc.region_game_reviews > 100
        ORDER BY popularity DESC
        ) 
TO 'game-region-sentiment-popularity.csv'
''')

