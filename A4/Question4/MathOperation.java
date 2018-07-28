public class MathOperation {
    private int leftOperand;
    private int rightOperand;

    public MathOperation(int leftOperand, int rightOperand) {
        this.leftOperand  = leftOperand;
        this.rightOperand = rightOperand;
    }

    public int getLeftOperand() {
        return leftOperand;
    }

    public void setLeftOperand(int leftOperand) {
        this.leftOperand = leftOperand;
    }

    public int getRightOperand() {
        return rightOperand;
    }

    public void setRightOperand(int rightOperand) {
        this.rightOperand = rightOperand;
    }
}


