# Guia 4 v4 - Simulador 3D

Version WebGL del simulador de fluidos viscosos de la Guia 4.

## Como abrir

Abrir `index.html` con doble click en un navegador moderno.

La escena usa Three.js local en `vendor/`, por eso no necesita servidor. Las ecuaciones se renderizan con MathJax desde CDN cuando hay conexion a internet.

## Que cambia respecto de v3

- La escena ya no es una proyeccion 2D en canvas: ahora usa WebGL y controles de orbita reales.
- Las particulas tienen profundidad de escena, asi que el cilindro interno de Taylor-Couette oculta lo que queda detras.
- Flechas, particulas y perfil lateral se calculan desde las mismas funciones analiticas.
- Taylor-Couette muestra contornos suaves de `|v|` con una paleta secuencial menos dura que viridis puro.
- P7 usa lineas de corriente 3D alrededor de la esfera en vez de lineas decorativas planas.
- Las placas, cilindros y discos moviles tienen marcadores animados para que se vea la condicion de contorno.
- Cada escena tiene un inset de perfil dentro de la figura, ademas del panel derecho.
- P5 muestra tres conductos comparativos y barras de caudal para visualizar la ley `Q ~ a^4`.
- Cada problema conserva el panel de cuentas en LaTeX.

## Modulos

- P1: Couette-Poiseuille entre placas.
- P2: pelicula viscosa sobre plano inclinado.
- P3: dos fluidos estratificados sobre plano inclinado.
- P4: Poiseuille cilindrico.
- P5: escala dimensional de Poiseuille.
- P6(i)-(iv): configuraciones de placas, plano inclinado, anillo axial y Taylor-Couette.
- P7: arrastre sobre una esfera y numero de Reynolds.
- P8: primer problema de Stokes.
- P9: vortice viscoso.
- P10: placa oscilante.
- P11: canal finito impulsivo.
- P12: capa limite de Blasius.
- P13: placa giratoria.
