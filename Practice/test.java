public class test{
    public static void main(String args[]){

        // int arr[] = {13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7};
        int arr[] = {-10, 56, -34, 78, 90, 10, -9, -19, 45, 67, 5};

        

        int maxi = Integer.MIN_VALUE;
        int sum = 0,start=-1,end=-1;

        for(int i=0;i<arr.length;i++){
            sum += arr[i];
            //Final ans (Maximum sum):
            if(maxi<sum){
                maxi = sum;
                end = i;
            }
            System.out.print(sum+"("+maxi+")"+"\t");
            //Special case:
            if(sum<0){
                sum = 0;
                start=i+1;
            }
        }

        System.out.println("\n"+maxi);
        System.out.println(start+" "+end);

    }
}