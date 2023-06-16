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
  var sudokuBoardState = [];
  
  function validateRows(board){
    const set =new Set();
    for(let i=0; i<9; i++){
      set.clear();
      for(let j=0; j<9; j++){
        if(board[i][j] !== '.'){
          if(set.has(board[i][j]))
            return false;
          set.add(board[i][j]);
        }
      }
    }
    return true;
  }

  function validateColumns(board){
    const set =new Set();
    for(let j=0; j<9; j++){
      set.clear();
      for(let i=0; i<9; i++){
        if(board[i][j] !== '.'){
          if(set.has(board[i][j]))
            return false;
          set.add(board[i][j]);
        }
      }
    }
    return true;
  }

  function validateBlocks(board){
    const set = new Set();
    for(let i=0; i<3; i++){
      for(let j=0; j<3 ;j++){
        set.clear();
        for(let rw=i*3; rw<(i+1)*3; rw++){
          for(let cl=j*3; cl<(j+1)*3; cl++){
            if(board[rw][cl] !== '.'){
              if(set.has(board[rw][cl]))
                return false;
              set.add(board[rw][cl]);
            }
          }
        }
      }
    }
    return true;
  }

  function Validate(e){
    const inputs = Sboard.current.children;
    const boardState={};
    sudokuBoardState = [];
    for(const input of inputs){
      boardState[input.id] = input.value;
    }
    for(let i=0; i<9; i++){
      var row = [];
      for(let j=0; j<9; j++){
        let inputID = i*9+j+1;
        if(boardState[inputID] === '')
          row.push('.');
        else
          row.push(boardState[inputID]);
      }
      sudokuBoardState.push(row);
    }
    console.log(boardState);
    console.log(sudokuBoardState);

    const isValidSudoku = validateRows(sudokuBoardState) && validateColumns(sudokuBoardState) && validateBlocks(sudokuBoardState);
    console.log(isValidSudoku);

    if(isValidSudoku){
      axios
      .post(baseURL ,{
        body: JSON.stringify(sudokuBoardState)
      })
      .then((response) => {
          console.log(response["data"]["SolvedGrid"]);
          setSolvedGridonUI(response["data"]["SolvedGrid"]);
      });
    }
    else{
      setModalOpen(true);
    }
  }

  function setSolvedGridonUI(solvedGrid){
    const boardState={};
    for(let i=0; i<9; i++){
      for(let j=0; j<9; j++){
        let inputID = i*9+j+1;
        boardState[inputID] = solvedGrid[i][j];
      }
    }
    const inputs = Sboard.current.children;
    for(const input of inputs){
      if(input.value === ''){
        input.style.backgroundColor = "lightgreen";
      }
      input.value = boardState[input.id];
    }
  }

 

  return (
    <div className="App">
      <h4 id='title'>SUDOKU SOLVER</h4>
      <Board ref={Sboard}/>
      <div>
        <Button variant="contained" color="success" id="btn" onClick={Validate}>SOLVE</Button>
      </div>
      {modalOpen && <Modal setOpenModal={setModalOpen} />}
    </div>
  );
}

export default App;
