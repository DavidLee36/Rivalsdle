import React, { useEffect, useState } from 'react';
import Search from '../components/search.jsx';
import "../styles/app.css";

const Home = () => {
    return (
        <div className="page-wrapper">
            <h1>Rivalsdle</h1>
            <Search/>
        </div>
    )
}

export default Home