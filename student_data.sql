-- refer to https://www.sjkjc.com/postgresql/join/#google_vignette
-- create 2 tables
CREATE TABLE student (
  student_id INTEGER NOT NULL,
  name varchar(45) NOT NULL,
  PRIMARY KEY (student_id)
);

CREATE TABLE student_score (
  student_id INTEGER NOT NULL,
  subject varchar(45) NOT NULL,
  score INTEGER NOT NULL
);

-- insert some data
INSERT INTO
  student (student_id, name)
VALUES
  (1,'Tim'),(2,'Jim'),(3,'Lucy');

INSERT INTO
  student_score (student_id, subject, score)
VALUES
  (1,'English',90),
  (1,'Math',80),
  (2,'English',85),
  (5,'English',92);
