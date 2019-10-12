select * from imdb;
create table results

select box_office.movie_title, box_office.release_year, box_office.inflation_adjusted_gross,
imdb.imdb_rating, imdb.rating_count, imdb.wins, imdb.nominations
into results 
from box_office
join imdb
on box_office.movie_title = imdb.movie_title
and box_office.release_year = imdb.release_year;

select * from results;

SELECT
   *
FROM
   results
WHERE
  inflation_adjusted_gross = (
    SELECT
        MAX (inflation_adjusted_gross)
   FROM
      results
);
SELECT
   *
FROM
   results
WHERE
  imdb_rating = (
    SELECT
        MAX (imdb_rating)
   FROM
      results
);
