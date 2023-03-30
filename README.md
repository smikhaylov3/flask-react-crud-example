# FullStack Example

This CRUD App can manipulate a database which includes a key and a pair of names, as follows:

![](./docs/Screenshot.png)
___

## Implementation

This app is meant to demonstrate a simple CRUD (Create, Read, Update, Delete) app built with Flask and React.

To run the app:

- Install all necessary python modules with pip. Keep running main.py in the backend directory.
- Run npm install in the frontend directory. Please note this was tested with node 16.16.0 lts
- After npm install finishes start the frontend using npm start.
- To find out your version of node run node -v. To easily switch node versions use NVM, if you are unaware of what node version manager is please google it.
- That's it!

## Details

- The top layer is [frontend](./frontend), which utilises the [APIs](./docs) provided by backend. When implementing [frontend](./frontend), we can assume that all the [APIs](./docs) have already been implemented.
- The middle layer is the [backend](./backend), which utilises the functions in [Model layer](./backend/dbms) to manipuate the database. When implementing the [backend](./backend), we assume that all the functions in [Model layer](./backend/dbms) have already been implemented.
- The bottom layer is [Model layer](./backend/dbms), which includes the implementation of the database.