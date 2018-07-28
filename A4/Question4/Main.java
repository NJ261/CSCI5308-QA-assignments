public class Main {
    public static void main(String[] args) {
        boolean pass = (Calculator.Divide(10, 2) == 5)
                       && (Calculator.Multiply(5, 2) == 10)
                       && (Calculator.Add(2, 2) == 4)
                       && (Calculator.Subtract(10, 2) == 8);

        if (pass) {
            System.out.println("PASS");
        } else {
            System.out.println("FAIL");
        }
    }
}


//~ Formatted by Jindent --- http://www.jindent.com
