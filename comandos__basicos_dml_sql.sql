/* seleccionar todos los registros de una tabla se puede utilizar el where dentro*/
/*SELECT * FROM movement WHERE quantity<0;*/
/*seleccionar algunos campos de una tabla de base de datos*/
/*SELECT concept,quantity FROM movement;
SELECT * FROM movement;*/
/* Para insertar nuevos registros en la tabla movement*/
/*INSERT INTO movement (date, concept, quantity) VALUES ("2025-09-05", "mercado", -250); */
/* comando para actualizar registros de la tabla movement, siempre usar el where en update
UPDATE movement SET concept = "almuerzo", quantity = -50 WHERE id=2; */
/*comando para borrar registros, importante utilizar el where siempre que se quiera borrar un registro especifico
DELETE FROM movement WHERE id=3;*/
SELECT * FROM movement ORDER BY id DESC;