const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let x,
  y,
  n = 0;

const solveQuadrant = (x, y) => {
  if (x > 0 && y > 0) console.log(1);
  else if (x < 0 && y > 0) console.log(2);
  else if (x < 0 && y < 0) console.log(3);
  else if (x > 0 && y < 0) console.log(4);
};

rl.on('line', line => {
  n++;
  const a = parseInt(line);
  if (n === 1) x = a;
  else if (n === 2) {
    y = a;
    solveQuadrant(x, y);
  }
});
