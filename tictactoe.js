let gameBoard = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
];

let currentPlayer = 'X';

function handleCellClick(event) {
    const row = event.target.parentNode.rowIndex;
    const col = event.target.cellIndex;
    if (gameBoard[row][col] === '') {
        gameBoard[row][col] = currentPlayer;
        event.target.textContent = currentPlayer;
        checkForWin();
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    }
}

function checkForWin() {
    // implement win condition logic here
    console.log('Implement win condition logic');
}

document.querySelectorAll('td').forEach(cell => {
    cell.addEventListener('click', handleCellClick);
});
