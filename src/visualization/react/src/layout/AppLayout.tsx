import React, {useState, useEffect} from 'react';
import '../style/layout/AppLayout.css';
import {Row, Col, Container, ListGroup, Alert} from 'react-bootstrap';
import MainLayout from './MainLayout';

function AppLayout() {
    const [currentTime, setCurrentTime] = useState(0);
    useEffect(() => {
        fetch("/time").then(res => res.json().then(data => {
            setCurrentTime(data.time);
        }));
    }, []);
    function alertClicked() {
        alert('You clicked on conf properties');
    }
    return (
        <div className="AppLayout">
            <Row className="header">
                <Container>
                    <Alert variant={'primary'}>
                        > The current time in milisec is: {currentTime}
                    </Alert>
                </Container>
            </Row>
            <Row className="main">
                <Col xs={12} md={1}>
                    <ListGroup className="leftMenu">
                        <ListGroup.Item action className="leftMenuItem"><a>Home</a></ListGroup.Item>
                        <ListGroup.Item disabled className="leftMenuItem">Data</ListGroup.Item>
                        <ListGroup.Item disabled className="leftMenuItem">Scripts</ListGroup.Item>
                        <ListGroup.Item className="leftMenuItem" onClick={alertClicked}>Conf</ListGroup.Item>
                    </ListGroup>
                </Col>
                <Col>
                    <MainLayout/>
                </Col>
            </Row>
        </div>
    );
}

export default AppLayout;
