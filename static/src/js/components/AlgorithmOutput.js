import React, { Component } from "react";
import { Col, Input, Row } from "reactstrap";
import Plot from "react-plotly.js";
import INPUT_OUTPUT_TYPES from "../config";

export default class AlgorithmOutput extends Component {
  constructor(props) {
    super(props);

    this.state = {
      algorithmName : props.algorithmName,
             action : props.action,
            results : props.results,
          inputType : props.inputType
    };
  }

  componentDidMount() { }

  render() {
    let inputPart, outputPart, outputHtml;

    // only display the input and output if we run the algorithm once
    if (this.props.action === "run") {
      switch (this.props.inputType) {
        case INPUT_OUTPUT_TYPES.LIST:
          inputPart = this.props.results.input.map(elmnt => <Col md={3}><Input type="text" className="element-input-component" readOnly={true} value={elmnt} /></Col> );
          break;

        case INPUT_OUTPUT_TYPES.GRAPH:
          inputPart = ( <div>Hello World!</div> );
          break;

        case INPUT_OUTPUT_TYPES.STRING:
        case INPUT_OUTPUT_TYPES.BOOLEAN:
        case INPUT_OUTPUT_TYPES.NUMBER:
          inputPart = ( <div>{this.props.results.input}</div> );
          break;

        default:
          inputPart = ( <div>Hello World!</div> );
          break;
      }

      switch (this.props.outputType) {
        case INPUT_OUTPUT_TYPES.LIST:
          outputPart = this.props.results.output.map(elmnt => <Col md={3}><Input type="text" className="element-output-component" readOnly={true} value={elmnt} /></Col> );
          break;

        case INPUT_OUTPUT_TYPES.GRAPH:
          outputPart = ( <div>Hello World!</div> );
          break;

        case INPUT_OUTPUT_TYPES.STRING:
        case INPUT_OUTPUT_TYPES.BOOLEAN:
        case INPUT_OUTPUT_TYPES.NUMBER:
          outputPart = ( <div>{this.props.results.output}</div> );
          break;

        default:
          outputPart = ( <div>Hello World!</div> );
          break;
      }

      outputHtml = (
        <Col md={12}>
          <Row>
            <h5>INPUT</h5>
            <Row>{inputPart}</Row>
          </Row>
          <Row>
            <h5>OUTPUT</h5>
            <Row>{outputPart}</Row>
          </Row>
          <Row>
            <h5>EXECUTION TIME</h5>
            <Row><Col><Input type="text" className="element-execution-time-component" readOnly={true} value={this.props.results['execution_time']} /></Col></Row>
          </Row>
        </Col>
      );
    }

    // test action on Python side uses different collections per repeat and / or jump
    else if (this.props.action === "test") {
      let xPlot = this.props.results.sizes;
      let yPlot = this.props.results.times;

      outputHtml = (
        <Plot
          data={[
            {
                   x   : xPlot,
                   y   : yPlot,
                type   : "scatter",
                mode   : "markers",
                marker : {
                  color : "blue"
                }
            }
          ]}

          layout={{
            title : {
              text: `Test results for the ${this.state.algorithmName} - ${(new Date(Date.now())).toLocaleString()}`
            },

            xaxis : {
              title : {
                text : "Collection Size"
              }
            },

            yaxis : {
              title : {
                text : "Time Taken"
              }
            }
          }}
        />
      );
    }

    return (
      <div className="result-specifics">
        {outputHtml}
      </div>
    );
  }
}