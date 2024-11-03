SELECT
    race_name,
    finishing_position AS position,  
    starting_grid AS grid,
    fastest_lap_time AS fastest_lap,
    championship_points AS points,
    driver_name,
    race_date,
    driver_nationality AS nationality,
    team_name AS team
FROM
    race_results
JOIN
    races ON race_results.race_id = races.race_id  
JOIN
    drivers ON race_results.driver_id = drivers.driver_id
JOIN 
    teams ON drivers.team_id = teams.team_id
WHERE
    race_year = 2020
ORDER BY
    championship_points DESC;