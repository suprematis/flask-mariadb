CREATE TABLE flasktest.tasks (task_id INT NOT NULL AUTO_INCREMENT, task_title VARCHAR(50), task_status VARCHAR(50), PRIMARY KEY (task_id));
INSERT INTO flasktest.tasks (task_title, task_status) VALUES ('Task 1', 'Success');
INSERT INTO flasktest.tasks (task_title, task_status) VALUES ('Task 2', 'Pending');
INSERT INTO flasktest.tasks (task_title, task_status) VALUES ('Task 3', 'Failed');
