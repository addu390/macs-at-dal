# PyCommerce

Project Proposal - Group Submission

- _Date Created_: 10 July 2022
- _Last Modification Date_: 13 July 2022
- _Git URL Repository_: <https://git.cs.dal.ca/adimurthy/csci-5709-group-16>
- _Deployed Application_: <https://pycommerce-16.herokuapp.com/>

## Author

- Adesh Nalpet Adimurthy - Full Stack Development

## Overview

The eCommerce application is built on the MERN stack. The client is a react application and heavily uses the Material UI component library. The server is a NodeJS + Express application with MongoDB as the NoSQL data store with mongoose to quickly model; the backend is for CRUD operations on all the models. 

## My Features

Both **Favorites/Wishlist** and **products dashboard** including **search operation** is completed (Frontend and Backend).

## My Files

The files that I have Authored are as follows:

### Backend

- `config/db-connection.js`
- `models/favorites-model.js`
- `models/product-model.js`
- `controllers/favorites-controller.js`
- `controllers/product-controller.js`
- `routes/router.js`
- `.env.example`

### Frontend

Action Types:
- `client/src/action-type/favorites-action-type.js`
- `client/src/action-type/product-action-type.js`

Actions:
- `client/src/actions/favorites-action.js`
- `client/src/actions/product-action.js`

Adapters:
- `client/src/adapters/firebase.js`

Feature Components:
- `client/src/components/favorites/favorites-list.js`
- `client/src/components/favorites/favorites.js`
- `client/src/components/product/image-slider.js`
- `client/src/components/product/product-details.js`
- `client/src/components/product/product-grid.js`
- `client/src/components/product/product-list.js`

Other Components:
- `client/src/components/footer/footer.js`
- `client/src/components/header/header.js`
- `client/src/components/navbar.js`
- `client/src/components/toast.js`

Constants:
- `client/src/constants/data.js`

Pages:
- `client/src/pages/home-page.js`
- `client/src/pages/product-details-page.js`
- `client/src/pages/products-page.js`
- `client/src/pages/favorites-page.js`
- `client/src/pages/error-page.js`

Reducers:
- `client/src/reducers/favorites-reducer.js`
- `client/src/reducers/product-reducer.js`

Styles:
- `client/src/styles/home-page.css`
- `client/src/styles/product-page.css`
- `client/src/styles/product-page.css`
- `client/src/app.css`
- `client/src/app.css`

Utils:
- `client/src/utils/string-util.js`
- `client/src/utils/toast-message.js`
- `client/src/templates/template-provider.js`

## Getting Started

## Prerequisites

