import React from "react";
import "./Modal.css";

function Modal({ setOpenModal }) {
  return (
    <div id="myModal" className="modal">
        <div className="modal-content">
            <span className="close" onClick={()=>{setOpenModal(false)}}>&times;</span>
            <p>Invalid Sudoku grid</p>
        </div>
    </div>
  );
}

export default Modal;
