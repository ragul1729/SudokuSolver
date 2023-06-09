import "./Board.css"
import SudokoCell from "./SudokoCell";

var IDs=[];
for(let i=0;i<9;i++){
    for(let j=1;j<=9;j++){
        IDs.push((i*9+j).toString());
    }
}

function Board(){
    
    return (
    <div id="board">

        {IDs.map(ID => {return <SudokoCell id={ID} />})}
        {/* <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />

        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />

        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />

        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />

        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />

        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />

        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />

        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell />
        <SudokoCell /> */}
    </div>
    );
}

export default Board;