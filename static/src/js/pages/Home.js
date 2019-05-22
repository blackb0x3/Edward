import React, { Component } from "react";
import { Button, Jumbotron } from "reactstrap";

export default class Home extends Component {
  constructor(props) {
    super(props);

    this.state = {};
  }

  componentDidMount() { }

  render() {
    return (
      <Jumbotron>
        <h1 className="display-3">Edward</h1>
        <p className="lead">A React + Python application demonstrating time and space complexities of various algorithms and data structures.</p>
        <hr/>
        <p>New features are being added to the site regularly!</p>
        <p className="lead">
          <Button color="primary">Learn more.</Button>{' '}
          <Button color="secondary">Contribute!</Button>
        </p>
      </Jumbotron>
    );
  }
}