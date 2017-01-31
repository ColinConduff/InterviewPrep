#!/usr/bin/env node

"use strict";

function quickSort(seq) {
	_quicksort(seq, 0, seq.length - 1);
}

function _quicksort(seq, leftIndex, rightIndex) {
	if (seq.length > 1 && leftIndex < rightIndex) {
		const pivotIndex = Math.floor(Math.random() * (rightIndex-leftIndex) + leftIndex);
		const newPivotIndex = _partition(seq, leftIndex, rightIndex, pivotIndex);

		_quicksort(seq, leftIndex, newPivotIndex - 1);
		_quicksort(seq, newPivotIndex + 1, rightIndex);
	}
}

function _partition(seq, leftIndex, rightIndex, pivotIndex) {
	const pivotValue = seq[pivotIndex];
	let newPivotIndex = leftIndex;
	[seq[pivotIndex], seq[rightIndex]] = [seq[rightIndex], seq[pivotIndex]];

	for (let i = leftIndex; i < rightIndex; i++) {
		if (seq[i] < pivotValue) {
			[seq[newPivotIndex], seq[i]] = [seq[i], seq[newPivotIndex]];
			newPivotIndex += 1;
		}
	}

	[seq[newPivotIndex], seq[rightIndex]] = [seq[rightIndex], seq[newPivotIndex]];
	return newPivotIndex;
}

module.exports = quickSort;