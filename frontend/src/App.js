import logo from './logo.svg';
import './App.css';
import Board from './Board';
import Modal from './Modal';
import Button from '@mui/material/Button';
import axios from "axios";
import { useState, useRef } from 'react';

const baseURL = "http://localhost:5000/state";

function App() {

  const [modalOpen, setModalOpen] = useState(false);
  const Sboard = useRef();

  // function ValidateGrid(){
  //   Sboard.body.Children
  // }

  function ValidateAndSend(){
    const sudokuBoard = [['.', '.', '.', '7', '.', '3', '1', '.', '.'],
                         ['.', '5', '.', '4', '9', '.', '8', '3', '.'],
                         ['.', '9', '.', '.', '1', '8', '7', '4', '5'],
                         ['1', '3', '.', '.', '4', '9', '.', '.', '.'],
                         ['9', '.', '.', '8', '.', '.', '6', '.', '3'],
                         ['2', '.', '6', '.', '.', '1', '9', '8', '.'],
                         ['5', '.', '4', '9', '6', '2', '3', '.', '.'],
                         ['.', '.', '.', '.', '8', '.', '.', '2', '.'],
                         ['.', '2', '.', '.', '.', '4', '5', '.', '.']
                        ];
    axios
      .post(baseURL ,{
        body: JSON.stringify(sudokuBoard)})
      .then((response) => {

      });
//     const resp =  fetch(baseURL , {
//   method : "POST",
//   mode: 'cors',
//   headers: {
//     'Content-Type': 'application/json'
//   },
//   body: "hjbcdghjdghjegfhjg"
// });
  }

  // function showModal(){
  //     setModalOpen(true);
  // }

  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      <h4 id='title'>SUDOKU SOLVER</h4>
      <Board ref={Sboard}/>
      <div>
        <Button variant="contained" color="success" id="btn" onClick={ValidateAndSend}>SOLVE</Button>
      </div>
      {modalOpen && <Modal setOpenModal={setModalOpen} />}
    </div>
  );
}

export default App;
