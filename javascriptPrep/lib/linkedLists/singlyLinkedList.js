#!/usr/bin/env node

"use strict";

const LinkedList = require('./LinkedList');

class Node {
	constructor(data, next=null) {
		this.data = data;
		this.next = next;
	}
}

class SinglyLinkedList extends LinkedList {

	// Override array
	get toArray() {
		let array = [];
		let node = this._head;

		while (node !== null) {
			array.push(node.data);
			node = node.next;
		}

		return array;
	}

	// Override insert
	insert(data, index) {
		if (index < 0 || index > this._size) {
			throw new Error("Index Out of Range");
		}

		this._size += 1;

		if (index === 0) {
			this._head = new Node(data, this._head);
		
		} else {
			let position = 1;
			let node = this._head;

			while (position !== index) {
				node = node.next;
				position += 1;
			}

			node.next = new Node(data, node.next);
		}
	}

	// Override popFrom
	popFrom(index) {
		if (index < 0 || index >= this._size) {
			throw new Error("Index Out of Range");
		}

		this._size -= 1;
		let nodeToReturn = null;

		if (index === 0) {
			nodeToReturn = this._head;
			this._head = this._head.next;
		
		} else {
			let position = 1;
			let node = this._head;

			while (position !== index) {
				node = node.next;
				position += 1;
			}

			nodeToReturn = node.next;
			node.next = node.next.next;
		}

		return (nodeToReturn !== null) ? nodeToReturn.data : null;
	}
}

module.exports = SinglyLinkedList;