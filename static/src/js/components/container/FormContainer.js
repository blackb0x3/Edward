import React, { Component } from "react";
import ReactDOM from "react-dom";
import Input from "../presentational/Input.js";

class FormContainer extends Component {
    constructor(props) {
        super(props);

        this.state = {
            title: ""
        };

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({ [event.target.id]: event.target.value });
        console.log(event.target.value);
    }

    render() {
        return (
            <form id="article-form">
            <Input
                text="title here"
                label="title"
                type="text"
                id="title"
                value={this.title}
                handleChange={this.handleChange}
            />
            </form>
        );
    }
}

export default FormContainer;
