package object.ensyu;

public class Maruyama {
	public static void main (String[] args) {
		int num = 10;
		int[] array = {8, 7, 2, 5, 3, 1};
		int[] array2 = {1, 2, 3, 5, 7, 8};
		
		
//		System.out.println("ペアの組み合わせ");
//		for (int i = 0; i < array.length; i++) {
//			for (int j = array.length - 1; j > i; j-- ) {
//				if (array[i] + array[j] == 10) {
//				System.out.println(array[i] + "と" + array[j]);
//				}
//			}
//		}
		

		int i = 0;
		int j = array2.length -1;
		System.out.println("開始");
		while (i != j) {
			if (array2[i] + array2[j] == 10) {
				System.out.println(array2[i] + "と" + array2[j]);
				i++;
			}	else if(array2[i] + array2[j] > 10) {
				j--;
			}else {
				i++;
			} 
		}	
		System.out.println("終了");
	}
}
