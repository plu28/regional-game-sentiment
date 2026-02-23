# A lot of this is mostly unused. was initially going to use duckdb more but decided to instead convert to csv's and tableau
import duckdb

input_file = 'reviews.parquet'
review_min = 1000 # Ignore any games with less than this many reviews. They're not popular enough

def main():
    # Regions and their representation in the data
    # res = duckdb.sql(f'''
    #     SELECT 
    #         language,
    #         COUNT(*) OVER (PARTITION BY language) * 1.0
    #         / COUNT(*) OVER () AS representation
    #     FROM '{input_file}'
    #     GROUP BY language
    #          ''')
    # print(res)

    # Games and the reviews per game
    # res = duckdb.sql(f'''
    #     SELECT
    #         game,
    #         COUNT(*) AS review_count,
    #     FROM
    #         '{input_file}'
    #     GROUP BY game
    #     HAVING review_count > '{review_min}'
    # ''')
    # print(res)

    # Compute ratio of voted up to voted down of a game per region
    # res = duckdb.sql(f'''
    #     SELECT
    #         language,
    #         game, 
    #         AVG(voted_up) AS up_ratio,
    #         SUM(voted_up) AS number_up,
    #         COUNT(*) AS review_amt,
    #     FROM '{input_file}'
    #     GROUP BY language, game
    #     HAVING review_amt >= '{review_min}' 
    #     ORDER BY up_ratio DESC
    #
    #            ''')
    # print(res)

    base = duckdb.sql(f'''
        SELECT
            language,
            game,
            voted_up
        FROM '{input_file}'
                  ''')



    # How popular a game is in a region
    # A games popularity is calculated using the amount of reviews that game has in the region: 
    # (region_game_reviews / region_total_reviews) / (global_game_reviews / global_reviews) 
    # If a region has >1.0, that means that game is more popular in that region and vice versa
    res = duckdb.sql(f'''
        WITH reg_reviews_tbl AS (
            SELECT
                language,
                game,
                COUNT(*) AS region_game_reviews
            FROM base
            GROUP BY language, game
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
                COUNT(*) AS global_game_reviews
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
            rrc.region_game_reviews,
            ggr.global_game_reviews
        FROM
            reg_reviews_tbl rrc
            JOIN reg_total_reviews_tbl rtr ON rtr.language = rrc.language
            JOIN global_game_reviews_tbl ggr ON ggr.game = rrc.game
            CROSS JOIN global_reviews_tbl gr
        WHERE ggr.global_game_reviews > 100000 AND rrc.region_game_reviews > 100
        ORDER BY popularity DESC
             ''')
    print(res)

    # Tell me the highest rated games by region

    # Look for games that between two regions, have a difference in up_ratio greater than some percent. This signals different cultural game preference maybe
    # Look for games that have a high review count in one region but low in other regions

if __name__ == "__main__":
    main()
