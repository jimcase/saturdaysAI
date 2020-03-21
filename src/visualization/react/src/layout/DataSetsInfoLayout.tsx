import React, {useState, useEffect} from 'react';
import '../style/layout/DataFrameLayout.css';
import {Row, Col, Container, ListGroup, Accordion, Card} from 'react-bootstrap';

function DataSetsInfo() {

    return (
        <div className="DataFrameLayout">
            <Row>
                <Accordion defaultActiveKey="0" className="DataFrameLayout_Accordion">
                    <Card>
                        <Accordion.Toggle as={Card.Header} eventKey="0">
                            Data Set 1.tsv
                        </Accordion.Toggle>
                        <Accordion.Collapse eventKey="0">
                            <Card.Body>Hello! I'm the body</Card.Body>
                        </Accordion.Collapse>
                    </Card>

                </Accordion>
            </Row>
        </div>
    );
}

export default DataSetsInfo;
