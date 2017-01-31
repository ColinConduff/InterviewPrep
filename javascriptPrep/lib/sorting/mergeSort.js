#!/usr/bin/env node

"use strict";

/** Return the sorted sequence. Time: Theta(n log(n)) Space: Theta(n) */
function mergeSort(seq) {
	if (seq.length <= 1) { return seq; }

	const middleIndex = Math.floor(seq.length / 2);

	const left = mergeSort(seq.slice(0, middleIndex));
	const right = mergeSort(seq.slice(middleIndex, seq.length));

	return _merge(left, right);
}

function _merge(left, right) {
	let combined = [];

	function* makeIter(array) { yield* array; }

	const leftIter = makeIter(left);
	const rightIter = makeIter(right);

	let leftCurrent = leftIter.next();
	let rightCurrent = rightIter.next();

	while (!leftCurrent.done && !rightCurrent.done) {
		if (leftCurrent.value < rightCurrent.value) {
			combined.push(leftCurrent.value);
			leftCurrent = leftIter.next();

		} else {
			combined.push(rightCurrent.value);
			rightCurrent = rightIter.next();
		}
	}

	// concat with slice is O(combined.length)

	// push remaining values in left
	while (!leftCurrent.done) {
		combined.push(leftCurrent.value);
		leftCurrent = leftIter.next();
	}

	// push remaining values in right
	while (!rightCurrent.done) {
		combined.push(rightCurrent.value);
		rightCurrent = rightIter.next();
	}

	return combined;
}

module.exports = mergeSort;