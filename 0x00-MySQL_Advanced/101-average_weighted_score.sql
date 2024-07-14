-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users AS US, (SELECT user_id,
			    SUM(score * weight) / SUM(weight) AS w_Avg
                            FROM corrections INNER JOIN projects
                            ON corrections.project_id = projects.id
                            GROUP BY user_id) AS WAVG
	SET US.average_score=WAVG.w_Avg
	WHERE US.id = WAVG.user_id;
END
$$
DELIMITER ;