import { useState } from "react";
import "./SudokoCell.css"

function SudokoCell(props){
    
    function fun1(e){
        if(e.target.value.length > 0){
            if(e.key !== "Backspace")
                e.preventDefault();
            else
                return;
        }
        if(e.key == null || e.key.length != 1)
            e.preventDefault();
        var unicode = e.key.charCodeAt(0);
        if(unicode < 48 || unicode > 57)
            e.preventDefault();
        
    }

    return ( 
    <input className="cell" onKeyDown={fun1} id={props.id}>
         
    </input> 
    );
}

export default SudokoCell;