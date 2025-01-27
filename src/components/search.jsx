import React, { useState, useEffect } from 'react';
import heroesData from '../../data_retrieval/heroes_lore.json';

const Search = () => {
    const [heroes, setHeroes] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        // Map the JSON data into an array of objects with name and image path
        const heroList = heroesData.map((hero) => {
            const name = Object.keys(hero)[0];
            return {
                name,
                image: `/assets/images/hero_icons/${name.toLowerCase()}.png`,
            };
        });
        setHeroes(heroList);
    }, []);

    // Filter heroes based on the search query
    const filteredHeroes =
        searchQuery.trim() === ''
            ? []
            : heroes.filter((hero) =>
                  hero.name.toLowerCase().includes(searchQuery.toLowerCase())
              );

    const heroClick = (e, hero) => {
        console.log(hero.name);
    }

    return (
        <div>
            <h2>Search</h2>
            <input
                type="text"
                placeholder="Search characters..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
            />
            {searchQuery.trim() !== '' && (
                <ul className="hero-list">
                    {filteredHeroes.map((hero, index) => (
                        <li
                            key={index}
                            className="hero-item"
                            onClick={e => heroClick(e, hero)}
                        >
                            <img
                                src={hero.image}
                                alt={hero.name}
                                className="hero-image"
                            />
                            <p>{hero.name}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};


export default Search;
