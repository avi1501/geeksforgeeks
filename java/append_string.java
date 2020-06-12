import java.util.Scanner;
class appendstring{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		System.out.println("Input first string");
		String s1 = scan.next();
		System.out.println("Input second string");
		String s2 = scan.next();
		String s3 = s1+s2;
		
		if(s3.charAt(s1.length()-1) == s3.charAt(s1.length())){
		s3 = s3.substring(0,s1.length())+s3.substring(s1.length()+1);
		}
		s3.toLowerCase();
		System.out.println(s3);
		scan.close();	
	}
}

