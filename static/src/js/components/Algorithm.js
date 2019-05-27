import React, { Component } from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardBody,
  Form,
  Input,
  Jumbotron
} from "reactstrap";

import axios from "axios";

export default class Algorithm extends Component {
  constructor(props) {
    super(props);

    this.state = {
      key         : props.algorithmKey,
      name        : "",
      description : "",
      steps       : [],
      bestCase    : "",
      averageCase : "",
      worstCase   : ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    axios.get(`/api/algorithms/${this.state.key}`)
      .then(resp => {
        this.setState({
          name        : resp.data.name,
          description : resp.data.description,
          steps       : resp.data.steps,
          bestCase    : resp.data.best_case,
          averageCase : resp.data.average_case,
          worstCase   : resp.data.worst_case
        });
      })
      .catch(err => alert(err));
  }

  handleChange() { }

  handleSubmit() { }

  render() {
    var stepsHtml = this.state.steps.map((stepText) => {
      return ( <li>{stepText}</li> );
    });

    console.log(stepsHtml);

    return (
      <div>
        <Jumbotron>
          <h1 className="display-3">{this.state.name}</h1>
          <p className="lead">{this.state.description}</p>
          <Card>
            <CardHeader>
              <CardTitle>Pseudo Code</CardTitle>
            </CardHeader>
            <CardBody>
              <ol>
                {stepsHtml}
              </ol>
            </CardBody>
          </Card>
        </Jumbotron>
        <hr/>
        <h3>Test it!</h3>
      </div>
    );
  }
}