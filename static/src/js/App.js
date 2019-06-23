import React, { Component } from "react";
import { BrowserRouter, Route } from "react-router-dom";

import EdwardNav from "./components/EdwardNav";
import Home from "./pages/Home";
import Algorithm from "./components/Algorithm";

import INPUT_OUTPUT_TYPES from "./config";
import AlgorithmType from "./pages/AlgorithmType";

export default class App extends Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);

    this.state = {
      isOpen: false
    };
  }

  componentDidMount() { }

  toggle() {
    this.setState( { isOpen: !this.state.isOpen } );
  }

  render() {
    let insertionSortKey = "insertion-sort";
    let selectionSortKey = "selection-sort";
    let countingSortKey = "counting-sort";
    let linearSearchKey = "linear-search";
    let bilinearSearchKey = "bi-linear-search";
    let binarySearchKey = "binary-search";

    return (
      <div>
        <BrowserRouter>
          <EdwardNav></EdwardNav>

          <Route
            exact
            path="/"
            component={Home}
          />

          <Route
            exact
            path="/home"
            component={Home}
          />

          <Route
            exact
            path="/sorting/insertion-sort"
            render={ (props) => <Algorithm {...props} algorithmKey={insertionSortKey} inputType={INPUT_OUTPUT_TYPES.LIST} outputType={INPUT_OUTPUT_TYPES.LIST} /> }
          />

          <Route
            exact
            path="/sorting/selection-sort"
            render={ (props) => <Algorithm {...props} algorithmKey={selectionSortKey} inputType={INPUT_OUTPUT_TYPES.LIST} outputType={INPUT_OUTPUT_TYPES.LIST} /> }
          />
          
          <Route
            exact
            path="/sorting/counting-sort"
            render={ (props) => <Algorithm {...props} algorithmKey={countingSortKey} inputType={INPUT_OUTPUT_TYPES.LIST} outputType={INPUT_OUTPUT_TYPES.LIST} /> }
          />

          <Route
            exact
            path="/sorting"
            render={ (props) => <AlgorithmType {...props} algorithmType="sorting" /> }
          />

          {/*
          <Route
            exact
            path="/searching/linear"
            render={ (props) => <Algorithm {...props} algorithmKey={linearSearchKey} inputType={INPUT_OUTPUT_TYPES.LIST} outputType={INPUT_OUTPUT_TYPES.NUMBER} /> }
          />
          
          <Route
            exact
            path="/searching/bilinear"
            render={ (props) => <Algorithm {...props} algorithmKey={bilinearSearchKey} inputType={INPUT_OUTPUT_TYPES.LIST} outputType={INPUT_OUTPUT_TYPES.NUMBER} /> }
          />

          <Route
            exact
            path="/searching/binary"
            render={ (props) => <Algorithm {...props} algorithmKey={binarySearchKey} inputType={INPUT_OUTPUT_TYPES.LIST} outputType={INPUT_OUTPUT_TYPES.NUMBER} /> }
          />
          */}

          <Route
            exact
            path="/searching"
            render={ (props) => <AlgorithmType {...props} algorithmType="searching" /> }
          />
        </BrowserRouter>
      </div>
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