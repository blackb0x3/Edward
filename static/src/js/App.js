import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import EdwardNav from "./components/EdwardNav";
import Home from "./pages/Home";

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
    return (
      <div>
        <EdwardNav></EdwardNav>
        <Router>
          <Route path="/" component={Home}></Route>
          <Route path="/home" component={Home}></Route>
          {/*<Route path="/sorting" component={}></Route>*/}
        </Router>
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