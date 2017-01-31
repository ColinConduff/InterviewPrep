#!/usr/bin/env node

"use strict";

const insertionSort = require('./insertionSort');
const countingSort = require('./countingSort');
const bubbleSort = require('./bubbleSort');
const selectionSort = require('./selectionSort');
const quickSort = require('./quickSort');
const mergeSort = require('./mergeSort');

module.exports = {  
	insertionSort,
	countingSort,
	bubbleSort,
	selectionSort,
	quickSort,
	mergeSort
}