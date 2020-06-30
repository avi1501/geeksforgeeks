class findKey{
    public static void main(String[] args){
        int input1 = 3522;
        int input2 = 2522;
        int input3 = 1715;
        int div = 1000;
        int result = 0;

        while (div>0){
            
            int a = input1/div;
            int b = input2/div;
            int c = input3/div;
            if((a>=b) && (a>=c)){
                result += a*div;
            }
            else if((b>=a) && (b>=c)){
                result += b*div;
            }
            else{
                result += c*div;
            }
            input1 = input1%div;
            input2 = input2%div;
            input3 = input3%div;
            
            div = div/10;
            
        }
        System.out.println(result);


    }
}