#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const ints = process.argv.map((x) => parseInt(x)).filter((x) => !isNaN(x));
  ints.sort((a, b) => b - a);
  console.log(ints[1]);
}
