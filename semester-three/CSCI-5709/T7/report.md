# Tutorial 7
Individual Submission

* *Date Created*: 09 Jun 2022
* *Last Modification Date*: 12 Jun 2022
* *Git URL Repository*: <https://git.cs.dal.ca/adimurthy/5709-tutorials>
* *Git URL Assignment*: <https://git.cs.dal.ca/adimurthy/5709-tutorials/-/tree/master/tutorial-7>
* *Deployed Application*: <https://tutorial-7-5709.herokuapp.com>

## Author
* [Adesh Nalpet Adimurthy](adesh.nalpet@dal.ca) - *(NodeJS Application Development)*

## Overview
A NodeJS application to add, update and get all users or an individual user.

## Getting Started

## Installing
### Local Set-up
- Start Client: `npm install && npm run start`

## Project Structure: 
- [Camel Case](https://www.upbeatcode.com/react/react-naming-conventions/) Naming convention
### Server-side (NodeJS)
Since the application solves for the small use case:
- controllers: The logic to handle an API request.
- models: Schema(s) used in the application.
- config: MongoDB database and env configuration file.
- router: List of all the routes in the application
- server: To start and force redirect the application to HTTPS.

## Deployment
### Heroku Set-up
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Login and Create a project: `heroku login` and `heroku create <unique-project-name>`
- Deploy: `git push heroku master`

## Built With

* [NodeJS](https://nodejs.org/en/) + [Express](https://expressjs.com/)

## Sources Used

### File: server.js
```
app.use('/', useRouter);

const port = process.env.PORT || 5000;

app.use((req, res, next) => {
  if (req.header('x-forwarded-proto') !== 'https' && process.env.NODE_ENV == "production") {
    res.redirect(`https://${req.header('host')}${req.url}`)
  }
  next();
});
```

The above code snipped is from Assignment 1/2 (Project).
- The parts of code in `server.js` was implemented by `Adesh Nalpet Adimurthy` (Self Attribution).
- `server.js`'s Code was used because I had a similar use case and re-using server starting and redirection was evident.
- `server.js`'s Code was further modified to remove unnecessary dependencies.

### File: router.js

```
const express = require("express");
const router = express.Router();

const {
  getProducts,
  getProductById,
  addProduct,
  getProductsByCategory,
} = require("../controllers/product-controller");

router.get("/products/get-products", getProducts);
router.get("/products/get-products/:categoryName", getProductsByCategory);
router.get("/products/get-product/:id", getProductById);
router.post("/products/add-product", addProduct);

module.exports = router;

```

- The parts of code in `router.js` was implemented by `Adesh Nalpet Adimurthy (Self Attribution)` for assignment 1/2.
- `router.js`'s Code was used because I had previously written a similar controller for CRUD operations for products.
- `router.js`'s Code was modified to perform get/add and update operations on user object instead of product.

### File: db-connection.js

```
const mongoose = require("mongoose");
require("dotenv").config({ path: "./.env" });
const _DBUrl = process.env.DB;

mongoose
    .connect(_DBUrl, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    })
    .then(() => console.log("Connection Successful"))
    .catch((err) => console.log(`Error : ${err}`));
```

- The parts of code in `db-connection.js` was implemented by `Adesh Nalpet Adimurthy (Self Attribution)` for assignment 3 and project.
- `db-connection.js`'s Code was used because I had previously written a similar database connection file to connect to MongoDB.
- `db-connection.js`'s Code was not modified and used as is.


## References
```
[1] Node.js Foundation, “Node.js,” Node.js, 2019. https://nodejs.org/en/ (accessed July. 10, 2022).

[2] A. N. Adimurthy, “PyCommerce,” GitLab. https://git.cs.dal.ca/adimurthy/5709-tutorials/-/tree/master/assignment-1 (accessed Jun. 02, 2022).

[3] Pyblog, “pyblog.xyz“, 2021. https://pyblog.xyz (accessed July. 09, 2022).
‌
```
‌