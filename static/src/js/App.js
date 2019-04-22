import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Card, CardHeader, CardBody, CardTitle } from "reactstrap";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() { }

  render() {
    return (
      <Router>
        {/* <Route></Route> */}
      </Router>
    );
  }

  /* render() {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Hello World!</CardTitle>
        </CardHeader>
        <CardBody>
          Testing a card.
        </CardBody>
      </Card>
    );
  } */
}