#!/usr/bin/env node

"use strict";

class Node {
	constructor(data, next=null) {
		this.data = data;
		this.next = next;
	}
}

class SinglyLinkedList {
	constructor() {
		this._head = null;
		this._size = 0;
	}

	get length() {
		return this._size;
	}

	get array() {
		let array = [];
		let node = this._head;

		while (node !== null) {
			array.push(node.data);
			node = node.next;
		}

		return array;
	}

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

	append(data) {
		this.insert(data, this._size);
	}

	appendFront(data) {
		this.insert(data, 0);
	}

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

	popLast() {
		return this.popFrom(this._size - 1);
	}

	popFront() {
		return this.popFrom(0);
	}
}

module.exports = SinglyLinkedList;