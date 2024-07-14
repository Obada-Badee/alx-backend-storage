-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
	BEGIN
		UPDATE users
		SET average_score=(SELECT AVG(score) FROM corrections WHERE corrections.id = user_id)
		WHERE users.id=user_id;
	END
	$$
DELIMITER ;
