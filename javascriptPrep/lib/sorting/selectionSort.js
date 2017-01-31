#!/usr/bin/env node

"use strict";

function selectionSort(seq) {
	for (let outerIndex = 0; outerIndex < seq.length; outerIndex++) {
		let minIndex = outerIndex;

		for (let innerIndex = outerIndex+1; innerIndex < seq.length; innerIndex++) {
			if (seq[innerIndex] < seq[minIndex]) {
				minIndex = innerIndex;
			}
		}

		[seq[outerIndex], seq[minIndex]] = [seq[minIndex], seq[outerIndex]];
	}
}

module.exports = selectionSort;