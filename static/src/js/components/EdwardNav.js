import React, { Component } from "react";
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
                  <DropdownItem href="/sorting/insertion-sort">
                    Insertion Sort
                  </DropdownItem>
                  <DropdownItem href="/sorting/selection-sort">
                    Selection Sort
                  </DropdownItem>
                  <DropdownItem href="/sorting/counting-sort">
                    Counting Sort
                  </DropdownItem>
                  <DropdownItem divider />
                  <DropdownItem href="/sorting">
                    More...
                  </DropdownItem>
                </DropdownMenu>
              </UncontrolledDropdown>
              <UncontrolledDropdown nav inNavbar>
                <DropdownToggle nav caret>
                  Searching
                </DropdownToggle>
                <DropdownMenu right>
                  <DropdownItem href="/searching/linear">
                    Linear Search
                  </DropdownItem>
                  <DropdownItem href="/searching/bilinear">
                    Bi-linear Search
                  </DropdownItem>
                  <DropdownItem href="/searching/binary">
                    Binary Search
                  </DropdownItem>
                  <DropdownItem divider />
                  <DropdownItem href="/searching">
                    More...
                  </DropdownItem>
                </DropdownMenu>
              </UncontrolledDropdown>
              <NavItem>
                <NavLink href="/settings">Settings</NavLink>
              </NavItem>
            </Nav>
          </Collapse>
        </Navbar>
      );
  }
};