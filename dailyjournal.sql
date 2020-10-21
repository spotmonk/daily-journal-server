INSERT INTO 'Mood' VALUES (null, 'Happy');
INSERT INTO 'Mood' VALUES (null, 'Sad');
INSERT INTO 'Mood' VALUES (null, 'Angry');
INSERT INTO 'Mood' VALUES (null, 'Ok');

INSERT INTO 'Entries' values (null, '1235', "123", 1598458543321, 1);
INSERT INTO 'Entries' values (null, 'abc', "123", 1598458548239, 2);
INSERT INTO 'Entries' values (null, 'delete', "now deleting", 1598458559152, 1);
INSERT INTO 'Entries' values (null, 'angry', "jlj", 1598557358781, 3);
INSERT INTO 'Entries' values (null, '678', "Now Deleting", 1598557373697, 4);


ALTER TABLE Entries
RENAME COLUMN mood_id TO moodId;
