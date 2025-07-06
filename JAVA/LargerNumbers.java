import java.math.BigInteger;

public class LargerNumbers {
    public static void main(String[] args) {
        BigInteger A = new BigInteger("78912818016345");
        System.out.println(A);

        // for primitives
        BigInteger a = BigInteger.valueOf(37818);
        System.out.println(a);
        BigInteger myNumber = factorial(100);
        System.out.println(myNumber);
        BigInteger myNumber2 = factorial(160);
        System.out.println(myNumber2);

        BigInteger largeNumber = new BigInteger(
                "36536810454385287258475864820648632108635026501285603632873801360806562183601286584786");
        System.out.println(largeNumber);
    }

    public static BigInteger factorial(int number) {
        BigInteger answer = new BigInteger("1");
        for (int i = 2; i <= number; i++) {
            answer = answer.multiply(BigInteger.valueOf(i));
        }

        return answer;
    }
}
