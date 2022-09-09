
import React from 'react';

const ChildRender = React.memo(props => {
    console.log('Child Render');
    return <h2> { props.name } </h2>;
  });

export default function Child() {
    return ( 
        <ChildRender />
    );
}


