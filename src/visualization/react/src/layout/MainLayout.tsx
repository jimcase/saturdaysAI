import React, {useState, useEffect} from 'react';
import '../style/layout/AppLayout.css';
import {Row, Col, Container, ListGroup} from 'react-bootstrap';
import DataFrameLayout from './DataFrameLayout';

function MainLayout() {

    return (
        <div className="MainLayout">
            <Row className="">
                <Col>
                    Basic Info
                </Col>
                <Col>
                    More basic info
                </Col>
            </Row>
            <Row>
                <Col>
                    <DataFrameLayout/>
                </Col>
            </Row>
        </div>
    );
}

export default MainLayout;
