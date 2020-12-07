let board = ['','','','','','','','','']
let player1 = 'X';
let player2 = 'O';
let endGame = false;

let currentPlayer = player1;
let winningMessage = () => `${currentPlayer} has won the game!`;
let playerMessage = () => `It's ${currentPlayer}'s move`;
const drawMessage = "Game ends in a Draw";

let statusDisplay = document.querySelector('.game--status');
statusDisplay.innerHTML = playerMessage();

// calls cellMove if spot is free
function cellClicked(cellEvent) {
	cellElement = cellEvent.target
	i = cellElement.getAttribute('data-cell-index');
	if (checkMove(i) && !endGame) {
		cellMove(i);
	}
};

// changes the cell to the currentPlayer marker
function cellMove(index) {
	board[index] = currentPlayer;
	drawBoard(board);
	endGame = checkState(board);
	if (!endGame) {
		playerChange();
	}
};

// draws the board to the HTML also calls the check state
function drawBoard(board) {
	board.forEach(function(spot,index) {
			cells[index].innerText = spot;
		}
	);
}

// switches the current player and displays the status message
function playerChange() {
	if (!endGame) {
		if (currentPlayer == player1) {
			currentPlayer = player2;
		} else if (currentPlayer == player2) {
			currentPlayer = player1;
		}
		statusDisplay.innerHTML = playerMessage();
	}
};

// resets the state of the game and assigns randomly a new player
function restartGame() {
	board = ['','','','','','','','',''];
	drawBoard(board);
	num = Math.round(Math.random());
	endGame = false;
	switch (num) {
		case 0:
			currentPlayer = player1;
			break;
		case 1:
			currentPlayer = player2;
	}
	statusDisplay.innerHTML = playerMessage();
};

// returns true if the spot is empty
function checkMove(index) {
	if (board[index] == '') {
		return true;
	} else {
		return false;
	}
};

// checks if the board has a winner or is draw
function checkState(board) {
	winStates = [
		// wining across
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		// winning down
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		// winning diag
		[0, 4, 8],
		[2, 4, 6]
	];
	for (i = 0; i < winStates.length; i++) {
		let winState = winStates[i];
		if (board[winState[0] ]==player1 && board[winState[1]]==player1 && board[winState[2]]==player1) {
			statusDisplay.innerHTML = winningMessage();
			return true;
		} else if (board[winState[0] ]==player2 && board[winState[1]]==player2 && board[winState[2]]==player2) {
			statusDisplay.innerHTML = winningMessage();
			return true;
		} 	
	};
	for (i = 0; i < 9; i++) {
		if (board[i] == '') {
			return false;
		}
	}
	statusDisplay.innerHTML = drawMessage;
	return true;
};


// adds iterativity to the cell class and restart button class
let cells = document.querySelectorAll('.cell')
cells.forEach(
	cell => cell.addEventListener('click',cellClicked)
);
document.querySelector('.game--restart').addEventListener('click',restartGame);

