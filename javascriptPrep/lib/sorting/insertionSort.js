#!/usr/bin/env node

"use strict";

function insertionSort(seq) {
	seq.forEach(function(currentValue, advIndex, sequence) {
		let retreatingIndex = advIndex - 1;

		while (retreatingIndex >= 0 && sequence[retreatingIndex] > currentValue) {
			sequence[retreatingIndex + 1] = sequence[retreatingIndex];
			retreatingIndex -= 1;
		}

		sequence[retreatingIndex + 1] = currentValue;
	});
}

module.exports = insertionSort;