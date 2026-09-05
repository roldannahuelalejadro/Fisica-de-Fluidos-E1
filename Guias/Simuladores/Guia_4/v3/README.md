# Guia 4 v3 - Viscosidad visual

App local para estudiar soluciones analiticas de la Guia 4 con escenas tipo laboratorio.

## Como abrir

Abrir `index.html` con doble click en un navegador moderno.

Si hay conexion a internet, MathJax renderiza las ecuaciones del panel derecho en formato LaTeX.

## Que cambia respecto de v2

- Los problemas se muestran con geometria: placas, pelicula inclinada, tubo, cilindros coaxiales y esfera.
- Hay trazadores/particulas moviendose segun el perfil analitico.
- Se puede mover la escena arrastrando el canvas y hacer zoom con la rueda del mouse.
- El modulo Taylor-Couette muestra contornos de `|v_theta|` sobre el cilindro, oclusion simple del cilindro interno y celdas cualitativas si el criterio de Rayleigh indica inestabilidad.
- El panel derecho muestra cuentas paso a paso con ecuaciones en LaTeX.

## Controles

- Arrastrar sobre la escena: pan.
- Rueda del mouse: zoom.
- Boton `vista`: vuelve al encuadre inicial.
- Boton `reset`: vuelve a los parametros iniciales del problema activo.

## Modulos

- P1: Couette-Poiseuille entre placas.
- P2: pelicula viscosa sobre plano inclinado.
- P4: Poiseuille cilindrico.
- P6(iv): Taylor-Couette laminar y estabilidad cualitativa.
- P7: esfera, Reynolds y arrastre dimensional.

La app no resuelve Navier-Stokes numericamente. Visualiza soluciones analiticas y escalas de la guia.
