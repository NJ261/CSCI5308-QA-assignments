public class Calculator {
    public static int Add(int left, int right) {
        Addition addition = new Addition(right, right);

        return addition.GetResult();
    }

    public static int Divide(int left, int right) {
        Division division = new Division(left, right);

        return division.GetResult();
    }

    public static int Multiply(int left, int right) {
        Multiplication multiplication = new Multiplication(left, right);

        return multiplication.GetResult();
    }

    public static int Subtract(int left, int right) {
        Substraction substraction = new Substraction(left, right);

        return substraction.GetResult();
    }
}


