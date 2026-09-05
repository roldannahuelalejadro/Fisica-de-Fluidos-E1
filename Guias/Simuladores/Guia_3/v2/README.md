# Simulador Guia 3 - Flujos ideales

App web local para explorar la Practica 3 de Fisica de Fluidos.

## Como abrir

Abrir `index.html` con doble click en un navegador moderno.

## Que permite hacer

- Cargar presets de la guia: flujos singulares, imagenes con paredes, codo recto, cilindro y modelo fuente-sumidero con circulacion.
- Agregar fuentes, sumideros, vortices, dipolos, corrientes uniformes, cilindros y paredes.
- Arrastrar singularidades directamente en el plano complejo.
- Ver lineas de corriente, particulas advectadas en el campo y flechas de velocidad.
- Ver el campo de presion en todo el plano con una escala fija y una paleta Viridis suavizada.
- Editar parametros desde el inspector con controles numericos y sliders: posicion, caudal, circulacion, intensidad, angulo, radio, distancia del dipolo, densidad y escala de presion.
- Ajustar `P minimo`, `P maximo` y la unidad de la barra de colores. El zoom no cambia la escala de presion.
- Ver puntos de estancamiento aproximados, fuerza sobre cilindros y una grafica de `Cp(theta)` cuando hay un cilindro.
- Cargar el preset del Problema 6 con cilindro, circulacion atrapada, dipolo externo e imagen por el teorema del circulo.
- Agregar un potencial complejo personalizado y elegir si la entrada es `W(z)` o `dW/dz`.
- Regularizar singularidades de expresiones personalizadas con `xi`, que suaviza divisiones y logaritmos cerca de polos.

## Potenciales personalizados

Agregar con el boton `W`.

Variables disponibles:

- `z`: coordenada compleja global.
- `zc`: coordenada local respecto del marcador del objeto, `z - (x + i y)`.
- `i`, `pi`, `xi`.
- Cualquier otro nombre se vuelve parametro con slider, por ejemplo `U`, `a`, `Gamma`, `Q`, `x0`, `y0`.

Funciones disponibles:

`log`, `ln`, `exp`, `sqrt`, `sin`, `cos`, `tan`, `conj`, `abs`, `arg`, `re`, `im`, `pow`, `cis`.

Ejemplos:

```text
dW/dz: U*(1-a^2/z^2)-i*Gamma/(2*pi*z)
W(z):  U*(z+a^2/z)-i*Gamma/(2*pi)*log(z)
dW/dz: Q/(2*pi*(z-(x0+i*y0)))
```

Usar `*` para multiplicar: escribir `2*pi`, no `2pi`.

## Controles

- Rueda del mouse: zoom.
- Arrastrar fondo: mover la vista.
- Arrastrar objeto: cambiar coordenadas.
- Boton `II` / `▶`: pausa o reproduce la animacion.
- Boton `↻`: reinicia particulas.
- Boton `{}`: copia la escena actual como JSON.
- Boton `auto escala escena`: recalcula una escala de presion usando la configuracion completa, no el zoom actual.

El simulador es cualitativo y didactico. Las singularidades puntuales se suavizan cerca del centro para que la animacion no se rompa numericamente.
