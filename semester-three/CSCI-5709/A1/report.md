# Assignment 1
Individual Submission
![Heroku](https://pyheroku-badge.herokuapp.com/?app=assignment-1-5709&style=flat-square)

* *Date Created*: 05 Jun 2022
* *Last Modification Date*: 05 Jun 2022
* *Git URL Repository*: <https://git.cs.dal.ca/adimurthy/5709-tutorials>
* *Git URL Assignment*: <https://git.cs.dal.ca/adimurthy/5709-tutorials/-/tree/master/assignment-1>
* *Deployed Application*: <https://assignment-1-5709.herokuapp.com>

## Author
* [Adesh Nalpet Adimurthy](adesh.nalpet@dal.ca) - *(Full Stack Development)*

## Overview
The application is built on the MERN stack. The client is a react application and heavily uses the Material UI component library. The server is a NodeJS + Express application with MongoDB as the NoSQL data store with mongoose to quickly model and maintain the application schema. For this assignment, there are two models, `favorites` and `products`; the backend is for CRUD operations on these two models. On the other hand, the majority of the work on the client-side was on designing the home page, product page, and functionality to add products to the wishlist. Ideally, most of the data is either configurable or dynamically loaded by calling the backend APIs. For early prototyping, the products and adding products to the wishlist are dynamic. However, the banner, offers, deals, and featured brands on the home page are static.

## Getting Started
## Prerequisites
- Local MongoDB set-up or Atlas (MongoDB):
    - Create an [Atlas Account](https://www.mongodb.com/docs/atlas/getting-started/)
    - Choose free tier plan and create a shared cluster.
    - Copy of Host with username and password.

## Installaing
### Local Set-up
- Add mongoDB configuration to a `.env` file. Refer to `.env.example` for the the content of `.env` (to initialize mongoose at `config/db-connection.js`)
- Start Server: `npm install && npm run start`
- Start Client: `cd client` & `npm install && npm run start`

## Schema
- For the sake of demonstration, the application does not have login/register workflow.
- The only models used are: `Cart`, `Favorite`, `Product`. 
- Refer to the models: [/assignment-1/models](https://git.cs.dal.ca/adimurthy/5709-tutorials/-/tree/master/assignment-1/models)

## Project Structure: 
- [Kebab Case](https://www.upbeatcode.com/react/react-naming-conventions/) Naming convention
### Client-side (React)
- components: individual standalone, reusable sections of the application.
- action-type: Represents the different operations performed in a component. For example: the favorites component has operations such as "getFavorites", "addToFavorites" and "removeFromFavorites"
- actions: the implementation of action-type, uses axios to make API calls to the backend to perform the action-types.
- constants: hard coded static content segregated together in one place for easier access. 
- pages: Individual pages of the application, each page is usually a combination of different components. Example: Home page and Favorites page.
- reducers: an abstraction for state management and receives input of the current/initiate state and the action as the input and returns the new state.
- styles: css files for pages.
- utils: static generic functions.

### Backend (NodeJS)
- routes: List of APIs with path and the controller to visit to process a request.
- controller: The business logic layer with dependency on the service layer to perform the necessary actions.
- models: Schema of database models stored in MongoDB.
- logs: path to store application logs (rolling logs).

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

* [React](https://reactjs.org/) - A JavaScript library for building user interfaces
* [Material UI](https://mui.com/) - A comprehensive suite of UI tools and production-ready components
* [NodeJS](https://nodejs.org/en/) - A JavaScript runtime built on Chrome's V8 JavaScript engine
* [Express](https://expressjs.com/) - Fast, unopinionated, minimalist web framework for Node.js
* [MongoDB](https://www.mongodb.com/) - A source-available cross-platform document-oriented database

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

### Folder: images
- Self Attribution
- Created using [ProCreate](https://procreate.art/) by Adesh Nalpet Adimurthy

## References
```
[1] Rukminim1, “Ecommerce Images,” GitHub, May 26, 2022. https://rukminim1.flixcart.com/ (accessed Jun. 01, 2022).

[2] “Amazon.ca: Online shopping in Canada” Amazon.ca, 2019. https://www.amazon.ca/ (accessed Jun. 01, 2022).

[3] Walmart, “Walmart,” Walmart.ca, 2019. https://www.walmart.ca/en (accessed Jun. 01, 2022).

[4] “React Best Practices and Security,” TatvaSoft Blog. https://www.tatvasoft.com/blog/reactjs-best-practices/ (accessed Jun. 04, 2022).

[5] A. N. Adimurthy, “PyCommerce,” GitHub. https://github.com/addu390/py-commerce/blob/master/client/src/pages/error-page.js (accessed Jun. 02, 2022).

[6] Figma, “Figma: the collaborative interface design tool.,” Figma, 2019. https://www.figma.com/ (accessed Jun. 03, 2022).

[7] “Flowchart Maker & Online Diagram Software,” app.diagrams.net. https://draw.io/ (accessed May. 30, 2022).

[8] W3C, “The W3C Markup Validation Service,” W3.org, 2013. https://validator.w3.org/ (accessed Jun. 04, 2022)

[9] “MUI: The React component library you always wanted,” mui.com. https://mui.com/ (accessed May. 30, 2022).

[10] Node.js Foundation, “Node.js,” Node.js, 2019. https://nodejs.org/en/ (accessed May. 30, 2022).
‌
[11] MongoDB, “The most popular database for modern apps,” MongoDB, 2019. https://www.mongodb.com/ (accessed May. 30, 2022).
‌
[12] Facebook, “React – A JavaScript library for building user interfaces,” Reactjs.org, 2022. https://reactjs.org/ (accessed May. 30, 2022).

[13] Pyblog, “pyblog.xyz“, 2021. https://pyblog.xyz (accessed Jun. 01, 2022).
‌
```
‌
