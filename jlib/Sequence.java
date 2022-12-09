package jlib;

import java.util.HashSet;
import java.util.LinkedList;

public class Sequence<T> {
	private LinkedList<T> previous;
	private Integer max;

	public Sequence(Integer size) {
		this.max = size;
		this.previous = new LinkedList<T>();
	}

	/**
	 * Adds an element to the sequence. If the sequence contains the maximum amount
	 * of elements, it will remove the first element from the sequence.
	 *
	 * @param e The element to add to the sequence
	 */
	public void add(T e) {
		if (this.previous.size() == this.max) {
			this.previous.pop();
		}
		this.previous.add(e);
	}

	/**
	 * Provides info on how many elements are currently in the sequence.
	 *
	 * @return The number of elements in the sequence
	 */
	public Integer size() {
		return this.previous.size();
	}

	/**
	 * Determines if all of the elements in the sequence are unique or not.
	 */
	public Boolean isUnique() {
		HashSet<T> s = new HashSet<>();
		for (T e : this.previous) {
			s.add(e);
		}
		return s.size() == this.max;
	}
}
