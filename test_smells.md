## Test smells en tests generados por libería pynguin
Los tests generados por _pynguin_ tienen los siguientes test smell:
* _Eager test_: En la mayoría de los tests ocurre que se testean dos o más métodos dentro de un método de test lo cual dificulta documentar lo que se está testeando. Además, los test no cuentan con nombres representativos, por lo que identificar qué se testea se vuelve aún más difícil.
* _Lazy test_: En los tests case 1, 4, 5 y 6 del módulo _test\_src\_clock\_display.py_ se usa el mismo fixture (el mismo binario) para realizar el test.
* _Assertion Roulete_: Si ejecutamos los test generados con _pytest_, podemos ver que no tenemos cómo saber que tests fallaron y cuales pasaron correctamente, mucho menos saber en qué fallaron.