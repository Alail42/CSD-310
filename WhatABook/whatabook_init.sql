DROP DATABASE IF EXISTS 'whatabook';

CREATE DATABASE 'whatabook';

USE 'whatabook';

DROP USER IF EXISTS 'whatabook_user'@'localhost';


CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Admin123';


GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';


ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;


DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('1313 Mockingbird Lane, Bristol County, Gotham City, 42052');


INSERT INTO book(book_name, author, details)
    VALUES('The Call of Cthulhu', 'H. P. Lovecraft', 'Lovecrafts most famous and terrifying work');

INSERT INTO book(book_name, author, details)
    VALUES('The Colour Out of Space', 'H. P. Lovecraft', 'A story that will leave you quacking to the end');
INSERT INTO book(book_name, author, details)
    VALUES('Arthur Jermyn', 'H. P. Lovecraft', "an ugly story about an ugly man");

INSERT INTO book(book_name, author)
    VALUES('The Descendant', 'H. P. Lovecraft');

INSERT INTO book(book_name, author)
    VALUES('Dagon', 'H. P. Lovecraft');

INSERT INTO book(book_name, author)
    VALUES("Sarnath", 'H. P. Lovecraft');

INSERT INTO book(book_name, author)
    VALUES('1984', 'George Orwell');

INSERT INTO book(book_name, author)
    VALUES('Fahrenheit 451', ' Ray Bradbury');

INSERT INTO book(book_name, author)
    VALUES('Through the looking glass and What Alice Found There', 'Lewis Carroll');

INSERT INTO user(first_name, last_name) 
    VALUES('Richard', 'Grayson');

INSERT INTO user(first_name, last_name)
    VALUES('Jason', 'Todd');

INSERT INTO user(first_name, last_name)
    VALUES('Tim', 'Drake');


INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Richard'), 
        (SELECT book_id FROM book WHERE book_name = '1984')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Tim'),
        (SELECT book_id FROM book WHERE book_name = 'The Colour Out of Space')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jason'),
        (SELECT book_id FROM book WHERE book_name = 'Dagon')
    );
