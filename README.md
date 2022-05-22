# Ejercicio Técnico

Se tienen dos logs con datos en el siguiente formato, con valores separados por el carácter ```;```.


```
A;42.3;1653062446;001
A;41.3;1653062447;001
A;40.4;1653062448;002
B;43.3;1653062450;001
```

## Objetivo

Generar un script que una los dos archivos y los ordene según los datos de la tercera columna.

## Como ejecutar

```
python3 ejercicio.py archivo_logs archivo_logs2
```

### Resultado

Un archivo llamado ```logs_ordenados```, ordenados según los datos de la tercera columna.