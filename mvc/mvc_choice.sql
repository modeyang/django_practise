
create table "mvc_choice" (
	"id" integer NOT NULL PRIMARY KEY,
	"book_id" integer NOT NULL references "mvc_book" ("id"),
	"choice" varchar(20) NOT NULL,
	"votes" integer NOT NULL
);