- Local MongoDB set-up or Atlas (MongoDB):
  - Create an [Atlas Account](https://www.mongodb.com/docs/atlas/getting-started/)
  - Choose free tier plan and create a shared cluster.
  - Copy of Host with username and password.

## Installing

### Local Set-up

- Add mongoDB configuration to a `.env` file. Refer to `.env.example` for the the content of `.env` (to initialize mongoose at `config/db-connection.js`)
- Start Server: `npm install && npm run start`
- Start Client: `cd client` & `npm install && npm run start`

## Schema

- `favorites`: contains the mapping of `user-id` and `product-id`
- `products`: contains all the product details such as `title`, `description`, `price`, `discount`, `rating`, `image-url` and many more.


## Project Structure:

- [Kebab Case](https://www.upbeatcode.com/react/react-naming-conventions/) Naming convention

### Client-side (React)

- **components**: individual standalone, reusable sections of the application.
- **action-type**: Represents the different operations performed in a component. For example: the favorites component has operations such as "getFavorites", "addToFavorites" and "removeFromFavorites"
- **actions**: the implementation of action-type, uses axios to make API calls to the backend to perform the action-types.
- **constants**: hard coded static content segregated together in one place for easier access.
- **pages**: Individual pages of the application, each page is usually a combination of different components. Example: Home page and Favorites page.
- **reducers**: an abstraction for state management and receives input of the current/initiate state and the action as the input and returns the new state.
- **styles**: css files for pages.
- **utils**: static generic functions.

### Backend (NodeJS)

- **routes**: List of APIs with path and the controller to visit to process a request.
- **controller**: The business logic layer with dependency on the service layer to perform the necessary actions.
- **models**: Schema of database models stored in MongoDB.
- **logs**: path to store application logs (rolling logs).

## Deployment

### Heroku Set-up

- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Login and Create a project: `heroku login` and `heroku create <unique-project-name>`
- Add atlas (mongoDB) env variables: Project → Settings → Config Vars
- Deploy: `git push heroku master`

## Image Sizes

- Category Icon: `128 x 128`
- Banner (Top Slider): `1000 x 165`
- Ad Banner: `1000 x 85`
- Product: `500 x 540`
- Featured Brands: `1000 x 540`
- Poster Slider: `1000 x 615`

## Built With

- [React](https://reactjs.org/) - A JavaScript library for building user interfaces
- [Material UI](https://mui.com/) - A comprehensive suite of UI tools and production-ready components
- [NodeJS](https://nodejs.org/en/) - A JavaScript runtime built on Chrome's V8 JavaScript engine
- [Express](https://expressjs.com/) - Fast, unopinionated, minimalist web framework for Node.js
- [MongoDB](https://www.mongodb.com/) - A source-available cross-platform document-oriented database

## Sources Used

### File: featured.js

```
<Carousel
          swipeable={true}
          draggable={false}
          showDots={false}
          responsive={responsive}
          ssr={true}
          infinite={true}
          autoPlay={true}
          autoPlaySpeed={2500}
          keyBoardControl={true}
          customTransition="all 200ms"
          transitionDuration={500}
          containerClass="carousel-container"
          removeArrowOnDeviceType={["mobile"]}
          dotListClass="custom-dot-list-style"
          itemClass="carousel-item-padding-40-px"
        >
```

While it was not a direct code reference that was modified, the prime reference was from [react-multi-carousel](https://github.com/YIZHUANG/react-multi-carousel/blob/master/examples/ssr/pages/index.js). Which is also the library I used for carousel(s) in the entire application.

- The parts of code in `featured.js` was implemented by `react-multi-carousel` (examples in official documentation).
- `featured.js`'s Code was used because I had a simple use case and the example in the documentation had just what I needed
- `featured.js`'s Code was modified to add additional parameters and CSS classes such as `carousel-container`.

### File: error-page.js

- Self Attribution
- Created by Adesh Nalpet Adimurthy previously for the blog [https://pyblog.xyz](https://pyblog.xyz)

```
<div
      style={{
        textAlign: "center",
        fontSize: "14px",
        padding: "20px",
        marginTop: "100px",
      }}
    >
      <div>
        <img
          style={{ width: "450px", maxWidth: "100%" }}
          src="/images/404.png"
          alt=""
        />
        <div
          style={{
            fontSize: "1.3em",
            paddingTop: "10px",
            marginBottom: "35px",
          }}
        >
          Unfortunately the page you are looking for has been moved or deleted
        </div>
        <Button
          style={{ backgroundColor: "#222" }}
          variant="contained"
          color="primary"
        >
          <Link to="/">GO TO HOMEPAGE</Link>
        </Button>
      </div>
    </div>
```

- The parts of code in `error-page.js` was implemented by `Adesh Nalpet Adimurthy (Self Attribution)`.
- `error-page.js`'s Code was used because I had previously written a generic simple 404 page for an other react website.
- `error-page.js`'s Code was modified to add additional CSS for design consistency and the image(s).

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


### Folder: images

- Self Attribution
- Created using [ProCreate](https://procreate.art/) by Adesh Nalpet Adimurthy


## References

```
[1] “React Best Practices and Security,” TatvaSoft Blog. https://www.tatvasoft.com/blog/reactjs-best-practices/ (accessed Jun. 04, 2022).

[2] W3C, “The W3C Markup Validation Service,” W3.org, 2013. https://validator.w3.org/ (accessed Jun. 04, 2022)

[3] “MUI: The React component library you always wanted,” mui.com. https://mui.com/ (accessed May. 30, 2022).

[4] Node.js Foundation, “Node.js,” Node.js, 2019. https://nodejs.org/en/ (accessed May. 30, 2022).
‌
[5] MongoDB, “The most popular database for modern apps,” MongoDB, 2019. https://www.mongodb.com/ (accessed May. 30, 2022).
‌
[6] Facebook, “React – A JavaScript library for building user interfaces,” Reactjs.org, 2022. https://reactjs.org/ (accessed May. 30, 2022).

[7] Pyblog, “pyblog.xyz“, 2021. https://pyblog.xyz (accessed Jun. 01, 2022).

````
