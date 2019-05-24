import React, { Component } from "react";
import { NavLink as NavLinkRouterDom } from "react-router-dom";

import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  Dropdown
} from "reactstrap";

export default class EdwardNav extends Component {
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
        <Navbar color="dark" dark expand="md">
          <NavbarBrand href="/">Edward</NavbarBrand>
          <NavbarToggler onClick={this.toggle} />
          <Collapse isOpen={this.state.isOpen} navbar>
            <Nav className="ml-auto" navbar>
              <UncontrolledDropdown nav inNavbar>
                <DropdownToggle nav caret>
                  Sorting
                </DropdownToggle>
                <DropdownMenu right>
                  <DropdownItem>
                    <NavLinkRouterDom to="/sorting/insertion-sort">Insertion Sort</NavLinkRouterDom>
                  </DropdownItem>
                  <DropdownItem>
                    <NavLinkRouterDom to="/sorting/selection-sort">Selection Sort</NavLinkRouterDom>
                  </DropdownItem>
                  <DropdownItem>
                    <NavLinkRouterDom to="/sorting/counting-sort">Counting Sort</NavLinkRouterDom>
                  </DropdownItem>
                  <DropdownItem divider />
                  <DropdownItem href="/sorting">
                    <NavLinkRouterDom to="/sorting">More...</NavLinkRouterDom>
                  </DropdownItem>
                </DropdownMenu>
              </UncontrolledDropdown>
              <UncontrolledDropdown nav inNavbar>
                <DropdownToggle nav caret>
                  Searching
                </DropdownToggle>
                <DropdownMenu right>
                  <DropdownItem>
                    <NavLinkRouterDom to="/searching/linear">Linear Search</NavLinkRouterDom>
                  </DropdownItem>
                  <DropdownItem>
                    <NavLinkRouterDom to="/searching/bilinear">Bi-linear Search</NavLinkRouterDom>
                  </DropdownItem>
                  <DropdownItem>
                    <NavLinkRouterDom to="/searching/binary">Binary Search</NavLinkRouterDom>
                  </DropdownItem>
                  <DropdownItem divider />
                  <DropdownItem>
                    <NavLinkRouterDom to="/searching">More...</NavLinkRouterDom>
                  </DropdownItem>
                </DropdownMenu>
              </UncontrolledDropdown>
              <NavItem>
                <NavLink><NavLinkRouterDom to="/settings">Settings</NavLinkRouterDom></NavLink>
              </NavItem>
            </Nav>
          </Collapse>
        </Navbar>
      );
  }
};