const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', line => {
  const nums = line.split(' ');
  const A = parseInt(nums[0]);
  const I = parseInt(nums[1]);
  const res = A * (I -1) + 1;

    console.log(res)
});
