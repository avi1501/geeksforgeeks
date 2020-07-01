import java.util.*; 
public class passwordstable {
    public static boolean isNumBalanced(int num){ 
		num=Math.abs(num); 
		
		String str=num+""; 
		
		char[] ch_arr=str.toCharArray(); 
		
		HashSet<Character> hs=new HashSet<Character>(); 
		for(char ch:ch_arr){ 
		
            hs.add(ch); 
		} 
		int str_len=str.length(); 
		int hs_len=hs.size(); 
		if(hs_len<=str_len/2 || hs_len==str_len) 
		{ 
			return true; 
		} 
		return false; 
		
    } 
    public static int findpassword(int input1,int input2,int input3,int input4,int input5){
        int stable=0;
        int unstable =0;
        int i=0;
        int[] arr=new int[]{input1,input2,input3,input4,input5};
        while(i!=5){
        if(isNumBalanced(arr[i])){
            stable += arr[i];
        }
        else{
            unstable += arr[i];
        }
        i += 1;
    }

        return stable-unstable;
    }
    public static void main(String[] args){
        int a=1221;
        int b = 3221;
        int c = 7447;
        int d = 900;
        int e = 9009;
        int result = findpassword(a,b,c,d,e);
        System.out.println(result);
    }
}