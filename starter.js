const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', line => {
  const nums = line.split(' ');
  const a = parseInt(nums[0]);
  const b = parseInt(nums[1]);
        console.log(a)
        console.log(b)
});
