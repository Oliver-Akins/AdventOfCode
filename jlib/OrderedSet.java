package jlib;

import java.util.HashSet;
import java.util.Stack;

public class OrderedSet<T> extends HashSet<T> {
	private Stack<T> order;

	public OrderedSet() {
		this.order = new Stack<T>();
	}

	@Override
	public boolean add(T e) {
		if (super.add(e)) {
			this.order.add(e);
			return true;
		}
		return false;
	}

	/**
	 * Removes the most recently added element from the set
	 *
	 * @return The element that was removed from the set
	 */
	public T pop() {
		T e = this.order.pop();
		this.remove(e);
		return e;
	}

	public T top() {
		return this.order.peek();
	}
}
