#!/usr/bin/env node

"use strict";

function bubbleSort(seq) {
	for (let i = 0; i < seq.length; i++) { // i unused
		let swapsMade = 0;

		for (let n = 1; n < seq.length; n++) {
			if (seq[n-1] > seq[n]) {
				[seq[n-1], seq[n]] = [seq[n], seq[n-1]];
				swapsMade += 1;
			} 
		}

		if (swapsMade == 0) { break; }
	}
}

module.exports = bubbleSort;