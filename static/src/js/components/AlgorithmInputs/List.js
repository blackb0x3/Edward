import React, { Component } from "react";
import { Button, Col, Form, FormGroup, Input, Label, Row } from "reactstrap";
import axios from "axios";

export default class List extends Component {
  constructor(props) {
    super(props);

    this.state = {
      algorithmKey : props.algorithmKey,
      action       : props.action,
      listSizeMin  : 5,
      listSizeMax  : 20,
      listSizeJump : 1,
      repeats      : 5,
      runInputs    : {
        "list-item-0": null
      }
    };

    this.handleListElementChange = this.handleListElementChange.bind(this);
    this.pushRunInput = this.pushRunInput.bind(this);
    this.popRunInput  = this.popRunInput.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() { }

  handleListElementChange(e) {
    e.preventDefault();

    let objToMerge = {};
    objToMerge[e.target.id] = parseInt(e.target.value);

    let regex = new RegExp(/^\d+$/);

    if (regex.test(e.target.value)) {
      this.setState({
        runInputs: {
          ...this.state.runInputs,
          ...objToMerge
        }
      }, () => console.log(this.state.runInputs));
    } else {
      return false;
    }
  };

  pushRunInput() {
    let newInputObj = {};
    newInputObj[`list-item-${Object.keys(this.state.runInputs).length}`] = null;
    this.setState( prevState => ( { runInputs: Object.assign( prevState.runInputs, newInputObj ) } ) );
  }

  popRunInput() {
    let objToReturn = {...this.state.runInputs};
    let length = Object.keys(this.state.runInputs).length
    delete objToReturn[`list-item-${length - 1}`];
    this.setState( prevState => ( { runInputs: objToReturn } ) );
  }

  handleSubmit(e) {
    e.preventDefault();

    let postData = {
      action: this.state.action
    };
    
    switch (this.state.action) {
      case "run":
        postData["collection"] = Object.values(this.state.runInputs);
        break;
      case "test":
        postData["options"] = {
          min_size : this.state.listSizeMin,
          max_size : this.state.listSizeMax,
          jump     : this.state.listSizeJump,
          repeats  : this.state.repeats
        };
        break;
    }

    this.props.onPostDataReceived(postData);
  }

  render() {
    // html for run action
    let runHtml = (
      <Form onSubmit={this.handleSubmit}>
        <h5>Provide the algorithm with a specific list of elements as input.</h5>
        <Col>
          <FormGroup>
            <Row>
              {Object.keys(this.state.runInputs).map(input => <Col md={1}><Input type="text" className="listElementInput" id={input} onChange={this.handleListElementChange} />{' '}</Col> )}
            </Row>
          </FormGroup>
        </Col>
        <Col>
          <FormGroup>
            <Button color="success" onClick={this.pushRunInput}>+ New Element</Button>{' '}
            <Button color="danger" onClick={this.popRunInput}>- Remove Element</Button>
          </FormGroup>
        </Col>
        <Col>
          <FormGroup>
            <Button type="submit" color="secondary">Go!</Button>
          </FormGroup>
        </Col>
      </Form>
    );

    // html for test action
    let testHtml = (
      <Form onSubmit={this.handleSubmit}>
        <h5>Provide parameters to generate varying sizes of lists as inputs for this algorithm.</h5>
        <Col>
          <FormGroup>
            <Label>Minimum Number of Elements</Label>
            <Input
              type="number"
              name="listSizeMin"
              min='5'
              step='1'
            />
          </FormGroup>
        </Col>{' '}
        <Col>
          <FormGroup>
            <Label>Maximum Number of Elements</Label>
            <Input
              type="number"
              name="listSizeMax"
              min='10'
              step='1'
            />
          </FormGroup>
        </Col>{' '}
        <Col>
          <FormGroup>
            <Label>Size Steps</Label>
            <Input
              type="number"
              name="listSizeJump"
              min='1'
              step='1'
            />
          </FormGroup>
        </Col>{' '}
        <Col>
          <FormGroup>
            <Label>Repetitions</Label>
            <Input
              type="number"
              name="repeats"
              min='3'
              step='1'
            />
          </FormGroup>
        </Col>
        <Col>
          <FormGroup>
            <Button type="submit" color="secondary">Go!</Button>
          </FormGroup>
        </Col>
      </Form>
    );

    // default html if action cannot be verified / is not implemented
    let defaultHtml = (
      <div>
        <h4>Unknown action provided</h4>
      </div>
    );

    if (this.state.action === "run") {
      return runHtml;
    } else if (this.state.action === "test") {
      return testHtml;
    } else {
      return defaultHtml;
    }
  }
}