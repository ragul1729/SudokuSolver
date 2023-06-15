import { useState, forwardRef } from "react";
import "./Board.css"
import SudokoCell from "./SudokoCell";

var IDs=[];
for(let i=0;i<9;i++){
    for(let j=1;j<=9;j++){
        IDs.push((i*9+j).toString());
    }
}

function Board(props, ref)  {
    
    // const [boardState, setBoardState] = useState({0:'.', "1":'.', "2": '.', "3": '.', "4": '.', "5": '.', "6": '.', "7": '.', "8": '.',
    //                                               "9":'.', "10":'.', "11":'.', "12": '.', "13": '.', "14": '.', "15": '.', "16": '.', "17": '.',
    //                                               "18":'.', "19":'.', "20":'.', "21": '.', "22": '.', "23": '.', "24": '.', "25": '.', "26": '.',
    //                                               "27":'.', "28":'.', "29":'.', "30": '.', "31": '.', "32": '.', "33": '.', "34": '.', "35": '.',
    //                                               "36":'.', "37":'.', "38":'.', "39": '.', "40": '.', "41": '.', "42": '.', "43": '.', "44": '.',
    //                                               "45":'.', "46":'.', "47":'.', "48": '.', "49": '.', "50": '.', "51": '.', "52": '.', "53": '.',
    //                                               "54":'.', "55":'.', "56":'.', "57": '.', "58": '.', "59": '.', "60": '.', "61": '.', "62": '.',
    //                                               "63":'.', "64":'.', "65":'.', "66": '.', "67": '.', "68": '.', "69": '.', "70": '.', "71": '.',
    //                                               "72":'.', "73":'.', "74":'.', "75": '.', "76": '.', "77": '.', "78": '.', "79": '.', "80": '.',})

    // function updateSudokuCelValue(e){
    //     setBoardState(prevBoardState => { 
    //         return {...prevBoardState, "e.target.id" : "e.target.value" }
    //     })
    // }                                                  


    return (
    <div id="board" ref={ref} >

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

export default forwardRef(Board);