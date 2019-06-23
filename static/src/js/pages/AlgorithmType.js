import React, { Component } from "react";
import {
  Card,
  CardBody,
  CardTitle,
  Button } from "reactstrap";
import axios from "axios";
import { NavLink as NavLinkRouterDom } from "react-router-dom";

export default class AlgorithmType extends Component {
  constructor(props) {
    super(props);

    console.log("hi");

    this.state = {
      algorithmType : props.algorithmType,
      algorithmKeys : {}
    };
  }

  componentDidMount() {
    axios.get(`/api/algorithmType/${this.state.algorithmType}`)
      .then(resp => {
        this.setState({
          algorithmKeys: resp.data
        });
      })
      .catch(err => alert(err));
  }

    // push to `/${this.state.algorithmKey}/${chosenKey}`

  render() {
    return (
      <div>
        {Object.keys(this.state.algorithmKeys).map(key => <Card><CardBody><CardTitle>{this.state.algorithmKeys[key]}</CardTitle><NavLinkRouterDom to={`${this.state.algorithmType}/${key}`}><Button outline color="secondary">Go!</Button></NavLinkRouterDom></CardBody></Card>)}
      </div>
    );
  }
}