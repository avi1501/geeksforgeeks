import java.util.*;
class avi{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("enter the Palindrome");
        String str = scan.next();
        String sacvar = "" ;
        for (int i =str.length()-1;i>=0;i--){
            sacvar = sacvar+str.charAt(i);
        }
        if(sacvar.equals(str)){
            System.out.println("String is palindrome");
        }        
        else{
            System.out.println("String is not a palindrome");
        }


    }
}