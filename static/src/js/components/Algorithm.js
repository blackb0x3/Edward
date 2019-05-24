import React, { Component } from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardBody,
  Form,
  Jumbotron
} from "reactstrap";

export default class Algorithm extends Component {
  constructor(props) {
    super(props);

    this.state = {};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() { }

  handleChange() { }

  handleSubmit() { }

  render() {
    return (
      <div>
        <Jumbotron>
          <h1 className="display-3">ALGORITHM NAME</h1>
          <p className="lead">This algorithm...</p>
          <Card>
            <CardHeader>
              <CardTitle>Pseudo Code</CardTitle>
            </CardHeader>
            <CardBody>
              code here....
            </CardBody>
          </Card>
        </Jumbotron>
        <hr/>
        <h3>Test it!</h3>
        <Form></Form>
      </div>
    );
  }
}