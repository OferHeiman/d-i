1:

SELECT

   COUNT(*)

FROM

   actors;


2:

If i try to add a new actor with a blank field i think i will get an error that a field is missing.

INSERT INTO actors (first_name, last_name, age, number_oscars)

VALUES('Leonardo','Dicaprio','11/11/1974');

result:

ERROR:  INSERT has more target columns than expressions

LINE 1: INSERT INTO actors (first_name, last_name, age, number_oscar...

                                                        ^
SQL state: 42601

Character: 49

