import React, { Component } from "react";
import {
  Button,
  ButtonGroup,
  Card,
  CardHeader,
  CardTitle,
  CardBody,
  Col,
  Container,
  Input,
  Jumbotron,
  Row
} from "reactstrap";

import axios from "axios";
import { List, Graph } from "./AlgorithmInputs/index";
import AlgorithmOutput from "./AlgorithmOutput";
import INPUT_OUTPUT_TYPES from "../config";

export default class Algorithm extends Component {
  constructor(props) {
    super(props);

    // algorithmKey is the endpoint name used in the GET and POST requests
    this.state = {
      algorithmOutput : null,
         algorithmKey : props.algorithmKey,
         inputType    : props.inputType,
         outputType   : props.outputType,
         name         : "",
         description  : "",
         steps        : [],
         bestCase     : "",
         averageCase  : "",
         worstCase    : "",
         action       : "run"
    };
    
    this.setAlgorithmAction = this.setAlgorithmAction.bind(this);
    this.onPostDataReceived = this.onPostDataReceived.bind(this);
  }

  componentDidMount() {
    axios.get(`/api/algorithms/${this.state.algorithmKey}`)
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

  /**
   * Sets the user's desired action for the algorithm.
   * @param {*} e The event object.
   */
  setAlgorithmAction(e) {
    e.preventDefault();

    console.log(e.target);

    this.setState({
      action: e.target.value
    }, () => console.log(this.state));
  }

  /**
   * Callback function which activates the chosen algorithm via the Python API, and renders the results
   * @param {*} postData The post body to send to the Python API.
   */
  onPostDataReceived(postData) {
    axios.post(`/api/algorithms/${this.state.algorithmKey}`, postData)
      .then(resp => {
        console.log(resp.data);

        this.setState({algorithmOutput: <AlgorithmOutput algorithmName={this.state.name} action={this.state.action} results={resp.data} inputType={this.props.inputType} outputType={this.props.outputType} />})
      })
      .catch(err => console.log(err));
  }

  render() {
    var stepsHtml = this.state.steps.map((stepText) => {
      return ( <li>{stepText}</li> );
    });

    let algorithmFormInput;

    // determine input type from props
    // input type (string, list, dict, graph etc.) can change based on the algorithm
    // e.g. binary search needs a list, but djikstra requires a graph
    switch (this.props.inputType) {
      case INPUT_OUTPUT_TYPES.LIST:
        algorithmFormInput = <List algorithmKey={this.state.algorithmKey} onPostDataReceived={this.onPostDataReceived} action={this.state.action} />;
        break;

      case INPUT_OUTPUT_TYPES.GRAPH:
        algorithmFormInput = <Graph algorithmKey={this.state.algorithmKey} onPostDataReceived={this.onPostDataReceived} action={this.state.action} />;
        break;

      // TODO
      case INPUT_OUTPUT_TYPES.STRING:
        algorithmFormInput = <div>Hello World!</div>;
        break;

      // TODO
      case INPUT_OUTPUT_TYPES.NUMBER:
        algorithmFormInput = <div>Hello World!</div>;
        break;

      // TODO
      case INPUT_OUTPUT_TYPES.DICT:
        algorithmFormInput = <div>Hello World!</div>;
        break;

      // TODO
      case INPUT_OUTPUT_TYPES.BOOLEAN:
        algorithmFormInput = <div>Hello World!</div>;
        break;

      // TODO
      case INPUT_OUTPUT_TYPES.CUSTOM:
      default:
        algorithmFormInput = <List algorithmKey={this.state.algorithmKey} onPostDataReceived={this.onPostDataReceived} action={this.state.action} />;
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
          <h3>Try it out now!</h3>
          <ButtonGroup>
            <Button id="action-run"  className="action" value="run"  onClick={this.setAlgorithmAction} color="primary">Run</Button>
            <Button id="action-test" className="action" value="test" onClick={this.setAlgorithmAction} color="secondary">Test</Button>
          </ButtonGroup>
          <Row>
            <Col>
              {algorithmFormInput}
            </Col>
            <Col>
              {this.state.algorithmOutput}
            </Col>
          </Row>

        </Container>
      </div>
    );
  }
}