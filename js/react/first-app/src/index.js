import React from "react";
import ReactDOM from "react-dom/client";

function Greeting() {
    return (
        <div>
            <PersonBin />
            <BinDescription />
        </div>
    );
}

const PersonBin = () => {
    return <h1>Bin is Here</h1>;
};
const BinDescription = () => <p>He is a cool human</p>;

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<Greeting />);
