Matplotlib Architecture:
- Three main layers:
    - The back-end layers has three builtin abstract interface classes:
      - FirgureCanvas: encompasses the area onto which the figure is drawn
      - Renderer: knows how to draw on the FigureCanvas
      - Event: hanldes user inputs
    - The artist layer: knows how to use the Renderer to draw on the canvas. Title, lines, tick labels, and images, all correspond to individual Artist instances. Two types of Artist objects:
      - Primitive: line2d, rectangle, circle and text.
      - Composite: tick, axes, axis and figure.
    - The scripting layer: it was developed for scientists