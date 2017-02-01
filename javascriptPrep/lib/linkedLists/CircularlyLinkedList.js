#!/usr/bin/env node

"use strict";

const LinkedList = require('./LinkedList');

class Node {
	constructor(data, next=null, prev=null) {
		this.data = data;
		this.next = next;
		this.prev = prev;
	}
}

class CircularlyLinkedList extends LinkedList {

	// Override array
	get toArray() {
		let array = [];

		if (this._head !== null) {
			array.push(this._head.data);
			let node = this._head.next;

			while (node !== this._head) {
				array.push(node.data);
				node = node.next;
			}
		}

		return array;
	}

	// Override insert
	insert(data, index) {
		if (index < 0 || index > this._size) {
			throw new Error("Index Out of Range");
		}

		this._size += 1;

		if (this._head === null) {
			this._head = new Node(data);
			this._head.next = this._head;
			this._head.prev = this._head;
		
		} else if (index === 0 || index === this._size) {
			this._head = new Node(data, this._head, this._head.prev);
			this._head.prev.next = this._head;
			this._head.next.prev = this._head;
		
			if (index === this._size) {
				this._head = this._head.next;
			}
		
		} else {
			let position = 1;
			let node = this._head;

			while (position !== index) {
				node = node.next;
				position += 1;
			}

			node.next = new Node(data, node.next, node);
			node.next.next.prev = node.next;
		}
	}

	// Override popFrom
	popFrom(index) {
		if (index < 0 || index >= this._size) {
			throw new Error("Index Out of Range");
		}

		let nodeToPop = null;

		if (this._size === 1) {
			nodeToPop = this._head;
			this._head = null;

		} else if (index === 0) {
			nodeToPop = this._head;
			this._head = this._head.next;

		} else if (index === this._size - 1) {
			nodeToPop = this._head.prev;
		
		} else {
			let position = 1;
			nodeToPop = this._head.next;

			while (position != index) {
				nodeToPop = nodeToPop.next;
				position += 1;
			}
		}

		nodeToPop.prev.next = nodeToPop.next;
		nodeToPop.next.prev = nodeToPop.prev;

		this._size -= 1;

		return nodeToPop.data;
	}
}

module.exports = CircularlyLinkedList;