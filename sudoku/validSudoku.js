/**
 * @param {character[][]} board
 * @return {boolean}
 */
const N = 9;


function validRows(board) {
    for (let i = 0; i < N; i++) {
        const seen = new Set();
        for (let j = 0; j < N; j++) {
            const x = board[i][j];
            if (x === '.') {
                continue;
            }
            if (seen.has(x)) {
                return false;
            }
            seen.add(x);
        }
    }
    return true;
}

function validColumns(board) {
    for (let i = 0; i < N; i++) {
        const seen = new Set();
        for (let j = 0; j < N; j++) {
            const x = board[j][i];
            if (x === '.') {
                continue;
            }
            if (seen.has(x)) {
                return false;
            }
            seen.add(x);
        }
    }
    return true;
}

function validBoxes(board) {
    let iStart = 0;
    let jStart = 0;
    while (jStart < 9) {
        const seen = new Set();
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const x = board[i + iStart][j + jStart];
                if (x === '.') {
                    continue;
                }
                if (seen.has(x)) {
                    return false;
                }
                seen.add(x);
            }
        }
        iStart += 3;
        if (iStart === 9) {
            iStart = 0;
            jStart += 3;
        }
    }
    return true;
}

var isValidSudoku = function(board) {
    return validRows(board) 
        && validColumns(board)
        && validBoxes(board);
};
