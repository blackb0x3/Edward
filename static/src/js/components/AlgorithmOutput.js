import React, { Component } from "react";
import { Col, Input, Row } from "reactstrap";
import Plot from "react-plotly.js";

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
    let outputHtml;

    // only display the input and output if we run the algorithm once
    if (this.props.action === "run") {
      switch (this.props.inputType) {
        case "list":
            let elementInputComponents = this.props.results.input.map(elmnt => <Col md={2}><Input type="text" className="element-input-component" readOnly={true} value={elmnt} /></Col> );
            let elementOutputComponents = this.props.results.output.map(elmnt => <Col md={2}><Input type="text" className="element-output-component" readOnly={true} value={elmnt} /></Col> );
            outputHtml = (
              <Col md={6}>
                <Row>
                  {elementInputComponents}
                </Row>
                <Row>
                  {elementOutputComponents}
                </Row>
                <Row>
                  <p>Execution Time: {this.props.results['execution_time']}</p>
                </Row>
              </Col>
            );
          break;

        case "graph":
          inputOutputHtml = ( <div>Hello World!</div> );
          break;

        case "string":
          inputOutputHtml = ( <div>Hello World!</div> );
          break;

        default:
          inputOutputHtml = ( <div>Hello World!</div> );
          break;
      }
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
                mode   : "lines+points",
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