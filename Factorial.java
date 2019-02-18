import java.util.Scanner;
class Factorial{
	public static void main(String[] args){
		Scanner  scan = new Scanner(System.in);
		System.out.println("Enter a number");
		int n = scan.nextInt();

		int res = factorial(n);
		System.out.println(res);



	}

	public static int factorial(int n){
		if(n==0){
		return 1;

		}else{
			int res  = n*factorial(n-1);
		return res;

			
		}
		
	}
}