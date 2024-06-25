CREATE TABLE IF NOT EXISTS  book(
    id SERIAL PRIMARY KEY UNIQUE,
    title VARCHAR(50),
    author VARCHAR(20),
    publication_year INTEGER
);

CREATE TABLE IF NOT EXISTS "user"(
    id SERIAL PRIMARY KEY UNIQUE,
    full_name varchar(50)
);

CREATE TABLE IF NOT EXISTS borrows_history(
    id SERIAL PRIMARY KEY UNIQUE,
    book_id INTEGER REFERENCES book(id),
    user_id INTEGER REFERENCES "user"(id),
    borrow_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "user"(full_name) 
VALUES 
('Ivan Ivanov'),
('Nikolay Niloayev'),
('Mykola Mykolovych'),
('Alexandr Alexandrov');

 INSERT INTO book (title, author, publication_year)
 VALUES
 ('Harry Potter', 'Jhoan Roaling', 2003),
 ('Lord of The Ring', 'Tolkin', 1941);

INSERT INTO borrows_history (book_id, user_id)
VALUES
    (1, 3),
    (3, 1),
    (2, 2),
    (3, 2),
    (2, 4);

SELECT * FROM "user"
WHERE id IN 
(SELECT user_id FROM borrows_history);

BEGIN TRANSACTION;

DELETE  FROM book;
COMMIT;
BEGIN TRANSACTION;

DELETE  FROM "user";
COMMIT;

BEGIN TRANSACTION;

DELETE FROM borrows_history
WHERE user_id IN (SELECT id FROM "user");
COMMIT;
BEGIN TRANSACTION;

DELETE  FROM borrows_history;
COMMIT;