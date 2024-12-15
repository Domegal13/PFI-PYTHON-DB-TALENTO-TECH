<h1 align="center"> Proyecto Codo a Codo - NodeJS </h1>

---

# API REST de Plantas 🏁

Esta es una API REST para gestionar información sobre plantas. La API permite crear, leer, actualizar y eliminar registros de plantas.

---

![Static Badge](https://img.shields.io/badge/version-1.0.0-blue)
🚧![Static Badge](https://img.shields.io/badge/En%20Construcci%C3%B3n-ff0000)🚧

## Requisitos 🛠️

![Node.js](https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?logo=express&logoColor=white)
![Sequelize](https://img.shields.io/badge/Sequelize-purple?logo=sequelize&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)
![Nodemon](https://img.shields.io/badge/Nodemon-76D04B?logo=nodemon&logoColor=black)

---

## Descripción General 🚀

La API REST de Plantas proporciona los siguientes endpoints:

- `GET /plantas` - Obtiene una lista de todas las plantas.
- `GET /plantas/{id}` - Obtiene los detalles de una planta específica por ID.
- `POST /plantas` - Crea una nueva planta.
- `PUT /plantas/{id}` - Actualiza una planta existente por ID.
- `DELETE /plantas/{id}` - Elimina una planta por ID.

---

## Instalación 🔧

1. Clone el repositorio:

   ```sh
   git clone https://github.com/Domegal13/PFI-PYTHON-DB-TALENTO-TECH.git
   ```

2. Navega al directorio del proyecto:

   `cd Proyecto-PFI-PYTHON-DB`

3. Cree un entorno virtual (opcional):

    `python -m venv 'Nombre_del_entorno_virtual'`

    3.1. Active el entorno virtual:

    `Nombre_del_entorno_virtual/Scripts/activate`

4. Instala las dependencias:

   `pip install -r requirements.txt`

4. Configure la base de datos en el archivo .env.

```JavaScript
const mysql = {
  PORT: process.env.PORT,
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  DB_PORT: process.env.DB_PORT,
};
```

---

## Uso 📄

1. Inicie el servidor
   `npm run dev`

2. Para realizar las pruebas puede utilizar cualquier herramienta como:

- Insomnia.
- Postman.
- Thunder Client.
- etc.

---

## Endpoints 🚦

### 1. Obtener todas las plantas

- #### URL: `/api/v1/plantas`
- #### Método: `GET`

![GET](./src/assets/images/traer-todos-los-registros.png)

### 2. Obtener una planta por ID

- #### URL: `/api/v1/plantas/{id}`
- #### Método: `GET`

![GET](./src/assets/images/traer-registro-por-id.png)

### 3. Crear una nueva Planta

- #### URL: `/api/v1/plantas/`
- #### Método: `POST`

![POST](./src/assets/images/crear-registro-planta.png)

### 2. Actualizar planta por ID

- #### URL: `/api/v1/plantas/{id}`
- #### Método: `PUT`

![PUT](./src/assets/images/actualizar-registro-planta.png)

### 2. Eliminar una planta por ID

- #### URL: `/api/v1/plantas/{id}`
- #### Método: `DELETE`

![DELETE](./src/assets/images/eliminar-registro-planta.png)

---

## Autores ✒️

| <h3 align="center">Nombre</h3>                                                                                                                                                                                                                                                                                    | <h3 align="center">GitHub</h3>                                                                                                             | <h3 align="center">Linkedin</h3>                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [<img src="https://avatars.githubusercontent.com/u/105987399?v=4" width="30"  style="border-radius: 30px;" align="center">](https://github.com/Domegal13) **_Doménico Gallo García_**                                                                                                                             | [<img alt="Static Badge" src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white">](https://github.com/Domegal13)      | [<img alt="Static Badge" src="https://img.shields.io/badge/Linkedin-0A66C2?logo=Linkedin&logoColor=white">](https://www.linkedin.com/in/domegal13/)                                                                                                  |
| [<img src="https://media.licdn.com/dms/image/C4D03AQFpLcw7xmhOSQ/profile-displayphoto-shrink_200_200/0/1603458892263?e=1726099200&v=beta&t=1PRM9ReuAZro5lxMhYToGCAIeAR3AtNloNAKIEoabiE" width="30"  style="border-radius: 30px;" align="center" >](https://github.com/guadasalgado) **_Guadalupe Luján Salgado_** | [<img alt="Static Badge" src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white">](https://github.com/guadasalgado)   | [<img alt="Static Badge" src="https://img.shields.io/badge/Linkedin-0A66C2?logo=Linkedin&logoColor=white">](https://www.linkedin.com/in/guadasalgado/)                                                                                               |
| [<img src="https://avatars.githubusercontent.com/u/94230956?v=4" width="30"  style="border-radius: 30px;" align="center" >](https://github.com/agus0914) **_Agustin Peréz_**                                                                                                                                      | [<img alt="Static Badge" src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white">](https://github.com/agus0914)       | [<img alt="Static Badge" src="https://img.shields.io/badge/Linkedin-0A66C2?logo=Linkedin&logoColor=white">](https://www.linkedin.com/in/agustin-perez-a44569267/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) |
| [<img src="https://avatars.githubusercontent.com/u/161794715?v=4" width="30"  style="border-radius: 30px;" align="center" >](https://github.com/MarinaCorbalan) **_Marina Corbalan_**                                                                                                                             | [<img alt="Static Badge" src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white">](https://github.com/MarinaCorbalan) | [<img alt="Static Badge" src="https://img.shields.io/badge/Linkedin-0A66C2?logo=Linkedin&logoColor=white">]()                                                                                                                                        |

---

## Agradecimientos 🎉

**_Queremos expresar nuestro agradecimiento especial a:_**

**_Prof. Gabriel Muñoz:_** Por su guía, dedicación, asesoramiento y enseñanza en estos meses que han sido fundamentales para llevar a cabo este proyecto.

**_Codo a Codo:_** Por permitirnos ser parte de esta gran comunidad.