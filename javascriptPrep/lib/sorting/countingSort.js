#!/usr/bin/env node

"use strict";

function countingSort(sequence) {

	if (sequence.length <= 1) { return; }

	// The spread operator (...sequence) is similar to python's *sequence
	const minNum = Math.min(...sequence);
	const maxNum = Math.max(...sequence) + 1; // not necessary

	let frequencies = Array(maxNum-minNum).fill(0);

	sequence.forEach(function(num) {
		frequencies[num - minNum]++;
	});

	let seqIndex = 0; // raises appropriate error if out of bounds

	for (let num = minNum; num < maxNum; num++) {
		let frequency = frequencies[num - minNum];

		for (let j = 0; j < frequency; j++) {
			sequence[seqIndex] = num;
			seqIndex += 1; // avoid sequence[seqIndex++]
		}
	}
}

module.exports = countingSort;