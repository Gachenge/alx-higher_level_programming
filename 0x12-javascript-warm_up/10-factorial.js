#!/usr/bin/node

// recursively find factorial

function factorial(num){
	if (num >1){
		return num * factorial(num - 1);
	}
	return 1;
}
console.log(factorial(Number(process.argv[2])));