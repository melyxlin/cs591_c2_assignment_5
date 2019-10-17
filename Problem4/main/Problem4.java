package main;
import java.util.Arrays;

public class Problem4 {

	public static int findSmallestPositve(int[] a) {
		Arrays.sort(a);
		boolean neg = true;
		int prev = a[0];
		for (int i = 0; i < a.length; i++) {
			if (neg) {
				if (a[i] < 0)
					continue;
				else if (a[i] >= 0) {
					if (a[i] != 0) {
						return 0;
					}
					prev = a[i];
					neg = false;
				}
			} else {
				if (a[i] != prev && a[i] != prev + 1)
					return prev + 1;
				prev = a[i];
			}
		}
		return a[a.length - 1] + 1;
	}
	public static void main(String[] args) {

		int[] array = new int[args.length];
		for (int i = 0; i < args.length; i++) {
			array[i] = Integer.parseInt(args[i]);
		}
		
		System.out.println(findSmallestPositve(array));


	}

}
