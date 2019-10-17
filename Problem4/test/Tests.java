package test;

import static org.junit.Assert.*;

import main.Problem4;

public class Tests {

	public static void main(String[] args) {
		assertEquals(Problem4.findSmallestPositve(new int[]{1,2,0,-1, 3, 5}), 4);
		assertEquals(Problem4.findSmallestPositve(new int[]{1,2, -2,-1, 3, 5}), 0);
		assertEquals(Problem4.findSmallestPositve(new int[]{1,2, -2,-1, 0, 3, 3}), 4);

	}

}
