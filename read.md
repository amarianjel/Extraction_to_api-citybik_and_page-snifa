# Tabla de Contenidos

- [Proyecto Django](#proyecto-django)
- [Tarea 1](#tarea-1)
- [Tarea 2](#tarea-2)
- [Librerias adicionales](#librerias-adicionales)
- [Crear el entorno virtual](#crear-el-entorno-virtual)
- [Instalar DJANGO](#instalar-django)
- [Aplicaciones](#aplicaciones)
- [BDD PostgreSQL](#bdd-postgresql)
- [Eliminar venv y restaurar](#eliminar-venv-y-restaurar)

## Proyecto Django

<!-- Contenido de la sección "Proyecto Django" -->
fdsafsdaf

# [React](https://reactjs.org/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/main/LICENSE) [![npm version](https://img.shields.io/npm/v/react.svg?style=flat)](https://www.npmjs.com/package/react) [![CircleCI Status](https://circleci.com/gh/facebook/react.svg?style=shield)](https://circleci.com/gh/facebook/react) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://reactjs.org/docs/how-to-contribute.html#your-first-pull-request)

[Learn how to use React in your project](https://reactjs.org/docs/getting-started.html).





We have several examples [on the website](https://reactjs.org/). Here is the first one to get you started:

```jsx
import { createRoot } from 'react-dom/client';

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = createRoot(document.getElementById('container'));
root.render(<HelloMessage name="Taylor" />);
```

This example will render "Hello Taylor" into a container on the page.

You'll notice that we used an HTML-like syntax; [we call it JSX](https://reactjs.org/docs/introducing-jsx.html). JSX is not required to use React, but it makes code more readable, and writing it feels like writing HTML. If you're using React as a `<script>` tag, read [this section](https://reactjs.org/docs/add-react-to-a-website.html#optional-try-react-with-jsx) on integrating JSX; otherwise, the [recommended JavaScript toolchains](https://reactjs.org/docs/create-a-new-react-app.html) handle it automatically.


The following examples show how one might use `file-loader` and what the result would be.

**file.js**

```js
import png from './image.png';
```

**webpack.config.js**

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: 'dirname/[contenthash].[ext]',
            },
          },
        ],
      },
    ],
  },
};
```

Result:

```bash
# result
dirname/0dcbbaa701328ae351f.png
```






## Tarea 1

<!-- Contenido de la sección "Tarea 1" -->

## Tarea 2

<!-- Contenido de la sección "Tarea 2" -->

## Librerias adicionales

<!-- Contenido de la sección "Librerias adicionales" -->

## Crear el entorno virtual










dfsf
<!-- Contenido de la sección "Crear el entorno virtual" -->

## Instalar DJANGO

<!-- Contenido de la sección "Instalar DJANGO" -->

## Aplicaciones

<!-- Contenido de la sección "Aplicaciones" -->

## BDD PostgreSQL

<!-- Contenido de la sección "BDD PostgreSQL" -->

## Eliminar venv y restaurar

<!-- Contenido de la sección "Eliminar venv y restaurar" -->

