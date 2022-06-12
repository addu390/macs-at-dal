# Tutorial 4
Individual Submission

* *Date Created*: 09 Jun 2022
* *Last Modification Date*: 11 Jun 2022
* *Git URL Repository*: <https://git.cs.dal.ca/adimurthy/5709-tutorials>
* *Git URL Assignment*: <https://git.cs.dal.ca/adimurthy/5709-tutorials/-/tree/master/tutorial-4>
* *Deployed Application*: <https://tutorial-4-5709.herokuapp.com>

## Author
* [Adesh Nalpet Adimurthy](adesh.nalpet@dal.ca) - *(React Application Development)*

## Overview
A react application with login, user list with search functionality and user profile.

## Getting Started
## Prerequisites
- React application created from [create-react-app](https://create-react-app.dev/)

## Installing
### Local Set-up
- Start Client: `npm install && npm run start`

## Project Structure: 
- [Camel Case](https://www.upbeatcode.com/react/react-naming-conventions/) Naming convention
### Client-side (React)
Since the application solves for the small use case:
- components: individual standalone, reusable sections of the application.
- styles: css files for pages.
- utils: static generic functions.

## Deployment
### Heroku Set-up
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Login and Create a project: `heroku login` and `heroku create <unique-project-name>`
- Deploy: `git push heroku master`

## Built With

* [React](https://reactjs.org/) - A JavaScript library for building user interfaces

## Sources Used

### File: Form.js
```
import React, { Component } from "react";
import { withRouter } from "react-router";

const emailRegex = RegExp(/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/)
const nameRegex = RegExp(/^[a-zA-Z]*$/)
const passwordRegex = RegExp(/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/)

class UserForm extends Component {
    constructor(props) {
        super(props)

        this.state = {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            re_password: '',
            isError: {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                re_password: ''
            }
        }
    }

    formValid = () => {
        let isValid = true;
        Object.values(this.state.isError).forEach(val => {
            if (val.length > 0) {
                isValid = false
            }
        });

        return isValid;
    };

    onSubmit = e => {
        this.validations("first_name", this.state.first_name);
        this.validations("last_name", this.state.last_name);
        this.validations("email", this.state.email);
        this.validations("password", this.state.password);
        this.validations("re_password", this.state.re_password);
        e.preventDefault();

        if (this.formValid(this.state)) {
            this.props.history.push("/profile", { data: this.state })
        } else {
            console.log("Invalid");
        }
    };

    formValChange = e => {
        e.preventDefault();
        const { name, value } = e.target;
        this.validations(name, value);
    };

    validations(name, value) {
        let isError = this.state.isError;
        switch (name) {
            case "first_name":
                if (!nameRegex.test(value)) {
                    isError.first_name = "First name can only have letters";
                }
                else if (value.length < 4) {
                    isError.first_name = "Atleast 4 characaters required";
                } else {
                    isError.first_name = '';
                }
                break;

            case "last_name":
                if (!nameRegex.test(value)) {
                    isError.last_name = "Last name can only have letters";
                }
                else if (value.length < 4) {
                    isError.last_name = "Atleast 4 characaters required";
                } else {
                    isError.last_name = '';
                }
                break;

            case "email":
                isError.email = emailRegex.test(value) ? "" : "Email address is invalid";
                break;

            case "password":
                if (value.length < 8) {
                    isError.password = "Atleast 8 characaters required";
                } else if (!passwordRegex.test(value)) {
                    isError.password = "Should have at least one letter, one number and one special character";
                } else {
                    isError.password = '';
                }

            case "re_password":
                if (this.state.password !== value) {
                    isError.re_password = "Passwords do not match"
                } else {
                    isError.re_password = '';
                }

                break;
            default:
                break;
        }

        this.setState({
            isError,
            [name]: value
        })
    }

    render() {
        const { isError } = this.state;
        return (
            <form onSubmit={this.onSubmit} noValidate>
                <div className="form-group">
                    <label>First Name</label>
                    <input
                        type="text"
                        className={isError.first_name.length > 0 ? "is-invalid form-control" : "form-control"}
                        name="first_name"
                        onChange={this.formValChange}
                    />
                    {isError.first_name.length > 0 && (
                        <span className="invalid-feedback">{isError.first_name}</span>
                    )}
                </div>

                <div className="form-group">
                    <label>Last Name</label>
                    <input
                        type="text"
                        className={isError.last_name.length > 0 ? "is-invalid form-control" : "form-control"}
                        name="last_name"
                        onChange={this.formValChange}
                    />
                    {isError.last_name.length > 0 && (
                        <span className="invalid-feedback">{isError.last_name}</span>
                    )}
                </div>

                <div className="form-group">
                    <label>Email</label>
                    <input
                        type="email"
                        className={isError.email.length > 0 ? "is-invalid form-control" : "form-control"}
                        name="email"
                        onChange={this.formValChange}
                    />
                    {isError.email.length > 0 && (
                        <span className="invalid-feedback">{isError.email}</span>
                    )}
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input
                        type="password"
                        className={isError.password.length > 0 ? "is-invalid form-control" : "form-control"}
                        name="password"
                        onChange={this.formValChange}
                    />
                    {isError.password.length > 0 && (
                        <span className="invalid-feedback">{isError.password}</span>
                    )}
                </div>

                <div className="form-group">
                    <label>Re-enter Password</label>
                    <input
                        type="password"
                        className={isError.re_password.length > 0 ? "is-invalid form-control" : "form-control"}
                        name="re_password"
                        onChange={this.formValChange}
                    />
                    {isError.re_password.length > 0 && (
                        <span className="invalid-feedback">{isError.re_password}</span>
                    )}
                </div>

                <button type="submit" className="btn btn-block btn-danger" onChange={this.onSubmit}>Register</button>
            </form>
        );
    }
}

export default withRouter(UserForm);
```

The above code snipped is from Tutorial 3, developed for a registration form.
- The parts of code in `Form.js` was implemented by `Adesh Nalpet Adimurthy` (Self Attribution).
- `Form.js`'s Code was used because I had a similar use case and re-using the registration form for Login was evident.
- `Form.js`'s Code was further modified to make an API call after form submission along with error handling and only use email and password and omit the rest of the fields used in registration.

### File: ToastMessage.js

```
import { toast } from "react-toastify";

const toastStyle = {
  position: "bottom-center",
  autoClose: 3500,
  hideProgressBar: true,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
  progress: undefined,
  theme: "dark",
  closeButton: false,
};

const toastMessage = (msg, type) => {
  switch (type) {
    case "info":
      toast.info(msg, toastStyle);
      break;
    case "error":
      toast.error(msg, toastStyle);
      break;
    case "success":
      toast.success(msg, toastStyle);
      break;
    case "warning":
      toast.warning(msg, toastStyle);
      break;
    default:
      toast.info(msg, toastStyle);
      break;
  }
};

export default toastMessage;

```

- The parts of code in `ToastMessage.js` was implemented by `Adesh Nalpet Adimurthy (Self Attribution)` for assignment 1.
- `ToastMessage.js`'s Code was used because I had previously written a generic simple toast message component for asssignment 1 (aslo used for the project).
- `ToastMessage.js`'s Code was modified to add additional CSS for design consistency for the tutorial.


## References
```
[1] “React Best Practices and Security,” TatvaSoft Blog. https://www.tatvasoft.com/blog/reactjs-best-practices/ (accessed Jun. 04, 2022).

[2] A. N. Adimurthy, “PyCommerce,” GitHub. https://github.com/addu390/py-commerce/blob/master/client/src/pages/error-page.js (accessed Jun. 02, 2022).

[3] W3C, “The W3C Markup Validation Service,” W3.org, 2013. https://validator.w3.org/ (accessed Jun. 04, 2022)

[4] Pyblog, “pyblog.xyz“, 2021. https://pyblog.xyz (accessed Jun. 01, 2022).
‌
```
‌
