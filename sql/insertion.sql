INSERT INTO library.users VALUES (1, "JAKE", "MASON", 5732025625);
INSERT INTO library.users VALUES (2, "JOHN", "DOE", 5554206969);
INSERT INTO library.authors VALUES (1, "CL", "RS");
INSERT INTO library.authors VALUES (2, "DOCTOR", "SEUSS");
INSERT INTO library.books VALUES (9780262046305, 1, 1990, 3, "Aisle 2", "Algorithms");
INSERT INTO library.books VALUES (0400307299532, 2, 1957, 3, "Asile 1", "Cat in the Hat");
INSERT INTO library.books VALUES (9780007355914, 2, 1960, 3, "Asile 1", "Green Eggs and Ham");
INSERT INTO library.computers VALUES (1, "2nd Floor");
INSERT INTO library.computers VALUES (2, "2nd Floor");
INSERT INTO library.computers VALUES (3, "1st Floor");
INSERT INTO library.rooms VALUES (100, 1);
INSERT INTO library.rooms VALUES (101, 1);
INSERT INTO library.rooms VALUES (200, 2);
INSERT INTO library.rooms VALUES (201, 2);
INSERT INTO library.familymembers VALUES (5732222222, 2);

SELECT * FROM library.books;
SELECT * FROM library.authors;