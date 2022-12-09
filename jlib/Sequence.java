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

	public void add(T e) {
		if (this.previous.size() == this.max) {
			this.previous.pop();
		}
		this.previous.add(e);
	}

	public Integer size() {
		return this.previous.size();
	}

	public Boolean isUnique() {
		HashSet<T> s = new HashSet<>();
		for (T e : this.previous) {
			s.add(e);
		}
		return s.size() == this.max;
	}
}
