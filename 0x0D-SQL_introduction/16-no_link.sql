-- listall records if the tale having a name value in the mysql server
--order is by descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
