import React, { Component } from "react";
import {
  Button,
  ButtonGroup,
  Card,
  CardHeader,
  CardTitle,
  CardBody,
  Container,
  Jumbotron
} from "reactstrap";

import axios from "axios";
import { List, Graph } from "./AlgorithmInputs/index";

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
      worstCase   : "",
      action      : "run"
    };
    
    this.setAlgorithmAction = this.setAlgorithmAction.bind(this);
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

  setAlgorithmAction(e) {
    e.preventDefault();

    this.setState({
      action: e.target.value
    });
  }

  validateForm() {

  }

  onPostDataReceived(postData) {
    console.log(postData);
  }

  render() {
    var stepsHtml = this.state.steps.map((stepText) => {
      return ( <li>{stepText}</li> );
    });

    let algorithmFormInput;

    switch (this.props.inputType) {
      case "list":
        algorithmFormInput = <List  onPostDataReceived={this.onPostDataReceived} action={this.state.action} />;
        break;
      case "graph":
        algorithmFormInput = <Graph onPostDataReceived={this.onPostDataReceived} action={this.state.action} />;
        break;
      default:
        algorithmFormInput = <List  onPostDataReceived={this.onPostDataReceived} action={this.state.action} />;
        break;
    }

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
        <Container>
          <h3>Try it out!</h3>
          <ButtonGroup>
            <Button id="action-run"  className="action" value="run"  onClick={this.setAlgorithmAction} color="primary">Run</Button>
            <Button id="action-test" className="action" value="test" onClick={this.setAlgorithmAction} color="secondary">Test</Button>
          </ButtonGroup>
          {algorithmFormInput}
        </Container>
      </div>
    );
  }
}