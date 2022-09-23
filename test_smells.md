### Test smells en tests generados por libería pynguin:

Los tests generados por pynguin tienen los siguientes test smell:
- Eager test: En la mayoría de los tests ocurre que se testean dos o más métodos dentro de un método de test lo cual dificulta documentar lo que se está testeando. Además, los test no cuentan con nombres representativos, por lo que identificar qué se testea se vuelve aún más difícil.
- Lazy test: En los tests case 1, 4, 5 y 6 del módulo test\_src\_clock\_display.py se usa el mismo fixture (el mismo binario) para realizar el test.
- Assertion Roulete: Si ejecutamos los test generados con pytest, podemos ver que no tenemos cómo saber que tests fallaron y cuales pasaron correctamente, mucho menos saber en qué fallaron.