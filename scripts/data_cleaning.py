# Drop unnecessary rows, and format data
import duckdb
input = "../archive/all_reviews/all_reviews.csv"
output = "../data/reviews"
min_reviews = 1000


# entries = duckdb.sql(f'''
#     COPY (
#         SELECT
#             game,
#             language,
#             voted_up,
#             timestamp_created AS timestamp,
#         FROM read_csv_auto('{input}', max_line_size=10485760)
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
        voted_up,
        timestamp,
    FROM '{output}.parquet'
              ''')
# duckdb.sql(f'''
# COPY (
#         WITH reg_reviews_tbl AS (
#             SELECT
#                 language,
#                 game,
#                 AVG(voted_up) AS reg_positive_percent,
#                 COUNT(*) AS region_game_reviews
#             FROM base
#             GROUP BY language, game
#             HAVING region_game_reviews > 100
#         ),
#         reg_total_reviews_tbl AS (
#             SELECT
#                 language,
#                 COUNT(*) AS region_total_reviews
#             FROM base
#             GROUP BY language
#         ),
#         global_game_reviews_tbl AS (
#             SELECT
#                 game,
#                 AVG(voted_up) AS global_positive_percent,
#                 COUNT(*) AS global_game_reviews,
#             FROM base
#             GROUP BY game
#         ),
#         global_reviews_tbl AS (
#             SELECT
#                 COUNT(*) AS global_reviews
#             FROM base
#         )
#         SELECT
#             rrc.language,
#             rrc.game,
#             (rrc.region_game_reviews / rtr.region_total_reviews) / (ggr.global_game_reviews / gr.global_reviews) AS popularity,
#             (rrc.reg_positive_percent) / (ggr.global_positive_percent) AS sentiment,
#             rrc.reg_positive_percent, 
#             rrc.region_game_reviews,
#             ggr.global_game_reviews,
#             ggr.global_positive_percent,
#         FROM
#             reg_reviews_tbl rrc
#             JOIN reg_total_reviews_tbl rtr ON rtr.language = rrc.language
#             JOIN global_game_reviews_tbl ggr ON ggr.game = rrc.game
#             CROSS JOIN global_reviews_tbl gr
#         WHERE ggr.global_game_reviews > 100000 AND rrc.region_game_reviews > 100
#         ORDER BY popularity DESC
#         ) 
# TO 'game-region-sentiment-popularity.csv'
# ''')


# CSV with review timestamps for OW2 China review visualization
# res = duckdb.sql(f'''
#     COPY (
#         SELECT
#             language,
#             voted_up,
#             timestamp,
#         FROM '{output}.parquet'
#         WHERE game = 'Overwatch® 2' AND (language = 'schinese' OR language = 'tchinese' OR language = 'english')
# ) 
#     TO 'avg-rating-with-time.csv'
# ''')

# Debugging
# res = duckdb.sql(f'''
#             SELECT
#                 language,
#                 game,
#                 AVG(voted_up) AS reg_positive_percent,
#                 COUNT(*) AS region_game_reviews
#             FROM base
#             GROUP BY language, game
#             HAVING region_game_reviews = 2487 AND game = 'Red Dead Redemption 2'
# ''')

# Counting games vs cut down
res = duckdb.sql(f'''
            SELECT
                COUNT(DISTINCT game) AS game_count,
            FROM base
''')
print(res)

# Cut down games have 100,000 global reviews and at least 100 regional reviews
res = duckdb.sql(f'''
             WITH regions_game_reviews AS (
                SELECT
                    COUNT(*) AS region_game_reviews,
                    game,
                FROM base
                GROUP BY game, language
                HAVING region_game_reviews > '{min_reviews}'
             )
            SELECT
                COUNT(DISTINCT game) AS filtered_game_count,
            FROM regions_game_reviews 
''')
print(res)
