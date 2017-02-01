#!/usr/bin/env node

"use strict";

class LinkedList {
	constructor() {
		this._head = null;
		this._size = 0;
	}

	get length() {
		return this._size;
	}

	get toArray() {
		throw new Error("toArray function not implemented.");
	}

	insert(data, index) { 
		throw new Error("Insert function not implemented.");
	}

	popFrom(index) { 
		throw new Error("popFrom function not implemented.");
	}

	append(data) { 
		this.insert(data, this._size);
	}

	appendFront(data) {
		this.insert(data, 0); 
	}

	popLast() {
		return this.popFrom(this._size - 1);
	}

	popFront() {
		return this.popFrom(0);
	}
}

module.exports = LinkedList;