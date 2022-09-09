
import React from 'react';
import { useState } from 'react';
import Child from './Child';

export function Parent() {
    const [count, setCount] = useState(0);

    const handleClick = () => { setCount(count + 1); };
    console.log('Parent Render');

    return ( 
        <div>
            <button onClick = { handleClick }> Increase Count </button> 
            <h2> { count } </h2> 
            <Child name = { 'Child Component' } /> 
        </div >
    );
}
